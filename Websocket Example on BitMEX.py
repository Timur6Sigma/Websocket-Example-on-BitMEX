import json
import websocket

ws = websocket.create_connection("wss://www.bitmex.com/realtime")

#First need to subscribe to instruments, then one can subscribe to a specific instrument like orderBookL2
#send a request
ws.send(json.dumps({"op": "subscribe", "args": ["instrument:XBTUSD"]}))
#receive a request
result = ws.recv()
print(result)
ws.send(json.dumps({"op": "subscribe", "args": ["orderBookL2_25:XBTUSD"]}))
for i in range(10):
    result = ws.recv()
    print(result)
ws.close()
