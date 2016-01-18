import os
from flask import Flask, session

app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = 'secret!'


@app.route('/')
def mainIndex():
    print 'in hello world'
    return app.send_static_file('index.html')
    


# start the server
if __name__ == '__main__':
        app.run(host=os.getenv('IP', '0.0.0.0'), port =int(os.getenv('PORT', 8080)), debug=True)
