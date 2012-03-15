from settings import users
from main import session

def authenticate( username, password ):
    for user in users:
        if user.username == username and user.password == password:
            session.user = user
            return True
        
    return False

def logged_in():
    if session.has_key( 'user' ):
        return True
    else:
        return False
    
def logged_in_user():
    if logged_in():
        return session.user
    else:
        return None
    
def logout():
    session.kill()