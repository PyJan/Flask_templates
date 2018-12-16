from flask import Flask
from views.profile import profile

app = Flask(__name__)
app.register_blueprint(profile)

if __name__ == '__main__':
    app.run(debug=True)