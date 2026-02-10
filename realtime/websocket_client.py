import websocket
import json

def start_socket(on_message_function):
    socket_url = "wss://fstream.binance.com/ws/btcusdt@depth"

    def on_message(ws, message):
        data = json.loads(message)
        on_message_function(data)

    ws = websocket.WebSocketApp(socket_url, on_message=on_message)
    ws.run_forever()
