from web import create_app, db

if __name__ == '__main__':
    flask_app = create_app('dev')

    flask_app.run()