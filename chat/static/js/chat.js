export async function getMessages(){
    let response = await fetch('/api/messages/list/');

    if (response.ok) { 
        let json = await response.json();
        return json;
    } else {
        return null;
    }

}

export async function sendMessage(text, userId, token){
    const data = {
        method: 'POST', 
        headers: {'Content-Type': 'application/json', 'X-CSRFToken': token}, 
        body: JSON.stringify({
            "text": text,
            "user": userId
        })
    };
    let response = await fetch('/api/messages/create/', data);
    if (response.ok) {
        let json = await response.json();
        return json;
    } else {
        return null;
    }
}


export async function deleteMessage(messageId, token){
    const data = {
        method: 'DELETE', 
        headers: {'Content-Type': 'application/json', 'X-CSRFToken': token}, 
    };
    let response = await fetch(`/api/messages/delete/${messageId}`, data);
    if (response.ok) {
        return true;
    } else {
        return false;
    }
}