from flask import Flask,jsonify,request

import csv

all_articles = []

with open('articles.csv') as f:
    csv_reader = csv.reader(f)

    data = list(csv_reader)

    all_articles = data[1:]

print("LENGTH:",len(all_articles))

liked_articles = []
not_liked_articles = []


app = Flask(__name__)

@app.route("/get-article",methods=["GET"])
def get_article():
    return jsonify({
        "data":all_articles[0],
        "status":"success, articles retreived"
    }),200

@app.route("/liked-article",methods=["POST"])
def liked_article():
    liked_articles.append(all_articles[0])
    all_articles.pop(0)
    return jsonify({
        "status":"article liked!"
    }),200


@app.route("/not-liked-article",methods=["POST"])
def not_liked_article():
    not_liked_articles.append(all_articles[0])
    all_articles.pop(0)
    return jsonify({
        "status":"article unliked!"
    }),200


if __name__ == "__main__":
    app.run()