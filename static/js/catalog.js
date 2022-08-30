// Фильтрация курсов
filterSelection("all")

function filterSelection(c) {
    var x, i;
    x = document.getElementsByClassName("filterItem");
    if (c == "all") c = "";
    for (i = 0; i < x.length; i++) {
        removeClass(x[i], "show");
        if (x[i].className.indexOf(c) > -1) addClass(x[i], "show");
    }
}

function addClass(element, name) {
    var i, arr1, arr2;
    arr1 = element.className.split(" ");
    arr2 = name.split(" ");
    for (i = 0; i < arr2.length; i++) {
        if (arr1.indexOf(arr2[i]) == -1) {
            element.className += " " + arr2[i];
        }
    }
}

function removeClass(element, name) {
    var i, arr1, arr2;
    arr1 = element.className.split(" ");
    arr2 = name.split(" ");
    for (i = 0; i < arr2.length; i++) {
        while (arr1.indexOf(arr2[i]) > -1) {
            arr1.splice(arr1.indexOf(arr2[i]), 1);
        }
    }
    element.className = arr1.join(" ");
}

// Добавит активный класс к текущей кнопке
var btnContainer = document.getElementById("catalogBtn");
var btns = btnContainer.getElementsByClassName("btn");
for (var i = 0; i < btns.length; i++) {
    btns[i].addEventListener("click", function() {
        var current = document.getElementsByClassName("active");
        current[0].className = current[0].className.replace(" active", "");
        this.className += " active";
    });
}


// кнопка добавить в избранное

for (var like_btn of document.getElementsByTagName('svg')) {

    like_btn.onclick = function() {

        this.style.fill = this.style.fill === 'red' ? 'none' : 'red';
        this.style.stroke = this.style.stroke === 'red' ? 'black' : 'red';
    }
}




// кнопка показать еще курсы
window.onload = function() {
    var box = document.getElementsByClassName('filterItem');
    var btn_load_more = document.getElementById('load_more');
    for (let i = 8; i < box.length; i++) {
        box[i].style.display = "none";
    }

    var countD = 8;
    btn_load_more.addEventListener("click", function() {
        countD += 8;
        if (countD <= box.length) {
            for (let i = 0; i < countD; i++) {
                box[i].style.display = "block";
            }
        }

        if (countD >= box.length) {
            btn_load_more.style.display = "none";
        }

    })
}