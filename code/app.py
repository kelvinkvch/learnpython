from flask import Flask

app = Flask(__name__, static_folder=".", static_url_path="/code")


@app.route("/")
def home():
    return app.send_static_file("index.html")


@app.route("/echo/<thing>")
def echo(thing):
    return f"Say hello to my little friend: {thing}!"


app.run(port=8080, debug=True)
