const links = document.querySelectorAll(".link");
const prevButton = document.querySelector(".pag-button1");
const nextButton = document.querySelector(".pag-button2");

let currentValue = 1;

function setActiveLink() {
  for (let link of links) {
    link.classList.remove("active");
  }
  links[currentValue - 1].classList.add("active");
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
  currentValue = parseInt(event.target.textContent);
  setActiveLink();
}

prevButton.addEventListener("click", handlePrevClick);
nextButton.addEventListener("click", handleNextClick);
links.forEach((link) => {
  link.addEventListener("click", handleLinkClick);
});

// Встановлюємо активний клас для першого елементу по замовчуванню
setActiveLink();
