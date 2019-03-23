import flask,system

class StreamingController(system.FlaskServerBinder):
    
    def internalRouting(self):
        if self.subModule=="hello":
            return self.postStream()
        return flask.Response(response=None,status=404)
    
    def postStream(self):
        return "done again"