from flask import Flask
from project.interview import configure_routes

app = Flask(__name__)
app.secret_key= 'dljsaklqk24e21cjn!Ew@@dsa5'

configure_routes(app)

if __name__ == '__main__':
    app.run()