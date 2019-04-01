import asyncio
import websockets
import json


async def hello(websocket, path):
    while True:
        temp = await websocket.recv()
        myJson=json.dumps(temp)
        # print(f"< {name}")
        bn=[]
        for kk in myJson['data']:
            bn.append(float(kk))
        # bn=list(map(float,myJson['data']))
        bi=bytearray(bn)
        f = open('static/temp.wav', 'ab')
        f.write(bi)
        f.close()
        greeting = f"Hello {myJson['itration']}!"

        await websocket.send(greeting)
        print(f"> {greeting}")

start_server = websockets.serve(hello, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()