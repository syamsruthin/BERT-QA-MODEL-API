from q_a_api import app
from flask import jsonify,Response
from q_a_api.models.q_a_model import q_a_model


@app.route("/",methods=["GET"])
def home_page():
    return app.send_static_file('ui.html')


@app.route("/status",methods=["GET"])
def status():
    return Response("Q_A model API started",200)

@app.route("/predict",methods=["POST"])
def predict():
    qa = q_a_model()
    resp = jsonify(qa.predict())
    resp.status_code = 200
    return resp
