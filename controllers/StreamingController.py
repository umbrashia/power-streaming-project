import flask,system

class StreamingController(system.FlaskServerBinder):
    
    def internalRouting(self):
        if self.subModule=="hello":
            return self.postStream()
        if self.subModule=="streamingView":
            return self.streamingView()
        return flask.Response(response=None,status=404)
    
    def postStream(self):
        return "done again : "

    def streamingView(self):
        return flask.render_template("streamingVideoSender.html")