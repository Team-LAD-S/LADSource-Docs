(function () {
  const realmHashPattern = /^#(server|client)-/;

  function getRealmTabSet() {
    return Array.from(document.querySelectorAll(".tabbed-set")).find(function (tabSet) {
      return tabSet.querySelector('[id^="server-"], [id^="client-"]');
    });
  }

  function getRealmInputs(tabSet) {
    return Array.from(tabSet.querySelectorAll(":scope > input[type='radio']"));
  }

  function getInputRealm(tabSet, input) {
    const label = tabSet.querySelector(`.tabbed-labels > label[for="${input.id}"]`);
    return label ? label.textContent.trim().toLowerCase() : "";
  }

  function selectRealmFromHash(tabSet) {
    const match = window.location.hash.match(realmHashPattern);
    if (!match) {
      return;
    }

    const hashRealm = match[1];
    const input = getRealmInputs(tabSet).find(function (candidate) {
      return getInputRealm(tabSet, candidate) === hashRealm;
    });
    if (input) {
      input.checked = true;
    }
  }

  function updateRealmToc(tabSet) {
    const activeInput = getRealmInputs(tabSet).find(function (input) {
      return input.checked;
    });
    if (!activeInput) {
      return;
    }

    const activeRealm = getInputRealm(tabSet, activeInput);
    document
      .querySelectorAll(".md-nav--secondary a[href]")
      .forEach(function (link) {
        const match = new URL(link.href, window.location.href).hash.match(
          realmHashPattern
        );
        const item = link.closest(".md-nav__item");
        if (!match || !item) {
          return;
        }

        const hidden = match[1] !== activeRealm;
        item.hidden = hidden;
        if (hidden) {
          link.classList.remove("md-nav__link--active", "md-nav__link--passed");
        }
      });
  }

  function initializeRealmTabToc() {
    const tabSet = getRealmTabSet();
    if (!tabSet) {
      return;
    }

    selectRealmFromHash(tabSet);
    updateRealmToc(tabSet);

    if (tabSet.dataset.realmTocInitialized === "true") {
      return;
    }
    tabSet.dataset.realmTocInitialized = "true";

    getRealmInputs(tabSet).forEach(function (input) {
      input.addEventListener("change", function () {
        updateRealmToc(tabSet);
      });
    });
  }

  window.addEventListener("hashchange", initializeRealmTabToc);

  if (typeof document$ !== "undefined") {
    document$.subscribe(initializeRealmTabToc);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initializeRealmTabToc);
  } else {
    initializeRealmTabToc();
  }
})();
