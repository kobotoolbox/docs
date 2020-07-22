(function () {
  window.addEventListener("load", function () {
    const captions = document.querySelectorAll(".custom-section-page .page__body > p.caption");

    if (captions.length !== 0) {
      for (let i = 0; i < captions.length; i++) {
        let child = captions[i];
        const textEl = child.querySelector(".caption-text");
        if (textEl && textEl.innerText === window.docs.currentTitle) {
          child.setAttribute("id", `${window.docs.currentPagename}-section-caption`);
        }
      }
      console.info("custom section page ready");
    }
  });
})();
