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
      // The body renders one toctree caption per section, in the same order as
      // sectionOrder (both come from the toctree order in index.rst). We reveal
      // the section matching the current page by its position rather than by
      // caption text, so it works in every language — the caption text is
      // translated, but currentPagename is not.
      const sectionNames = window.docs.sectionOrder || [];
      const sectionIndex = sectionNames.indexOf(window.docs.currentPagename);
      const target = sectionIndex !== -1 ? captions[sectionIndex] : undefined;
      if (target) {
        target.setAttribute("id", `${window.docs.currentPagename}-section-caption`);
      }
      console.info("Custom section page ready.");
    }
  });
})();
