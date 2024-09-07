document.addEventListener("DOMContentLoaded", () => {
  const navLinks = document.querySelectorAll(".nav-link.main_nav");

  navLinks.forEach((link) => {
    link.addEventListener("click", function () {
      navLinks.forEach((navLink) => navLink.classList.remove("active"));
      this.classList.add("active");
    });
  });
});
