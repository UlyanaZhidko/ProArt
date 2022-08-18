'use strict';

/* Меню */
function burgerMenu(selector) {
    let menu = document.querySelector(selector);
    let button = document.querySelector('.burger-menu_button', '.burger-menu_lines');
    let links = document.querySelector('.burger-menu_link');
    let overlay = document.querySelector('.burger-menu_overlay');

    button.addEventListener('click', (e) => {
        e.preventDefault();
        toggleMenu();
    });

    links.addEventListener('click', () => toggleMenu());
    overlay.addEventListener('click', () => toggleMenu());

    function toggleMenu() {
        menu.classList.toggle('burger-menu_active');

        if (menu.classList.contains('burger-menu_active')) {
            document.body.style.overlow = "hidden";
        } else {
            document.body.style.overlow = "visible";
        }
    }
}

burgerMenu('.burger-menu');