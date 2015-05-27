from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_question():
    return jsonify({'question': get_random_question()})

@app.route('/', methods=['POST'])
def save_answer(answer):
    print answer


def get_random_question():
    import random
    l = ["Are you a female?", "Are you ZORO?",
         "Do you live in Haifa?", "Is your name Tal?",
         "Do you breath?", "Are you a homosapien?"]
    return random.choice(l)

if __name__ == '__main__':
    app.run(port=12345, debug=True)