(function () {
  const collator = new Intl.Collator(undefined, {
    numeric: true,
    sensitivity: "base",
  });

  function valueFor(row, column, type) {
    const value = row.cells[column].textContent.trim();
    return type === "number" ? Number(value) : value;
  }

  function sortTable(table, column, type, direction) {
    const rows = Array.from(table.tBodies[0].rows);
    const multiplier = direction === "ascending" ? 1 : -1;

    rows.sort(function (left, right) {
      const leftValue = valueFor(left, column, type);
      const rightValue = valueFor(right, column, type);
      let result;

      if (type === "number") {
        result = leftValue - rightValue;
      } else {
        result = collator.compare(leftValue, rightValue);
      }

      if (result === 0) {
        result = collator.compare(
          valueFor(left, 0, "text"),
          valueFor(right, 0, "text")
        );
      }
      return result * multiplier;
    });

    const fragment = document.createDocumentFragment();
    rows.forEach(function (row) {
      fragment.appendChild(row);
    });
    table.tBodies[0].appendChild(fragment);
  }

  function makeSortable(table, header, column, type, firstDirection) {
    const label = header.textContent.trim();
    const button = document.createElement("button");
    button.type = "button";
    button.className = "api-sort-button";
    button.textContent = label;
    button.title = `Sort by ${label}`;
    header.textContent = "";
    header.appendChild(button);

    button.addEventListener("click", function () {
      const isCurrent = table.dataset.sortColumn === String(column);
      const currentDirection = header.getAttribute("aria-sort");
      const direction = isCurrent
        ? currentDirection === "ascending"
          ? "descending"
          : "ascending"
        : firstDirection;

      Array.from(table.tHead.rows[0].cells).forEach(function (cell) {
        cell.removeAttribute("aria-sort");
      });
      header.setAttribute("aria-sort", direction);
      table.dataset.sortColumn = String(column);
      sortTable(table, column, type, direction);
    });
  }

  function initializeModuleTables() {
    document.querySelectorAll(".api-module-list table").forEach(function (table) {
      if (table.dataset.sortable === "true" || !table.tHead || !table.tBodies[0]) {
        return;
      }

      table.dataset.sortable = "true";
      const headers = table.tHead.rows[0].cells;
      makeSortable(table, headers[0], 0, "text", "ascending");
      makeSortable(table, headers[1], 1, "number", "descending");
      headers[0].setAttribute("aria-sort", "ascending");
      table.dataset.sortColumn = "0";
    });
  }

  if (typeof document$ !== "undefined") {
    document$.subscribe(initializeModuleTables);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initializeModuleTables);
  } else {
    initializeModuleTables();
  }
})();
