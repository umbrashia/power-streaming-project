from flask import Flask, render_template, request, Response
import system
import controllers

app = Flask(__name__, template_folder="templates/")


@app.route('/engine/<module>/<subModule>/')
@app.route('/engine/<module>/<subModule>/<parm1>/')
@app.route('/engine/<module>/<subModule>/<parm1>/<parm2>/')
def engine(module, subModule, parm1=None, parm2=None):
    system.FlaskServerBinder.setData(module=module,subModule=subModule)
    if module == "streaming":
        return controllers.StreamingController().internalRouting()
    return Response(response=None,status=404)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/streamingVideoSender")
def streamingVideoSender():
    return render_template("streamingVideoSender.html")


if __name__ == '__main__':
    app.run()
