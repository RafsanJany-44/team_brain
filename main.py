from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def getResponse():
    return "is hi thare hello"



if __name__=="__main__":
    app.run()

#lets make contribution
