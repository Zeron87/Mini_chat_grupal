import { getMessages, sendMessage, deleteMessage } from './chat.js';

const chat = document.querySelector('.chat_messages');
const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]');

async function init(){
    const textElement = document.querySelector('.message_text');
    const button = document.querySelector('.send-text');
    const messages = await getMessages();
    messages.forEach(message => {
        addMessageChat(message.text, message.user.username, message.user.id, message.id);
    });
    button.addEventListener('click', async function(event){
        event.preventDefault();
        const result = await sendMessage(textElement.value, sessionStorage.getItem('user_id'), csrfToken.value);
        if (result){
            addMessageChat(result.text, sessionStorage.getItem('username'), sessionStorage.getItem('user_id'), '1', true);
            textElement.value='';
            console.log(result);
        }
    });  
}

function addMessageChat (text, username, userId, messageId, scroll=false){
    const messageElement = document.createElement('li'); 
    const messageContainer = document.createElement('div');
    
    messageElement.textContent = `${username}: ${text}`;
    messageContainer.appendChild(messageElement);
    if(userId == sessionStorage.getItem('user_id')){
        const deleteButton = document.createElement('button');
        deleteButton.textContent='X';
        messageContainer.appendChild(deleteButton);
        deleteButton.addEventListener('click', () =>{
            const messageDeleted = deleteMessage(messageId, csrfToken.value);
            if (messageDeleted){
                messageContainer.remove();
            }
        });
    }
    chat.appendChild(messageContainer);
    if(scroll){
        messageElement.scrollIntoView();
    }
}
init();
