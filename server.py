from flask import Flask, render_template, url_for

app = Flask(__name__)
print(__name__)



@app.route("/")
def my_home():
    print(url_for('static', filename='images/favicon.ico'))
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/blog/2020/dogs")
def blog2():
    return "<p>This is my dog</p>"
