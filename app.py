from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Hello!"

@app.route("/test")
def test():
    return "test hello!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
