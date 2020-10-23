from burdy import create_app
from waitress import serve
import tensorflow as tf

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    # FOR PRODUCTION ONLY
    # serve(app, host='localhost', port=82)
