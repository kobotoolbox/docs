(function () {
  const listId = "breadcrumbslist";
  let breadcrumbsCount = 0;

  // Resolve a section by its position in the sidebar rather than by caption
  // text: the captions appear in the same order as window.docs.sectionOrder
  // (both come from the toctree order in index.rst), and the section names are
  // language-independent while the caption text is translated.
  function findSectionByIndex(captionIndex) {
    const order = (window.docs && window.docs.sectionOrder) || [];
    const name = order[captionIndex];
    if (name && window.docs.sectionsData) {
      return window.docs.sectionsData[name] || null;
    }
    return null;
  }

  function addBreadcrumb(title, captionIndex) {
    const listEl = document.getElementById(listId);
    const crumb = window.document.createElement("li");
    crumb.classList.add("breadcrumb");

    const section = findSectionByIndex(captionIndex);

    if (section) {
      const anchor = window.document.createElement("a");
      anchor.href = window.docs.rootUrl + `${section.name}.html`;
      anchor.insertAdjacentText("beforeend", title);
      crumb.appendChild(anchor);
    } else {
      crumb.insertAdjacentText("beforeend", title);
    }
    listEl.appendChild(crumb);
    breadcrumbsCount++;
  }

  window.addEventListener("DOMContentLoaded", function () {
    const tocs = document.querySelector(".sidebar_tocs");
    if (tocs && tocs.children.length !== 0) {
      // The sidebar is a flat, strictly alternating list of caption (<p>) then
      // list (<ul>) elements, one pair per section, in sectionOrder order. We
      // count captions so the "current" list maps back to its section's index.
      // (We count <p> by tag rather than the "caption" class: breadcrumbs.js
      // runs before sidebar_toc.js, which is what adds that class on builds
      // where Sphinx omits it.)
      let captionIndex = -1;
      for (let i = 0; i < tocs.children.length; i++) {
        let child = tocs.children[i];
        if (child.tagName === "P") {
          captionIndex++;
        }
        if (child.classList.contains("current")) {
          // The caption sits immediately before this "current" list, so its
          // section index is the current captionIndex.
          addBreadcrumb(tocs.children[i-1].innerText, captionIndex);
        }
      }
      const listEl = document.getElementById(listId);
      listEl.classList.add("activated");
      console.info("Breadcrumbs ready.", breadcrumbsCount);
    }
  });
})();
