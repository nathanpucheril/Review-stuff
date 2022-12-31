from flask import request, jsonify, app as flask_app
from flask_sqlalchemy import SQLAlchemy

from reviewstuff.database.models import Base, User, Account, Project, Review


def routes(app: flask_app, db: SQLAlchemy):
    @app.route('/health')
    def health():
        return jsonify({"result": "healthy"})

    @app.route('/init')
    def init():
        Base.metadata.create_all(db.engine)
        db.session.commit()
        return jsonify({})

    @app.post('/<model_type>/v1/create')
    def generic_model_create(model_type):
        model_ref = get_model_ref_from_type_str(model_type)
        content = request.json
        db.session.add(model_ref(**content))
        db.session.commit()
        return jsonify({"result": "success"})

    @app.get('/<model_type>/v1/get_by_id/<id_>')
    def generic_model_get_by_id(model_type, id_):
        model_ref = get_model_ref_from_type_str(model_type)
        model = db.session.query(model_ref).filter(model_ref.id == id_).one()
        return jsonify(dict(model))

    @app.get('/user/v1/get_by_email/<email>')
    def user_get_by_email(email):
        user = db.session.query(User).filter(User.email == email).one()
        return jsonify(dict(user))

    @app.get('/review/v1/get_by_project_id/<id>')
    def review_get_by_project_id(id):
        res = db.session.query(Review).filter(Review.project_id == id).all()
        return jsonify(dict(res))

    def get_model_ref_from_type_str(model_type: str) :
        if model_type == "user":
            return User
        elif model_type == "account":
            return  Account
        elif model_type == "project":
            return Project
        elif model_type == "review":
            return  Review
        raise Exception("unknown model type to get")

