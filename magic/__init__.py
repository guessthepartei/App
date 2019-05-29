from flask import Flask
import go
import predict
app = Flask(__name__)

@app.route("/main")
def main():
    return go.go()


if __name__ == "__main__":
    app.run()
