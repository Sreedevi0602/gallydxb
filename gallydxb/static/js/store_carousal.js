

  document.addEventListener("DOMContentLoaded", function () {
    const carousel = document.querySelector("#storeCarousel");
    const items = carousel.querySelectorAll(".carousel-item");
    let currentIndex = 0;
    const interval = 5000; // 5 seconds

    function showSlide(index) {
      items.forEach((item, i) => {
        item.classList.toggle("active", i === index);
        const video = item.querySelector("video");
        if (video) {
          video.currentTime = 0;
          video.play();
        }
      });
    }

    setInterval(() => {
      currentIndex = (currentIndex + 1) % items.length;
      showSlide(currentIndex);
    }, interval);
  });
