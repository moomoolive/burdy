from burdy import create_app
from waitress import serve
import sys

sys.path.append('C:\\Users\\Mostafa Elbannan\\Desktop\\Programming\\Projects\\burdy_app\\backend\\burdy\\main')
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    # FOR PRODUCTION ONLY
    # serve(app, host='localhost', port=82)
