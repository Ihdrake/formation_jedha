from flask import Flask
from flask import request
from flask import jsonify,redirect,url_for, request,render_template,make_response
import requests

app = Flask(__name__)

dark_sky_api_key = "ea0e6cfdcb0f8d10e11ce1be72f5d985"
ipstack_api_key ="a5df38961a6e333dd3ba62c904ea28af"

@app.route("/" ,  methods=["GET", "POST"])
def index():
    current_location = requests.get("http://api.ipstack.com/check", params={"access_key":ipstack_api_key}).json()
    lat = current_location["latitude"]
    long = current_location["longitude"]
    dark_sky = requests.get("https://api.darksky.net/forecast/{}/{},{}".format(dark_sky_api_key,lat,long), params={"lang":"fr"}).json()
    response = make_response(render_template("index.html",
                            forecast = dark_sky))

    return response



#Get ip of user on website 
#@app.route("/get_my_ip", methods=["GET"])
#def get_my_ip():
#    return jsonify({'ip': request.remote_addr}), 200





if __name__ == '__main__':
    app.run(debug=True)


