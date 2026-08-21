// Minimal full-screen photo viewer for the /photography/ galleries.
//
// Binds every [data-photo] anchor on the page as one sequence in document order,
// so navigation runs across location sections rather than restarting per section.
// No dependencies; the grid works without it (anchors fall back to the raw image).

(function () {
  "use strict";

  var all = Array.prototype.slice.call(document.querySelectorAll("a[data-photo]"));
  if (!all.length) return;

  // Recomputed each time the viewer opens, so photographs that photo-fallback.js
  // has hidden (deleted on Flickr since the last import) drop out of the sequence
  // rather than showing up as a blank frame under the arrow keys.
  var items = all;

  function refresh() {
    items = all.filter(function (el) {
      return !el.hidden && el.offsetParent !== null;
    });
  }

  var index = -1;
  var overlay, figure, image, caption, counter, source, prevBtn, nextBtn, lastFocused;

  function build() {
    overlay = document.createElement("div");
    overlay.className = "photo-lightbox";
    overlay.setAttribute("role", "dialog");
    overlay.setAttribute("aria-modal", "true");
    overlay.setAttribute("aria-label", "Photo viewer");
    overlay.hidden = true;

    overlay.innerHTML = [
      '<button class="photo-lightbox-close" type="button" aria-label="Close">&times;</button>',
      '<button class="photo-lightbox-prev" type="button" aria-label="Previous photo">&#8249;</button>',
      '<button class="photo-lightbox-next" type="button" aria-label="Next photo">&#8250;</button>',
      '<figure class="photo-lightbox-figure">',
      '  <img alt="">',
      '  <figcaption><span class="photo-lightbox-caption"></span>',
      '  <span class="photo-lightbox-counter"></span>',
      '  <a class="photo-lightbox-source" target="_blank" rel="noopener">View on Flickr</a></figcaption>',
      "</figure>",
    ].join("");

    figure = overlay.querySelector(".photo-lightbox-figure");
    image = overlay.querySelector("img");
    caption = overlay.querySelector(".photo-lightbox-caption");
    counter = overlay.querySelector(".photo-lightbox-counter");
    source = overlay.querySelector(".photo-lightbox-source");
    prevBtn = overlay.querySelector(".photo-lightbox-prev");
    nextBtn = overlay.querySelector(".photo-lightbox-next");

    overlay.querySelector(".photo-lightbox-close").addEventListener("click", close);
    prevBtn.addEventListener("click", function () {
      show(index - 1);
    });
    nextBtn.addEventListener("click", function () {
      show(index + 1);
    });

    // A thumbnail can load while the full size has gone; say so rather than
    // leaving an empty frame open.
    image.addEventListener("error", function () {
      if (!image.getAttribute("src")) return;
      figure.classList.add("photo-lightbox-missing");
      caption.textContent = "This photograph is no longer available.";
    });

    // Click the backdrop (but not the photo itself) to dismiss.
    overlay.addEventListener("click", function (event) {
      if (!figure.contains(event.target)) close();
    });

    document.body.appendChild(overlay);
  }

  function preload(i) {
    if (i < 0 || i >= items.length) return;
    var img = new Image();
    img.src = items[i].getAttribute("href");
  }

  function show(i) {
    if (i < 0 || i >= items.length) return;
    index = i;

    var item = items[i];
    var text = item.getAttribute("data-caption") || "";
    var w = item.getAttribute("data-full-width");
    var h = item.getAttribute("data-full-height");

    figure.classList.remove("photo-lightbox-missing");

    // Reserve the right box before the full image lands, so nothing jumps.
    if (w && h) image.style.aspectRatio = w + " / " + h;

    image.src = item.getAttribute("href");
    image.alt = text || item.querySelector("img").alt || "";
    caption.textContent = text;
    counter.textContent = i + 1 + " / " + items.length;

    // Flickr's terms require embedded photos to link back to their photo page.
    var page = item.getAttribute("data-page");
    source.href = page || "";
    source.hidden = !page;

    prevBtn.disabled = i === 0;
    nextBtn.disabled = i === items.length - 1;

    preload(i + 1);
    preload(i - 1);
  }

  function open(i) {
    lastFocused = document.activeElement;
    overlay.hidden = false;
    document.body.classList.add("photo-lightbox-open");
    show(i);
    nextBtn.disabled ? prevBtn.focus() : nextBtn.focus();
  }

  function close() {
    overlay.hidden = true;
    document.body.classList.remove("photo-lightbox-open");
    image.removeAttribute("src");
    if (lastFocused && lastFocused.focus) lastFocused.focus();
  }

  build();

  all.forEach(function (item) {
    item.addEventListener("click", function (event) {
      // Leave modified clicks alone so "open in new tab" still works.
      if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      refresh();
      var position = items.indexOf(item);
      if (position !== -1) open(position);
    });
  });

  document.addEventListener("keydown", function (event) {
    if (overlay.hidden) return;
    if (event.key === "Escape") close();
    else if (event.key === "ArrowLeft") show(index - 1);
    else if (event.key === "ArrowRight") show(index + 1);
    else return;
    event.preventDefault();
  });

  // Horizontal swipe to page through, ignoring mostly-vertical drags.
  var startX = null;
  var startY = null;

  overlay.addEventListener(
    "touchstart",
    function (event) {
      startX = event.changedTouches[0].clientX;
      startY = event.changedTouches[0].clientY;
    },
    { passive: true }
  );

  overlay.addEventListener(
    "touchend",
    function (event) {
      if (startX === null) return;
      var dx = event.changedTouches[0].clientX - startX;
      var dy = event.changedTouches[0].clientY - startY;
      if (Math.abs(dx) > 45 && Math.abs(dx) > Math.abs(dy)) {
        show(dx < 0 ? index + 1 : index - 1);
      }
      startX = startY = null;
    },
    { passive: true }
  );
})();
