from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def getResponse():
    if request.method == 'POST':
        text = request.form['text']
        user = request.form['user']
        if user == '':
            user = "unknown"
        # todo some magic
        response = text # function call

        if response == 'command':
            print("call micro")

            # todo API call user and text

            return "hi  " + user + " : "
        elif response == "quary":
            print("call another mocro")

            # todo API call user and text

            # API type = POST
            # from body(query,username)

            return "hi  " + user + " : "
        else:
            return "My apology, I don't understand!"
    elif request.method == 'GET':

        return "Hi"


@app.route('/getRec', methods=['GET'])
def getRecommandation():
    return "some recommadation"

#lets make contribution
