from flask import request, jsonify, app as flask_app
from flask_sqlalchemy import SQLAlchemy

from reviewstuff.database.models import Base, User, Account, Project, Review


def routes(app: flask_app, db: SQLAlchemy):

    @app.route('/health')
    def health():
        return jsonify({"result":"healthy"})

    @app.route('/init')
    def init():
        Base.metadata.create_all(db.engine)
        db.session.commit()
        return jsonify({})

    @app.post('/user/v1/create')
    def user_create():
        content = request.json
        db.session.add(User(**content))
        db.session.commit()
        print(content)
        return jsonify({})

    @app.get('/user/v1/get_by_id/<id>')
    def user_get_by_id(id):
        print(id)

        res = db.session.query(User).filter(User.id == id).all()
        for r in res:
            print(r)

        return jsonify({})

    @app.get('/user/v1/get_by_email/<email>')
    def user_get_by_email(email):

        res = db.session.query(User).filter(User.email == email).all()
        for r in res:
            print(r)

        return jsonify({})

    @app.post('/review/v1/create')
    def review_create():
        content = request.json
        db.session.add(Review(**content))
        db.session.commit()
        return jsonify({})


    @app.get('/review/v1/get_by_project_id/<id>')
    def review_get_by_project_id(id):

        res = db.session.query(Review).filter(Review.project_id == id).all()
        for r in res:
            print(r)

        return jsonify({})

    @app.post('/project/v1/create')
    def project_create():
        content = request.json
        db.session.add(Project(**content))
        db.session.commit()
        return jsonify({})

    @app.post('/account/v1/create')
    def account_create():
        content = request.json
        db.session.add(Account(**content))
        db.session.commit()
        return jsonify({})