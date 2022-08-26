
from flask import Flask
from housing.exception import HousingException
from housing.logger import logging
import sys

app=Flask(__name__)

@app.route('/', methods=["POST","GET"])
def main():
    try:
        raise Exception("we are testing exception modulue")
    except Exception as e:
        housing=HousingException(e,sys)
        logging.info(housing.error_message)
        logging.info("we are testing logger")
        logging.info("testing method log")
    return "welcome to  world of datascience and machine learning project"


if __name__ =="__main__":
    app.run(debug=True)