from flask import Flask, render_template

#new object
app = Flask(__name__)

#controller - handler
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/contact")
def icontact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(use_reloader=True)