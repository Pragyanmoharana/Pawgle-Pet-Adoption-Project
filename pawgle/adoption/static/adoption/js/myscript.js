 var swiper = new Swiper(".mySwiper", {
    loop: true,
    grabCursor: true,
    spaceBetween: 30,
    autoplay: {
      delay: 5000,
    },
    slidesPerView: 1,
    breakpoints: {
      768: { slidesPerView: 2 },
      1024: { slidesPerView: 3 },
    },
  });




   window.onload = () => {
    document.querySelector("form").reset();
  };