(function () {
  function limitTocDisplay(tocEl) {
    const exceedingChildren = tocEl.querySelectorAll("li.toctree-l1:nth-child(n+6)");

    if (exceedingChildren.length > 0) {
      // hide all items over 5
      exceedingChildren.forEach(hide);

      // add show all button
      const showAll = window.document.createElement("div");
      showAll.classList.add("show-all-button");
      showAll.classList.add("link");
      showAll.insertAdjacentText("beforeend", "See all");
      showAll.addEventListener("click", function () {
        // on click show all previously hidden items and hide the button
        exceedingChildren.forEach(show);
        hide(showAll);
      });
      tocEl.appendChild(showAll);
    }
  }

  window.addEventListener("load", function () {
    const tocs = document.querySelectorAll(".toctree-wrapper[id^='home-page-toc-']");
    if (tocs.length !== 0) {
      tocs.forEach(limitTocDisplay)
      console.info("Home page TOCs activated.");
    }
  });
})();
