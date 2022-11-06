from flask import Flask, request
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello"


def send_msg(msg):
    PHONE_ID = "110829038490956"
    TOKEN = "EAAJVc3j40G8BAK9Ez4mltrVf5W6FcPTiSKPplkg40NhoZC7NJO3lJHqyBjEPava9hGN4Ya98Bpbx5hGTP9b0ZCa92nXZAQKQluLZA2lb4r4VLhqQ6sSPYOsFgEu4f8i9yBM89nFEFdj6AofAbAZBdingHhGwrS32tpZBtxuYvAZBPyutF5CkTeD0KeSjbzcZAnKImQQfFsF6bwZDZD"
    NUMBER = "923462901820"
    MESSAGE = "<message>"
    headers = {
        "Authorization": "Bearer "+TOKEN,
    }
    json_data = {
        'messaging_product': 'whatsapp',
        "to": NUMBER,
        'type': 'text',
        "text": {
            "body": msg
        }
    }
    response = requests.post( "https://graph.facebook.com/v13.0/"+PHONE_ID+"/messages", headers=headers,
                             json=json_data)
    print(response.text)


@app.route('/receive_msg', methods=['POST', 'GET'])
def webhook():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "umer":
            return "Verification token missmatch", 403
        return request.args['hub.challenge'], 200
    return "Hello world", 200
    print(request)
    res = request.get_json()
    print(res)
    try:
        if res['entry'][0]['changes'][0]['value']['messages'][0]['id']:
            send_msg("Thank you for the response.")
    except:
        pass
    return '200 OK HTTPS.'


if __name__ == "__main__":
    app.run(debug=True)