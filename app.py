from flask import Flask, render_template

app = Flask(__name__)

all_posts = [
    {
        'title': "post 1", 
        'content': "content one",
        'author': 'Mark'
    },
    {
        'title': "post 2", 
        'content': "content two"
    }
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/posts")
def posts():
    return render_template("posts.html", posts = all_posts)

if __name__ == "__main__":
    app.run(debug = True)