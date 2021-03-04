from flask import Flask, render_template, request, jsonify
from random import random
import sys

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/random_number')
def random_number():
    return str(random())


chats = []


@app.route('/get_chats')
def get_chats():
    return jsonify(chats)


@app.route('/send_chat', methods=['POST'])
def send_chat():
    data = request.json
    chats.append(data['message'])
    print(data['message'])
    sys.stdout.flush()
    return jsonify({})


