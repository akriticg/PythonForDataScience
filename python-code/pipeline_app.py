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
import connexion

# Instantiate our Flask app object
app = connexion.FlaskApp(__name__, port=8080, specification_dir='swagger/')
application = app.app

@app.route("/", methods=["GET","POST"])
def health():
    # Test to make sure our service is actually healthy
    return ("Message: Service is OK")

@app.route("/", methods=["GET","POST"])
def predict(recordToTest):
    df = pd.DataFrame()
    df = GetJsonFromRecords(recordToTest)
    df1 = pd.DataFrame()
    df1 = df.copy()
    df1 = df1.T
    df1 = df1.reset_index()
    #giving columns names
    df1.columns = ['id','description']
    df1["description"] = df1["description"].apply(TextProcess)
    prediction = Predict(df1)
    # return 200
    return jsonify({"prediction" : prediction})

    # print output based on Prediction
    print("End")

# Read the API definition for our service from the yaml file
app.add_api("pipeline_api.yaml")

# Start the app
if __name__ == "__main__":
    app.run()