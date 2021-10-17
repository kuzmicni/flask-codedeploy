from flask import Flask

app = Flask(__name__)
@app.route("/")
def home():
    return 'hello from root'

@app.route("/hi")
def greet():
    return 'hello amigo!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)