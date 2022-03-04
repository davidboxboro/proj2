from zoodb import *
from debug import *
import auth_client

def create_empty(username):
    profiledb = profile_setup()
    profile = Profile()
    profile.username = username
    profiledb.add(profile)
    profiledb.commit()

def update(username, new_profile, token):
    # check that token is valid
    # if not, don't let user update profile 
    valid_token = auth_client.check_token(username, token)
    if not valid_token:
        return False

    profiledb = profile_setup()
    profile = profiledb.query(Profile).get(username)
    profile.profile = new_profile
    profiledb.commit()
    return True

def read(username):
    profiledb = profile_setup()
    profile = profiledb.query(Profile).get(username)
    return profile.profile
