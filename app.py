from flask import Flask, request, render_template
# from flask_debugtoolbar import DebugToolbarExtension
from stories import Story, story


app = Flask(__name__)
# app.debug = True
# app.config['SECRET_KEY'] = "madlibkey"
# debug = DebugToolbarExtension(app)

@app.route('/')
def home_():
    return render_template("home.html")

@app.route('/story.html')
def story_time():
    args = request.args

    # stor = Story(["place","noun","verb","adjective","plural_noun"],   
    #  f"""Once upon a time in a long-ago {place}, there lived a
    #    large {adjective} {noun}. It loved to {verb} {plural_noun}.""")
    our_story = {
        "place" : args["place"],
        "noun" : args["noun"],
        "verb" : args["verb"],
        "adjective" : args["adjective"],
        "plural_noun" : args["plural_noun"]
    }
    x = story.generate(our_story)
    return render_template("story.html",return_string = x)