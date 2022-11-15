const chatSocket = new WebSocket(
  'ws://'
  + window.location.host
  + '/ws/chat/'
);

chatSocket.onmessage = function(e) {
  const data = JSON.parse(e.data);
  const chatLog = document.querySelector('#chat-log')
  chatLog.value += (data.message + '\n');
  chatLog.scrollTop = chatLog.scrollHeight;
};

chatSocket.onclose = function(e) {
  console.error('Chat socket closed unexpectedly');
};

document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').onclick = function(e) {
  const messageInputDom = document.querySelector('#chat-message-input');
  const message = messageInputDom.value;
  chatSocket.send(JSON.stringify({
      'message': message
  }));
  messageInputDom.value = '';
};
