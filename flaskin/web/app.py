from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    """TODO: Docstring for index.
    :returns: TODO

    """
    return "Hello, from docker..."

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
