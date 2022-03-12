document.querySelector('#room-name-input').focus();
document.querySelector('#room-name-input').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#room-name-submit').click();
    }
};

document.querySelector('#room-name-submit').onclick = function(e) {
    var roomName = document.querySelector('#room-name-input').value;
    if(roomName === ''){
        document.getElementById('alert-msg').innerHTML = "<p>Please enter a group name!</p>";
        
    }else{
        
        window.location.pathname = '/chat/box/' + roomName + '/';
    }
    
};