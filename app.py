from flask import Flask, render_template
import json
import urllib2

app = Flask(__name__)

@app.route("/")
def form():
    uResp = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=s5MDaZjde0L3q7Qcw4aAU0yOx7Git4aHWHcCXaIP")
    string_info = uResp.read()
    dic_info = json.loads(string_info)
    return render_template('home.html', title = dic_info["title"], copy_right = dic_info["copyright"], date = dic_info["date"], explanation = dic_info["explanation"], image1= dic_info["hdurl"], image2=dic_info["url"])

if __name__ == "__main__":
    app.debug = True
    app.run()
