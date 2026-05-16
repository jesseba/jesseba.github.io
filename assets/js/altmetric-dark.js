// Altmetric donut badges bake the score into an image; fix visibility in dark mode.
(function () {
  function isDark() {
    return document.documentElement.getAttribute("data-theme") === "dark";
  }

  function scoreFromEmbed(embed) {
    const span = embed.querySelector("._altmetric_score");
    if (span) return span.textContent.trim();

    const img = embed.querySelector("img[alt]");
    if (img) {
      const match = img.getAttribute("alt").match(/score of ([\d.,]+[km]?)/i);
      if (match) return match[1];
    }
    return null;
  }

  function fixEmbed(embed) {
    if (!embed.classList.contains("altmetric-embed")) return;

    const span = embed.querySelector("._altmetric_score");
    if (span) {
      if (isDark()) {
        span.style.setProperty("color", "#ffffff", "important");
      } else {
        span.style.removeProperty("color");
      }
      return;
    }

    const link = embed.querySelector("a");
    if (!link) return;

    let overlay = link.querySelector(".altmetric-score-overlay");

    if (!isDark()) {
      overlay?.remove();
      return;
    }

    const score = scoreFromEmbed(embed);
    if (!score) return;

    if (!overlay) {
      overlay = document.createElement("span");
      overlay.className = "altmetric-score-overlay";
      overlay.setAttribute("aria-hidden", "true");
      link.appendChild(overlay);
    }

    overlay.textContent = score;
  }

  function fixAll() {
    document.querySelectorAll(".altmetric-embed").forEach(fixEmbed);
  }

  let fixTimer;
  function scheduleFix() {
    clearTimeout(fixTimer);
    fixTimer = setTimeout(fixAll, 80);
  }

  document.addEventListener(
    "altmetric:show",
    function (e) {
      if (e.target?.classList?.contains("altmetric-embed")) {
        fixEmbed(e.target);
      } else {
        scheduleFix();
      }
    },
    true,
  );

  new MutationObserver(scheduleFix).observe(document.body, {
    childList: true,
    subtree: true,
  });

  new MutationObserver(scheduleFix).observe(document.documentElement, {
    attributes: true,
    attributeFilter: ["data-theme"],
  });

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", fixAll);
  } else {
    fixAll();
  }

  window.addEventListener("load", fixAll);
  [400, 1200, 2500].forEach(function (delay) {
    setTimeout(fixAll, delay);
  });
})();
