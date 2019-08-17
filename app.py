from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://www.catgifpage.com/nice-ride-dolly",
    "https://www.catgifpage.com/ginger-is-ready",
    "http://www.catgifpage.com/gifs/317.gif",
    "http://www.catgifpage.com/gifs/324.gif",
    "http://www.catgifpage.com/gifs/315.gif",
    "http://www.catgifpage.com/gifs/309.gif",
    "http://www.catgifpage.com/gifs/306.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
