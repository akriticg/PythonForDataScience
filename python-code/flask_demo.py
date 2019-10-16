from flask import Flask
from flask import jsonify
from datetime import datetime
import re
from Pipeline_mine import *
import sys
from XmlToJson import xmlToJson
import numpy as np
import pandas as pd
import string
import re
from Train import *

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/predict/<recordToTest>")
def predict(recordToTest):
    df = GetJsonFromRecords(recordToTest)
    df1 = df.copy()
    df1 = df1.T
    df1 = df1.reset_index()
    # giving columns names
    df1.columns = ['id','description']
    df1["descrp"] = df1["description"].apply(TextProcess)
    prediction = Predict(df1)
    return 200

    # print output based on Prediction
    print("End")