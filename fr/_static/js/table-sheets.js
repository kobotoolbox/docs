(function () {
  const SHEET_TYPES = ['survey', 'choices', 'settings'];

  function addSheetsToTables() {
    console.info('Configuring table sheets…');

    // We are looking for a table row with first cell containing single word
    // (one of SHEET_TYPES) and rest of cells being empty.
    const trs = document.querySelectorAll('tbody tr');

    for (let i = 0; i < trs.length; i++) {
      const tds = trs[i].querySelectorAll('td');
      const sheetName = tds[0].textContent;

      let areOtherCellsEmpty = true;
      for (let j = 1; j < tds.length; j++) {
        if (tds[j].textContent !== '') {
          areOtherCellsEmpty = false;
        }
      }

      if (SHEET_TYPES.includes(sheetName) && areOtherCellsEmpty) {
        trs[i].classList.add('table-sheets');
        tds[0].classList.add('table-sheets__container');
        tds[0].textContent = '';
        tds[0].setAttribute('colspan', '99');

        for (let k = 0; k < SHEET_TYPES.length; k++){
          const sheetType = SHEET_TYPES[k];
          const span = document.createElement('span');
          span.classList.add('table-sheets__sheet');
          span.appendChild(document.createTextNode(sheetType));
          if (sheetName === sheetType){
            span.classList.add('table-sheets__sheet--active');
          }
          tds[0].appendChild(span);
        }

        // Remove all other cells.
        for (let l = 1; l < tds.length; l++) {
          if (tds[l]) {
            tds[l].remove();
          }
        }
      }
    }
  }

  window.addEventListener('DOMContentLoaded', function () {
    addSheetsToTables();
  });
})();
