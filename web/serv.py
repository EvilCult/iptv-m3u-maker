from flask import send_from_directory
from Http import app

@app.route('/')
def index():
    return send_from_directory('static', filename='index.html')

if __name__ == '__main__':
    app.run(
        host = '0.0.0.0',
        debug = True
    )