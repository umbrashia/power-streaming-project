import asyncio
import websockets
import json
import kafka


async def hello(websocket, path):
    proCall=kafka.KafkaProducer()
    
    while True:
        temp = await websocket.recv()
        myJson=json.loads(temp)
        # print(f"< {name}")
        proCall.send(topic="radha",value=myJson['binary'])
        proCall.flush()
        greeting = f"Hello {myJson['itration']}!"

        await websocket.send(greeting)
        # print(f"> {greeting}")


start_server = websockets.serve(hello, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
"""bn=[]
for kk in myJson['data'].split(","):
    bn.append(kk)
bi=bytearray(myJson['data'],encoding='utf8')
f = open('static/'+str(myJson['itration'])+'_temp.wav', 'wb')
f.write(bi)
f.close()"""