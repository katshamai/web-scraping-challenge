from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mission_to_mars_db"
mongo = PyMongo(app)

@app.route("/")
def index():
    print("Welcome to Mars Data")
    mars = mongo.db.mars.find_one()
    return render_template("index.html", data=mars)


@app.route("/scrape")
def scrape():
    mars=mongo.db.mars
    mars_data = scrape_mars.scrape()
    mars.update({}, mars_data, upsert=True)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
