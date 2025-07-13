window.addEventListener("scroll", function () {
        const header = document.querySelector(".header");
        if (window.scrollY > 100) {
            header.classList.add("header-scrolled");
        } else {
            header.classList.remove("header-scrolled");
        }
    });


  window.addEventListener("scroll", function () {
    if (window.scrollY > 100) {
      header.classList.add("header-scrolled");
    } else {
      header.classList.remove("header-scrolled");
    }
  });

  burger.addEventListener('click', () => {
    if (header.classList.contains('header-scrolled')) {
      menu.classList.add('menu-scrolled');
    } else {
      menu.classList.remove('menu-scrolled');
    }

    menu.classList.add('active');
    document.body.classList.add('menu-open');
  });