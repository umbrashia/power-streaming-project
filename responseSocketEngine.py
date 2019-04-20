import asyncio
import websockets
import json
import kafka
import base64


async def responseStream(websocket, path):
    temp = await websocket.recv()
    consumer = kafka.KafkaConsumer("viom")
    for valu in consumer:
        fi=base64.b64decode(valu.value)
        # yield fi
        # res=json.dumps({"data":fi})
        
        await websocket.send(str(valu.value))

       




start_server = websockets.serve(responseStream, 'localhost', 8766)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()