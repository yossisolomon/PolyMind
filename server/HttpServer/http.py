from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_question():
    return jsonify({'question': get_random_question()})

@app.route('/', methods=['POST'])
def save_answer(answer):
    print answer


def get_random_question():
    return "Are you a female?"

if __name__ == '__main__':
    app.run(port=12345, debug=True)