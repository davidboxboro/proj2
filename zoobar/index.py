from flask import g, render_template, request
from login import requirelogin
from debug import *
from zoodb import *

import profilemod_client

@catch_err
@requirelogin
def index():
    warning = None
    if 'profile_update' in request.form:
        persondb = person_setup()
        person = persondb.query(Person).get(g.user.person.username)
        persondb.commit()

        profile = request.form['profile_update']

        # update profile via RPC call to profilemod service 
        success = profilemod_client.update(
                g.user.person.username, profile, g.user.token)
        if not success:
            # if token invalid, return
            warning = "Profile update failed" 
        else:
            # also update the cached version (see login.py)
            g.user.person.profile = profilemod_client.read(
                    g.user.person.username)
    return render_template('index.html', warning=warning)
