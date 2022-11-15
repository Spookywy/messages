const chatSocket = new WebSocket(
  'ws://'
  + window.location.host
  + '/ws/chat/'
);

chatSocket.onmessage = function(e) {
  const data = JSON.parse(e.data);
  const chatLog = document.querySelector('#chat-log');

  // Create a message container
  const messageContainer = document.createElement('div');
  messageContainer.classList.add('message-container');

  // Create and add the sender of the message to the container
  messageSender = document.createElement('p');
  messageSender.innerText = `${data.message_sender}: `;
  messageSender.classList.add('message-sender');
  messageContainer.appendChild(messageSender);

  // Create and add the content of the message to the container
  messageContent = document.createElement('p');
  messageContent.classList.add('message-content');
  messageContent.innerText = data.message;
  messageContainer.appendChild(messageContent);

  // Add the message container to the list of messages
  chatLog.appendChild(messageContainer);

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
