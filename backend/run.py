from burdy_app import app
from waitress import serve

if __name__ == '__main__':
    app.run(debug=True)
    # FOR PRODUCTION ONLY
    # serve(app, host='localhost', port=82)
