from flask import Flask, render_template, jsonify, request


import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('consolev2.html')

@app.route('/commands')
def commands():
    with open('commands.json', 'r') as f:
        commands = json.load(f)
    return jsonify(commands)

@app.route('/save-message', methods=['POST'])
def save_message():
    message = request.json.get('message')
    if message:
        with open('messages.json', 'a') as f:
            f.write(message + '\n')
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "error"}), 400


if __name__ == '__main__':
    app.run(debug=True)
