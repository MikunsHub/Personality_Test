import flask
import sklearn
import pickle
from flask import Flask, render_template, request, redirect, url_for

#load the model
clustering_model = pickle.load(open("C:/Users/HP PC/Desktop/work/Personality_Test/Personality_ML/Personality_class.pkl", 'rb'))


app = Flask(__name__)
@app.route("/", methods = ["GET","POST"])
def main():
    if flask.request.method == "POST":

        user_response = flask.request.form["main"]

        Personality = clustering_model.predict(user_response)
        return flask.render_template("main.html",Personality ="You have a personality of Class {}".format(Personality_class) )





if __name__ == "__main__":
    app.run(debug=True)
