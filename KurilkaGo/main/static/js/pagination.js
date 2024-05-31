'use strict';

const links = document.querySelectorAll(".link a");
const prevButton = document.querySelector(".pag-button1");
const nextButton = document.querySelector(".pag-button2");

let currentValue = 1;

function setActiveLink() {
  for (let link of links) {
    link.parentElement.classList.remove("active");
  }
  links[currentValue - 1].parentElement.classList.add("active");
  window.location.href = links[currentValue - 1].href; // Переходимо за посиланням
}

function handlePrevClick() {
  if (currentValue > 1) {
    currentValue--;
    setActiveLink();
  }
}

function handleNextClick() {
  if (currentValue < links.length) {
    currentValue++;
    setActiveLink();
  }
}

function handleLinkClick(event) {
  event.preventDefault(); // Зупиняє стандартну дію посилання
  currentValue = Array.from(links).indexOf(event.target) + 1;
  setActiveLink();
}

prevButton.addEventListener("click", handlePrevClick);
nextButton.addEventListener("click", handleNextClick);

links.forEach((link) => {
  link.addEventListener("click", handleLinkClick);
});

// Встановлюємо активний клас для першого елементу по замовчуванню
setActiveLink();
