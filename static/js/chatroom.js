const user_username = JSON.parse(document.getElementById('user_username').textContent);
  const roomName = JSON.parse(document.getElementById('room-name').textContent);
  const chatLog = document.querySelector('#chat-log')


  //Auto srcolling down in a div.
  const theElement = document.getElementById('chat-log');
  const scrollToBottom = (node) => {
	  node.scrollTop = node.scrollHeight;
  }

  //Empty String will show when there is no message
  if (chatLog.childNodes.length <= 1) {

    const emptyText = document.createElement('h3')
    emptyText.id = 'emptyText'
    emptyText.innerText = 'No message'
    emptyText.className = 'emptyText'
    chatLog.appendChild(emptyText)
  }

  const chatSocket = new WebSocket(
    'ws://' +
    window.location.host +
    '/ws/chat/box/' +
    roomName +
    '/'
  );

  chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    const messageElement = document.createElement('p')

    const userId = data['user_id']
    const loggedInUserId = JSON.parse(document.getElementById('user_id').textContent)


    if (userId === loggedInUserId) {
      messageElement.innerText = data.message
      messageElement.classList.add('message', 'sender')
    } else {
      messageElement.innerHTML = `<span style="color:black;">${data.username}:</span> ${data.message}`
      messageElement.classList.add('message', 'receiver')
    }

    chatLog.appendChild(messageElement)
    scrollToBottom(theElement);

    if (document.querySelector('#emptyText')) {
      document.querySelector('#emptyText').remove()
    }
  }
  chatSocket.onclose = function (e) {
    console.error('Chat socket closed unexpectedly');
  };

  document.querySelector('#chat-message-input').focus();
  document.querySelector('#chat-message-input').onkeyup = function (e) {
    if (e.keyCode === 13) {  // enter, return
      document.querySelector('#chat-message-submit').click();
    }
  };

  document.querySelector('#chat-message-submit').onclick = function (e) {
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
      'message': message,
      'username': user_username,
    }));
    messageInputDom.value = '';
    scrollToBottom(theElement);
    
  };