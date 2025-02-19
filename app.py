from web_socket_server import WebSocketServer, socketio, app
from flask import render_template

app = WebSocketServer().create_app()
# Task 1: Refactor the messages list to use a Hashmap called message_storage where the key is the author and the value is a list of messages.
message_storage = {}

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('message')
# Task 2: Modify the handle_message function to store messages in the message_storage Hashmap.
# Task 3: Update the socketio.on('message') event handler to retrieve messages from the message_storage HashMap.
def handle_message(message):
    print(f'Received message: {message}')
    message_storage['John Doe'] = message
    socketio.emit('message', message)

@socketio.on('get_user_messages')
# Task 5: Update socket get_all_messages to get all messages sending by a specific user.
def handle_get_user_messages(data):
    socketio.emit('get_user_messages', message_storage['John Doe'])

@app.route('/')
def index():
    return render_template('WebSocketClient.html')

if __name__ == '__main__':
    socketio.run(app)