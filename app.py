from flask import Flask 

app=Flask(__name__)

@app.route('/', methods=["POST","GET"])
def main():
    return "welcome to  world of datascience and machine learning project"


if __name__ =="__main__":
    app.run(debug=True)