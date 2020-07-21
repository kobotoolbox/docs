(function () {
  window.addEventListener("load", function () {
    const searchArr = document.getElementById("main-search-arrow");
    const page = document.getElementById("index");
    const mainHeader = document.getElementById("main-header");
    if (searchArr && page) {
      searchArr.addEventListener("click", function () {
        window.scrollTo({
          top: page.offsetTop - mainHeader.offsetHeight,
          behavior: "smooth",
        });
      });
      console.info("home page scroll arrow ready")
    }
  });
})();
