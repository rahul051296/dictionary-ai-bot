//python server.py -d models/dialogue -u models/nlu/default/wordsnlu -o out.log --cors *

let ul = document.getElementById('conversation');

function send(){
    let msg = document.getElementById('chat-input').value;
    let li = document.createElement('li');
    li.appendChild(document.createTextNode(msg));
    li.className = "sender"
    ul.appendChild(li);
    respond(msg);
    document.getElementById('chat-input').value = "";
    var element = document.getElementById("bottom");
    document.getElementById("chat-container").scrollTop = element.clientHeight + 100;
}
function respond(msg){
 let url = `http://localhost:5005/conversations/default/respond?q=${msg}`
fetch(url,{method:'GET'})
.then((response)=>{
  response.json()
  .then((response)=>{
    let li = document.createElement('li');
    li.appendChild(document.createTextNode(response));
    li.className = "responder"
    ul.appendChild(li);
   console.log(response); 
  });
});
}
var input = document.getElementById("chat-input");
input.addEventListener("keyup", function(event) {
    event.preventDefault();
    if (event.keyCode === 13) {
        document.getElementById("btn").click();
    }
});