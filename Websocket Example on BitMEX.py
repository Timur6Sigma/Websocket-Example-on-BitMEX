import json
import websocket

ws = websocket.create_connection("wss://www.bitmex.com/realtime")

#First need to subscribe to instruments, then one can subscribe to a specific instrument like orderBookL2
#send a request
ws.send(json.dumps({"op": "subscribe", "args": ["orderBookL2_25:XBTUSD"]}))
for i in range(5):
    # receive a request and print them (or more specific: the next 5 ones)
    result = ws.recv()
    print(result)
ws.close()
