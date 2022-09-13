from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")
    
@app.get("/about")
def about():
    me = {
        "first_name" : "Megan",
        "last_name" : "Paquin",
        "hobbies" : "Crafts",
        "bio" : "I have a Biomedical Engineering degree from Syracuse University and I am currently studying to be a web developer. I aspire to be a Software Engineer for medical devices and medical software. I served in the Army for 8 years."
    }

    return render_template("about.html", about_dict=me)

@app.get("/databases")
def databases():
    return render_template("databases.html")