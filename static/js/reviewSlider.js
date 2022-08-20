//Слайдер с отзывами


let slideIndex = 1;

showSlide(slideIndex);

/* Увеличичение индекса на 1 — следующий слайд */
function nextSlide() {
    showSlide(slideIndex += 1);
}

/* Уменьшение индекса на 1 — предыдущий слайд */
function previousSlide() {
    showSlide(slideIndex -= 1);
}

/* Текущий слайд */
function currentSlide(n) {
    showSlide(slideIndex = n)
}

/* Функция перелистывания: */
function showSlide(n) {
    let slides = document.getElementsByClassName("item");

    /* Проверяем количество слайдов: */
    if (n > slides.length) {
        slideIndex = 1;
    }
    if (n < 1) {
        slideIndex = slides.length
    }


    for (let slide of slides) {
        slide.style.display = "none";
    }

    slides[slideIndex - 1].style.display = "block";
}