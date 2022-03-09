// Loader
window.addEventListener("load", () =>{
  // preloader
  document.querySelector(".paceDiv").classList.add("fade-out");
  setTimeout(() =>{
    document.querySelector(".paceDiv").style.display="none";
  },600)
})

  
const check = document.querySelector('.toggler'),
hamburger = document.querySelector(".hamburger");

check.addEventListener('click', () => {
  hamburger.classList.toggle('active');
})


const btns = document.querySelectorAll(".nav-btn");
// const slides = document.querySelectorAll(".video-slide");
const contents = document.querySelectorAll(".content");

var sliderNav = function(manual){
  btns.forEach((btn) => {
    btn.classList.remove("active");
  });

  // slides.forEach((slide) => {
  //   slide.classList.remove("active");
  // });

  contents.forEach((content) => {
    content.classList.remove("active");
  });

  btns[manual].classList.add("active");
  // slides[manual].classList.add("active");
  contents[manual].classList.add("active");
}

btns.forEach((btn, i) => {
  btn.addEventListener("click", () => {
    sliderNav(i);
  });
});

/* ====== Slider ===== */
var slidePrev = document.getElementById("prev");
var slideNext = document.getElementById("next");
var thumbnail = document.getElementsByClassName("thumbnail");
var galleryImg = document.querySelector(".about .slider-container .gallery-img")

var backgroundImg = new Array(
  "img/SliderITCenter-1.jpg",
  "img/SliderITCenter-2.jpg",
  "img/SliderITCenter-3.jpg",
  "img/SliderITCenter-4.jpg",
  "img/SliderITCenter-5.jpg"
);


let i = 0;
slideNext.onclick = function(){
  if(i < 4){
    galleryImg.style.background = 'url("'+backgroundImg[i+1]+'") no-repeat center center / cover';
    thumbnail[i+1].classList.add("active");
    thumbnail[i].classList.remove("active");
    i++;
  }
}

slidePrev.onclick = function(){
  if(i > 0){
    galleryImg.style.background = 'url("'+backgroundImg[i-1]+'") no-repeat center center / cover';
    thumbnail[i-1].classList.add("active");
    thumbnail[i].classList.remove("active");
    i--;
  }
}