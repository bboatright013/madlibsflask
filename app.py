from flask import Flask
from flask import request, render_template
from stories import Story, story
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
app.debug = True
debug = DebugToolbarExtension(app)


@app.route('/')
def home_():
    return render_template("home.html")

@app.route('/story.html')
def story_time():
    args = request.args

    our_story = {
        "place" : args["place"],
        "noun" : args["noun"],
        "verb" : args["verb"],
        "adjective" : args["adjective"],
        "plural_noun" : args["plural_noun"]
    }
    x = story.generate(our_story)
    return render_template("story.html",return_string = x)