from flask import Flask, render_template, jsonify

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

if __name__ == '__main__':
    app.run(debug=True)
