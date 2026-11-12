(function () {
  const bar = document.createElement("div");
  bar.className = "nx-progress";
  bar.setAttribute("aria-hidden", "true");
  document.body.appendChild(bar);
  function update() {
    const doc = document.documentElement;
    const max = doc.scrollHeight - doc.clientHeight;
    bar.style.width = (max > 0 ? (doc.scrollTop / max) * 100 : 0) + "%";
  }
  window.addEventListener("scroll", update, { passive: true });
  window.addEventListener("resize", update);
  update();
})();

(function () {
  const table = document.getElementById("nx-challenge-table");
  if (!table) return;

  const rows = Array.from(table.tBodies[0].rows);
  const search = document.getElementById("nx-search");
  const count = document.getElementById("nx-count");
  const empty = document.getElementById("nx-empty");
  const reset = document.getElementById("nx-reset");
  const statusButtons = Array.from(
    document.querySelectorAll("[data-status-filter]")
  );
  const categoryButtons = Array.from(
    document.querySelectorAll("[data-category-filter]")
  );
  const eventButtons = Array.from(
    document.querySelectorAll("[data-event-filter]")
  );
  let status = "all";
  let category = "all";
  let track = "all";
  let query = "";

  function sync(buttons, attribute, value) {
    buttons.forEach(function (button) {
      const active = button.dataset[attribute] === value;
      button.classList.toggle("is-active", active);
      button.setAttribute("aria-pressed", active ? "true" : "false");
    });
  }

  function apply() {
    let visible = 0;
    rows.forEach(function (row) {
      const matchStatus = status === "all" || row.dataset.status === status;
      const matchCategory =
        category === "all" || row.dataset.category === category;
      const matchTrack = track === "all" || row.dataset.event === track;
      const matchQuery =
        !query || row.dataset.search.toLowerCase().includes(query);
      const show = matchStatus && matchCategory && matchTrack && matchQuery;
      row.hidden = !show;
      if (show) visible += 1;
    });
    count.textContent = visible + " challenge";
    empty.hidden = visible !== 0;
  }

  statusButtons.forEach(function (button) {
    button.addEventListener("click", function () {
      status = button.dataset.statusFilter;
      sync(statusButtons, "statusFilter", status);
      apply();
    });
  });

  categoryButtons.forEach(function (button) {
    button.addEventListener("click", function () {
      category = button.dataset.categoryFilter;
      sync(categoryButtons, "categoryFilter", category);
      apply();
      const target = document.getElementById("daftar-challenge");
      if (target) target.scrollIntoView({ behavior: "smooth", block: "start" });
    });
  });

  eventButtons.forEach(function (button) {
    button.addEventListener("click", function () {
      track = button.dataset.eventFilter;
      sync(eventButtons, "eventFilter", track);
      apply();
      const target = document.getElementById("daftar-challenge");
      if (target) target.scrollIntoView({ behavior: "smooth", block: "start" });
    });
  });

  if (search) {
    search.addEventListener("input", function () {
      query = search.value.trim().toLowerCase();
      apply();
    });
  }

  if (reset) {
    reset.addEventListener("click", function () {
      status = "all";
      category = "all";
      track = "all";
      query = "";
      if (search) search.value = "";
      sync(statusButtons, "statusFilter", status);
      sync(categoryButtons, "categoryFilter", category);
      sync(eventButtons, "eventFilter", track);
      apply();
    });
  }

  document.addEventListener("keydown", function (event) {
    const tag = document.activeElement.tagName;
    const typing = tag === "INPUT" || tag === "TEXTAREA";
    if (event.key === "/" && !typing && search) {
      event.preventDefault();
      search.focus();
    }
    if (event.key === "Escape" && document.activeElement === search) {
      search.value = "";
      query = "";
      apply();
      search.blur();
    }
  });

  apply();
})();
