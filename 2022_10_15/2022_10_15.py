# Flask Web app using Python

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')


# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'


# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
