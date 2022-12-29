import reviewstuff

if __name__ == '__main__':
    app = reviewstuff.create_app()
    app.run(debug=True)
