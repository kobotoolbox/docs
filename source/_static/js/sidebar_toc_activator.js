(function () {
  const listCurrentClass = "current";
  const captionCurrentClass = "caption--current";
  const captionClass = "caption";
  const captionOpenedClass = "caption--opened";
  const captionClosedClass = "caption--closed";

  function closeToc(captionEl, listEl) {
    captionEl.classList.remove(captionOpenedClass);
    captionEl.classList.add(captionClosedClass);
    hide(listEl);
    return false;
  }

  function openToc(captionEl, listEl) {
    captionEl.classList.remove(captionClosedClass);
    captionEl.classList.add(captionOpenedClass);
    show(listEl);
    return true;
  }

  function activateSidebarToc(captionEl, listEl) {
    const isCurrent = listEl.classList.contains(listCurrentClass);
    if (isCurrent) {
      captionEl.classList.add(captionOpenedClass);
      captionEl.classList.add(captionCurrentClass);
    } else {
      let isOpened = closeToc(captionEl, listEl);
      captionEl.addEventListener("click", function () {
        // toggle toc
        if (isOpened) {
          isOpened = closeToc(captionEl, listEl);
        } else {
          isOpened = openToc(captionEl, listEl);
        }
      });
    }
  }

  window.addEventListener("load", function () {
    const tocs = document.querySelector(".sidebar_tocs");
    if (tocs && tocs.children.length !== 0) {
      for (let i = 0; i < tocs.children.length; i++) {
        let child = tocs.children[i];
        if (child.classList.contains(captionClass)) {
          activateSidebarToc(child, tocs.children[i+1])
        }
      }
      console.info("Sidebar TOCs activated.");
    }
  });
})();
