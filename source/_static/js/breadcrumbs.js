(function () {
  const listId = "breadcrumbslist";

  function addBreadcrumb(title, url) {
    const listEl = document.getElementById(listId);
    const crumb = window.document.createElement("li");
    crumb.classList.add("breadcrumb");
    if (url) {
      const anchor = window.document.createElement("a");
      anchor.href = url;
      anchor.insertAdjacentText("beforeend", title);
      crumb.appendChild(anchor);
    } else {
      crumb.insertAdjacentText("beforeend", title);
    }
    listEl.appendChild(crumb);
  }

  function buildBreadcrumbs(parentTitle, pageTitle, pageUrl) {
    addBreadcrumb(parentTitle);
    addBreadcrumb(pageTitle, pageUrl);
  }

  window.addEventListener("load", function () {
    const tocs = document.querySelector(".sidebar_tocs");
    if (tocs.children.length !== 0) {
      for (let i = 0; i < tocs.children.length; i++) {
        let child = tocs.children[i];
        if (child.classList.contains("current")) {
          buildBreadcrumbs(tocs.children[i-1].innerText, window.docs.currentTitle, window.docs.currentUrl);
        }
      }
      const listEl = document.getElementById(listId);
      listEl.classList.add("activated");
      console.info("Breadcrumbs created.");
    }
  });
})();