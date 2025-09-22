from flask import Flask,request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello user!!!  This is my first time using Flask. Well it is goin so well ."

@app.route("/contact")
def contact():
    return "This is contact me page. Contact me anytime!"

@app.route("/about")
def about():
    return "This is about us page. What do you want to know about me."

@app.route("/submit",methods = ["GET", "POST"])
def submit():
    if request.method == "POST":
        return "You are sending the data"
    else:
        return "You are viewing the data" 

# if __name__ == "__main__":
#     app.run(debug=True)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
