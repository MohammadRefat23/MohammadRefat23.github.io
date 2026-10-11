(() => {
  async function fetchJson(path) {
    const response = await fetch(path, { cache: "no-cache" });
    if (!response.ok) throw new Error(`Could not load ${path} (${response.status})`);
    return response.json();
  }

  function createRow(pokemon) {
    const row = document.createElement("div");
    row.className = "vgc-rank-row";
    row.dataset.pokemon = pokemon.name;

    const rank = document.createElement("span");
    rank.className = "vgc-rank-number";
    rank.textContent = `#${pokemon.rank}`;

    const name = document.createElement("span");
    name.className = "vgc-species";
    name.textContent = pokemon.name;

    const track = document.createElement("span");
    track.className = "vgc-bar-track";
    track.setAttribute("aria-hidden", "true");
    const bar = document.createElement("span");
    bar.className = "vgc-bar";
    const usage = Number(pokemon.usage_pct) || 0;
    bar.style.width = `${Math.max(0, Math.min(100, usage))}%`;
    track.append(bar);

    const percentage = document.createElement("span");
    percentage.className = "vgc-usage";
    percentage.textContent = `${usage.toFixed(2)}%`;

    row.append(rank, name, track, percentage);
    return row;
  }

  function renderRanks(container, rows, topN) {
    const visible = (rows || []).slice(0, topN);
    const previousRows = new Map(
      [...container.children]
        .filter((row) => row.classList.contains("vgc-rank-row"))
        .map((row) => [row.dataset.pokemon, row]),
    );
    const nextRows = visible.map((pokemon) => {
      let row = previousRows.get(pokemon.name);
      if (!row || row.children.length !== 4 || !row.children[2].firstElementChild) {
        row = createRow(pokemon);
      }
      const [rank, name, track, percentage] = row.children;
      const bar = track.firstElementChild;
      const usage = Number(pokemon.usage_pct) || 0;
      row.dataset.pokemon = pokemon.name;
      rank.textContent = `#${pokemon.rank}`;
      name.textContent = pokemon.name;
      bar.style.width = `${Math.max(0, Math.min(100, usage))}%`;
      percentage.textContent = `${usage.toFixed(2)}%`;
      return row;
    });

    container.replaceChildren(...nextRows);
    if (!visible.length) {
      const empty = document.createElement("p");
      empty.textContent = "No rank data is available for this snapshot.";
      container.append(empty);
    }
  }

  function renderMoverList(container, rows) {
    container.replaceChildren();
    rows.forEach((row) => {
      const item = document.createElement("li");
      const changeValue = Number(row.usage_change_pp);
      const change = `${changeValue > 0 ? "+" : ""}${changeValue.toFixed(2)} pp`;
      item.textContent = `${row.pokemon}: ${change} (${row.earlier_rank} → ${row.later_rank})`;
      container.append(item);
    });
  }

  function renderComparison(root, comparison) {
    const range = root.querySelector("[data-comparison-range]");
    const summary = root.querySelector("[data-comparison-summary]");
    const gains = root.querySelector("[data-usage-gains]");
    const declines = root.querySelector("[data-usage-declines]");
    if (!comparison) {
      range.textContent = "A comparison will appear when two reports exist for one regulation.";
      summary.textContent = "No same-regulation month pair is available yet.";
      gains.replaceChildren();
      declines.replaceChildren();
      return;
    }

    range.textContent = `${comparison.earlier_month} → ${comparison.later_month} · Regulation ${comparison.regulation}`;
    const rhoText = comparison.spearman_rho_shared == null
      ? "unavailable"
      : Number(comparison.spearman_rho_shared).toFixed(3);
    const battleText = `${Number(comparison.earlier_battles || 0).toLocaleString()} → ${Number(comparison.later_battles || 0).toLocaleString()} battles`;
    const entryText = comparison.top_n_entered.length ? comparison.top_n_entered.join(", ") : "none";
    const exitText = comparison.top_n_exited.length ? comparison.top_n_exited.join(", ") : "none";
    summary.textContent =
      `${comparison.top_n_overlap}/${comparison.top_n} Pokémon remained in the top ${comparison.top_n}; ` +
      `Spearman ρ = ${rhoText} across ${comparison.shared_roster} shared Pokémon. ` +
      `Top-15 entrants: ${entryText}. Exits: ${exitText}. ${battleText}. ` +
      "Descriptive comparison only; the reports do not establish significance or causation.";
    renderMoverList(gains, comparison.largest_usage_gains);
    renderMoverList(declines, comparison.largest_usage_declines);
  }

  function setupWidget(root, current, historyIndex) {
    const topN = Number(current.top_n) || 15;
    const currentMeta = root.querySelector("[data-current-format]");
    const currentMonth = root.querySelector("[data-current-month]");
    const summary = root.querySelector("[data-rank-summary]");
    const currentRanks = root.querySelector("[data-current-ranks]");
    const regulationSelect = root.querySelector("[data-regulation]");
    const slider = root.querySelector("[data-month-slider]");
    const monthLabel = root.querySelector("[data-month-label]");
    const historyRanks = root.querySelector("[data-history-ranks]");
    const status = root.querySelector("[data-history-status]");
    const playButton = root.querySelector("[data-play]");
    const historyRoot = root.dataset.historyRoot;

    const hasCurrentData = Array.isArray(current.pokemon) && current.pokemon.length > 0;
    currentMeta.textContent = hasCurrentData
      ? `${current.format} · Regulation ${current.regulation} · ${current.rating_cutoff}+`
      : "Waiting for first Smogon data import";
    currentMonth.textContent = hasCurrentData ? `Latest: ${current.month}` : "";
    summary.textContent = hasCurrentData
      ? `Latest report: ${Number(current.total_battles || 0).toLocaleString()} battles. Showing the top ${topN}; bars use a fixed 0–100% usage scale.`
      : "The data importer will populate this view with Smogon's published monthly Champions VGC Bo3 statistics.";
    renderRanks(currentRanks, current.pokemon, topN);

    const byRegulation = new Map();
    for (const snapshot of historyIndex.snapshots || []) {
      const list = byRegulation.get(snapshot.regulation) || [];
      list.push(snapshot);
      byRegulation.set(snapshot.regulation, list);
    }

    const regulations = [...byRegulation.keys()].sort((a, b) => a.localeCompare(b));
    if (!regulations.length) {
      status.textContent = "Monthly history will appear after the first import.";
      renderComparison(root, null);
      return;
    }

    regulationSelect.replaceChildren(...regulations.map((regulation) => {
      const option = document.createElement("option");
      option.value = regulation;
      option.textContent = `Regulation ${regulation}`;
      return option;
    }));
    regulationSelect.disabled = false;
    slider.disabled = false;
    playButton.disabled = false;

    let snapshots = [];
    let timer = null;
    const cache = new Map();

    async function loadSnapshot(meta) {
      let snapshot = cache.get(meta.path);
      if (!snapshot) {
        snapshot = await fetchJson(`${historyRoot}${meta.path}`);
        cache.set(meta.path, snapshot);
      }
      return snapshot;
    }

    async function drawSnapshot(position) {
      const meta = snapshots[position];
      if (!meta) return;
      slider.value = String(position);
      monthLabel.textContent = meta.month;
      const snapshot = await loadSnapshot(meta);
      renderRanks(historyRanks, snapshot.pokemon, topN);
      status.textContent = `${snapshot.month} · ${Number(snapshot.total_battles || 0).toLocaleString()} battles`;
    }

    async function selectRegulation(regulation) {
      snapshots = (byRegulation.get(regulation) || []).slice().sort((a, b) => a.month.localeCompare(b.month));
      slider.min = "0";
      slider.max = String(Math.max(0, snapshots.length - 1));
      slider.value = String(Math.max(0, snapshots.length - 1));
      await drawSnapshot(Number(slider.value));
      const pair = snapshots.slice(-2);
      if (pair.length === 2) {
        const comparison = (historyIndex.comparisons || []).find((item) =>
          item.regulation === regulation &&
          item.earlier_month === pair[0].month &&
          item.later_month === pair[1].month,
        );
        renderComparison(root, comparison || null);
      } else {
        renderComparison(root, null);
      }
    }

    regulationSelect.addEventListener("change", () => {
      selectRegulation(regulationSelect.value).catch((error) => {
        status.textContent = error.message;
      });
    });
    slider.addEventListener("input", () => {
      drawSnapshot(Number(slider.value)).catch((error) => {
        status.textContent = error.message;
      });
    });
    playButton.addEventListener("click", () => {
      if (timer) {
        window.clearInterval(timer);
        timer = null;
        playButton.textContent = "Play";
        return;
      }
      playButton.textContent = "Pause";
      timer = window.setInterval(() => {
        const next = Number(slider.value) >= Number(slider.max) ? 0 : Number(slider.value) + 1;
        drawSnapshot(next).catch((error) => {
          status.textContent = error.message;
          window.clearInterval(timer);
          timer = null;
          playButton.textContent = "Play";
        });
      }, 1100);
    });

    const initialRegulation = regulations.includes(current.regulation)
      ? current.regulation
      : regulations.at(-1);
    regulationSelect.value = initialRegulation;
    selectRegulation(initialRegulation).catch((error) => {
      status.textContent = error.message;
    });
  }

  async function init() {
    const roots = [...document.querySelectorAll("[data-vgc-ranks]")];
    if (!roots.length) return;
    try {
      const dataRoot = roots[0];
      const [current, historyIndex] = await Promise.all([
        fetchJson(dataRoot.dataset.currentUrl),
        fetchJson(dataRoot.dataset.historyIndexUrl),
      ]);
      roots.forEach((root) => setupWidget(root, current, historyIndex));
    } catch (error) {
      roots.forEach((root) => {
        const summary = root.querySelector("[data-rank-summary]");
        if (summary) summary.textContent = `Usage ranks could not be loaded: ${error.message}`;
        const status = root.querySelector("[data-history-status]");
        if (status) status.textContent = "Data is unavailable.";
      });
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init, { once: true });
  } else {
    init();
  }
})();
