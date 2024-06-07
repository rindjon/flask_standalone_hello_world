from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def say_hi():
    return f"Hello ,Class!\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
