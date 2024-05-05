from g4f.client import Client
from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
client = Client()
@app.route('/gpt', methods=['GET'])
@cross_origin()
def uppercase():
    text = request.args.get('text', '')
    print(text)
    chat_completion = client.chat.completions.create(model="gpt-3.5-turbo",messages=[{"role": "user", "content":f"{text}"}])
    result=chat_completion.choices[0].message.content
    return result

if __name__ == '__main__':
    app.run(debug=True)