(function () {
  function findSection(tocEl) {
    let foundSection = null;
    if (window.docs && window.docs.sectionsData && tocEl) {
      Object.keys(window.docs.sectionsData).forEach((key) => {
        const item = window.docs.sectionsData[key];
        if (
          tocEl.getAttribute("id") !== null &&
          `home-page-toc-${item.name}` === tocEl.getAttribute("id")
        ) {
          foundSection = item;
        }
      });
    }
    return foundSection;
  }

  function setupToc(tocEl) {
    const section = findSection(tocEl);

    if (section && window.docs && window.docs.rootUrl) {
      // add show all button
      const showAll = window.document.createElement("a");
      showAll.classList.add("show-all-button");
      showAll.insertAdjacentText("beforeend", "See all");
      showAll.href = window.docs.rootUrl + `${section.name}.html`;
      tocEl.appendChild(showAll);
    } else {
      console.warn("section not found", tocEl)
    }
  }

  window.addEventListener("load", function () {
    const tocs = document.querySelectorAll(".toctree-wrapper[id^='home-page-toc-']");
    if (tocs.length !== 0) {
      tocs.forEach(setupToc)
      console.info("home page TOCs ready");
    }
  });
})();
