from flask import Flask, render_template
import random


app = Flask(__name__)

# list of cat images
images = [
        "http://scratchpads.eu/explore/sites-list"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('inde.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0.")

