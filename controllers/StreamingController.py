import flask
import system
import kafka


class StreamingController(system.FlaskServerBinder):

    def internalRouting(self):
        if self.subModule == "hello":
            return self.postStream()
        if self.subModule == "streamingView":
            return self.streamingView()
        if self.subModule == "kafkaProCall":
            return self.kafkaProCall()
        if self.subModule == "kafkaRecCall":
            return self.kafkaRecCall()
        return flask.Response(response=None, status=404)

    def postStream(self):
        return "done again : "

    def kafkaProCall(self):
        
        proCall=kafka.KafkaProducer()
        proCall.send(topic="radha",value=b"krishan")
        proCall.flush()
        return "please check...."

    def kafkaRecCall(self): 
        def generate():
            consumer = kafka.KafkaConsumer("viom")
            for valu in consumer:
                f = open("video.mp4", "wb")
                f.write(valu.value)
                
                f.close()
                exit()
        return flask.Response(generate(), mimetype='video/mp4')
        

    def streamingView(self):
        # local var for use.
        try:
            print("hello")
        except Exception as ex:
            print(ex.__str__())
        finally:
            return flask.render_template("streamingVideoSender.html")
