(function () {
  const storageKey = "ladsource-primary-sidebar-scroll";
  const sidebarSelector =
    ".md-sidebar--primary .md-sidebar__scrollwrap";

  function getSidebar() {
    return document.querySelector(sidebarSelector);
  }

  function rememberSidebarPosition() {
    const sidebar = getSidebar();
    if (sidebar) {
      sessionStorage.setItem(storageKey, String(sidebar.scrollTop));
    }
  }

  function restoreSidebarPosition() {
    const storedPosition = sessionStorage.getItem(storageKey);
    if (storedPosition === null) {
      return;
    }

    const scrollTop = Number(storedPosition);
    if (!Number.isFinite(scrollTop)) {
      sessionStorage.removeItem(storageKey);
      return;
    }

    const restore = function () {
      const sidebar = getSidebar();
      if (sidebar) {
        sidebar.scrollTop = scrollTop;
      }
    };

    // Material centers the active link during its own document update. Restore
    // after that update and once more after the browser completes layout.
    restore();
    requestAnimationFrame(function () {
      restore();
      requestAnimationFrame(restore);
    });
    sessionStorage.removeItem(storageKey);
  }

  document.addEventListener(
    "click",
    function (event) {
      if (event.target.closest(".md-sidebar--primary .md-nav__link[href]")) {
        rememberSidebarPosition();
      }
    },
    true
  );

  if (typeof document$ !== "undefined") {
    document$.subscribe(restoreSidebarPosition);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", restoreSidebarPosition);
  } else {
    restoreSidebarPosition();
  }
})();
