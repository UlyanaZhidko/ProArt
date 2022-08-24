//Модальное окно с кодом верификации из email
var modal = document.getElementById("otcModal");
var btn = document.getElementById("otcBtn_email");
var span = document.getElementsByClassName("close")[0];

btn.onclick = function() {
    modal.style.display = "block";
}

span.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

//Модальное окно с кодом верификации по номеру
var modal = document.getElementById("otcModal");
var btn = document.getElementById("otcBtn_phone");
var span = document.getElementsByClassName("close")[0];

btn.onclick = function() {
    modal.style.display = "block";
}

span.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}