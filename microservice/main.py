from app import create_app, init_api

app = create_app()
init_api(app)

if __name__ == '__main__':
    app.run(port=5010, host='0.0.0.0', debug = True)