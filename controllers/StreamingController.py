import flask,system

class StreamingController(system.FlaskServerBinder):
    
    def internalRouting(self):
        if self.subModule=="hello":
            return self.postStream()
        if self.subModule=="streamingView":
            return self.streamingView()
        return flask.Response(response=None,status=404)
    
    def postStream(self):
        t=5+10
        return "done again : "+str(t)
        
    def streamingView(self):
        return flask.render_template("streamingVideoSender.html")