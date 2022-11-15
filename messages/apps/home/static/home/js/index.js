const chatSocket = new WebSocket(
  'ws://'
  + window.location.host
  + '/ws/chat/'
);

chatSocket.onmessage = function(e) {
  const data = JSON.parse(e.data);
  const chatLog = document.querySelector('#chat-log');

  var containerToAdd;

  if(data.info) {
    containerToAdd = createInfoMessageContainer(data.info)
  } else {
    containerToAdd = createMessageContainer(data.message_sender, data.message)
  }

  chatLog.appendChild(containerToAdd);
  chatLog.scrollTop = chatLog.scrollHeight;
};

function createInfoMessageContainer(info) {
  infoContainer = document.createElement('p');
  infoContainer.innerText = info;
  infoContainer.classList.add('info-message');

  return infoContainer;
}

function createMessageContainer(messageSender, message) {
  // Create a message container
  const messageContainer = document.createElement('div');
  messageContainer.classList.add('message-container');

  // Add the sender of the message
  messageSenderContainer = document.createElement('p');
  messageSenderContainer.innerText = messageSender + ": ";
  messageSenderContainer.classList.add('message-sender');
  messageContainer.appendChild(messageSenderContainer);

  // Add the content of the message
  messageContentContainer = document.createElement('p');
  messageContentContainer.classList.add('message-content');
  messageContentContainer.innerText = message;
  messageContainer.appendChild(messageContentContainer);

  return messageContainer;
}

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
