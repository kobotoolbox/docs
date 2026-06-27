(function () {
  window.addEventListener("DOMContentLoaded", function () {
    let captions = document.querySelectorAll(".custom-section-page .page__body > p.caption");

    // HACK FIX WTF: previously we were targeting p.caption, but for some reason
    // on production build the caption class name is not added. We add it.
    if (captions.length === 0) {
      captions = document.querySelectorAll(".custom-section-page .page__body > p");
      captions.forEach((target) => {
        target.classList.add('caption');
      });
    }

    if (captions.length !== 0) {
      for (let i = 0; i < captions.length; i++) {
        let child = captions[i];
        const textEl = child.querySelector(".caption-text");
        if (textEl && textEl.innerText === window.docs.currentTitle) {
          child.setAttribute("id", `${window.docs.currentPagename}-section-caption`);
        }
      }
      console.info("Custom section page ready.");
    }
  });
})();
