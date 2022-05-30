
import albumentations as A
import torch

from fastai.vision.all import *
from flask import Flask, jsonify, request
from PIL import Image

app=Flask(__name__)
learn = load_learner('trained_model-4.pkl')

@app.route("/", methods=["GET"])
def get_example():
    """GET in server"""
    response = jsonify(message="Simple server is running")
    return response

@app.route("/", methods=["POST"])
def post_example():
    """POST in server"""
    return jsonify(message="POST request returned")

if __name__ == "__main__":
    app.run(
       # host="0.0.0.0", port="5000", 
        debug=True)