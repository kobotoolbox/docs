(function () {
  const listId = "breadcrumbslist";
  let breadcrumbsCount = 0;

  function findSection(title) {
    let foundSection = null;
    if (window.docs && window.docs.sectionsData) {
      Object.keys(window.docs.sectionsData).forEach((key) => {
        const item = window.docs.sectionsData[key];
        if (title === item.title) {
          foundSection = item;
        }
      });
    }
    return foundSection;
  }

  function addBreadcrumb(title) {
    const listEl = document.getElementById(listId);
    const crumb = window.document.createElement("li");
    crumb.classList.add("breadcrumb");

    const section = findSection(title);

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
      for (let i = 0; i < tocs.children.length; i++) {
        let child = tocs.children[i];
        if (child.classList.contains("current")) {
          addBreadcrumb(tocs.children[i-1].innerText);
        }
      }
      const listEl = document.getElementById(listId);
      listEl.classList.add("activated");
      console.info("breadcrumbs ready", breadcrumbsCount);
    }
  });
})();
