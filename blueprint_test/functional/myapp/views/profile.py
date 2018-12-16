from flask import Blueprint

profile = Blueprint('profile', __name__)

@profile.route('/<username>/desk')
def desk(username):
    return 'Your name is ' + username

@profile.route('/<username>/photos')
def photos(username):
    return 'Photos for ' + username 