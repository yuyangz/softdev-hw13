'''
Yuyang Zhang
SoftDev1 pd07
HW14 -- Getting More REST
2017-11-12  
'''

from flask import Flask, render_template
import json
import urllib2

app = Flask(__name__)

@app.route("/")
def form():
    uResp = urllib2.urlopen("https://gateway.marvel.com:443/v1/public/characters?apikey=d374bf260e04c8b56a55836e28e8f802")
    string_info = uResp.read()
    dic_info = json.loads(string_info)
    return render_template('home.html', copy_right = dic_info["copyright"], items = dic_info["items"], info = dic_info["results"])

if __name__ == "__main__":
    app.debug = True
    app.run()
