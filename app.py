from flask import Flask

app = Flask(__name__)

@app.route("/")
def form():
    return render_template('home.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
