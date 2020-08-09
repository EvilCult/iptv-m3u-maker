from Http import app

@app.route('/')
def index():
    return 'Welcome!!'

if __name__ == '__main__':
    app.run(
        host = '0.0.0.0',
        debug = True
    )