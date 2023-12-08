# pyright: reportMissingModuleSource=false
# pyright: reportMissingImports=false
from flask import send_from_directory
from Http import app

@app.route('/')
def index():
    return 'Congratulations🎉 <br> The project started successfully🍻'
    # return send_from_directory('static', filename='index.html')

if __name__ == '__main__':
    app.run(
        host  = '0.0.0.0',
        port  = 55120,
        debug = True
    )
