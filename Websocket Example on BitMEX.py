import json
import websocket

ws = websocket.create_connection("wss://www.bitmex.com/realtime")

#send a request
ws.send(json.dumps({"op": "subscribe", "args": ["orderBookL2_25:XBTUSD"]}))
# receive a request and print them (or more specific: the next 5 ones)
for i in range(5):
    result = ws.recv()
    print(result)
ws.close()
