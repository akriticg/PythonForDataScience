# Read xml file and product json for processing as dataframes

import sys
from XmlToJson import xmlToJson
import numpy as np
import pandas as pd
import string
import re
from Train import *


def ColTransform(df0):
    df = df0.copy()
    df = df.T

    df = df.reset_index()

    df.columns = ['id', 'description']
    return df


def Predict(df):
    # if want to return list of predictions
    predlist = []

    # loading the pickled files
    A_loaded_tfidf = joblib.load('1.LR-TFIDF.pkl')
    xtfidf = A_loaded_tfidf.transform(df.description)

    print(type(A_loaded_tfidf))

    A_loaded_model = joblib.load('1.LR.pkl.')
    predictions1 = []
    predictions1 = A_loaded_model.predict(xtfidf)

    if predictions1 == 1:
        print("The patient's Smoker status  is : Unknown")
        predlist.append("Unknown")
        # return predlist[-1]

    B_loaded_tfidf = joblib.load('2.GB-TFIDF.pkl')
    xtfidf = B_loaded_tfidf.transform(df.description)

    B_loaded_model = joblib.load('2.GB.pkl')
    predictions2 = []
    predictions2 = B_loaded_model.predict(xtfidf)

    if predictions2 == 1:
        print("The patient's Smoker status  is : Non-Smoker")
        predlist.append("Non-Smoker")
        # return predlist[-1]

    C_loaded_tfidf = joblib.load('3.GB-TFIDF.pkl')
    xtfidf = C_loaded_tfidf.transform(df.description)

    C_loaded_model = joblib.load('3.GB.pkl')
    predictions3 = []
    predictions3 = C_loaded_model.predict(xtfidf)
    if predictions3 == 1:
        print( "The patient's Smoker status  is : Past Smoker")
        predlist.append("Past Smoker")
        # return predlist[-1]
    else:
        print( "The patient's Smoker status  is : Smoker")
        predlist.append("Smoker")
        # return predlist[-1]

    # if want to return list of predictions
    print(predlist)
    return predlist[-1]

def main():
    # read test record from the command line
    recordToTest = "demo2.xml"
    # debug: recordToTest = "name.xml"

    # get the json from sample record as json
    df = GetJsonFromRecords(recordToTest)
    df1 = ColTransform(df)

    df1["description"] = df1["description"].apply(TextProcess)
    Predict(df1)

    # print output based on Prediction
    print("End")

# Run the main function
if __name__ == "__main__":

    main()
