from flask import Flask

app = Flask(__name__)


################################################
# how to create PATH parameter in Flask?       #
################################################

@app.route("/user/<username>")
def show_user_profile(username):
    # show user profile based on `username`
    return f"User {username} profile...."


###############################################################
# how to create PATH parameter in Flask with data types?      #
###############################################################
@app.route("/story/<int:story_number>")
def show_story(story_number):
    # TODO - REFER
    # https://flask.palletsprojects.com/en/2.2.x/quickstart/#variable-rules
    # LOGIC to show story with given `story_number` (which is a integer)
    return f"DETAIL STORY - story number {story_number}"