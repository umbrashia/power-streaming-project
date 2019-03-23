from flask import Flask,render_template

app = Flask(__name__,template_folder="templates/")

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/streamingVideoSender")
def streamingVideoSender():
    return render_template("streamingVideoSender.html")

if __name__ == '__main__':
   app.run()