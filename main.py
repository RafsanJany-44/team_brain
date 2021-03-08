from flask import Flask, request
from test import check_sent

app = Flask(__name__)


@app.route('/<string:name>')
def getResponse(name:str):

    ret=check_sent(name)

    return "The sentence is "+ret



if __name__=="__main__":
    app.run()


