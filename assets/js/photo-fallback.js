// Drop photographs Flickr no longer serves, instead of showing broken images.
//
// Images are hotlinked from Flickr's CDN, so a photo deleted or made private
// after the last import would otherwise render as a broken-image icon on a live
// page. This hides those quietly: the grid closes up, a chapter that loses every
// photo drops its heading too, and a missing index cover falls back to a caption.
//
// Runs on the photography index and on gallery pages. bin/check-photos does the
// same job at build time, against the manifests.

(function () {
  "use strict";

  // An <img> that has finished loading with no intrinsic width has failed.
  // Checked directly as well as via the error event, since lazy-loaded images
  // may already have failed before this script runs.
  function hasFailed(img) {
    return img.complete && img.naturalWidth === 0;
  }

  function hideItem(img) {
    var item = img.closest(".photo-item");
    if (!item || item.hidden) return;
    item.hidden = true;
    sweep();
  }

  function replaceCover(img) {
    var holder = img.closest(".photo-collection-image");
    if (!holder) return;
    var placeholder = document.createElement("div");
    placeholder.className = "photo-collection-placeholder";
    placeholder.innerHTML = "<span>photo unavailable</span>";
    holder.replaceChildren(placeholder);
  }

  // Hide any grid left with nothing in it, along with its chapter heading, and
  // say something if a whole gallery has gone rather than rendering blank.
  function sweep() {
    var grids = document.querySelectorAll(".photo-grid");
    var living = 0;

    Array.prototype.forEach.call(grids, function (grid) {
      var alive = grid.querySelectorAll(".photo-item:not([hidden])").length;
      grid.hidden = alive === 0;
      living += alive;

      var heading = grid.previousElementSibling;
      if (heading && heading.classList.contains("gallery-section")) {
        heading.hidden = alive === 0;
      }
    });

    var body = document.querySelector(".gallery-body");
    if (!grids.length || !body) return;

    var notice = document.getElementById("gallery-all-missing");
    if (living === 0 && !notice) {
      notice = document.createElement("p");
      notice.id = "gallery-all-missing";
      notice.className = "gallery-empty";
      notice.textContent = "These photographs are no longer available.";
      body.appendChild(notice);
    } else if (living > 0 && notice) {
      notice.remove();
    }
  }

  function watch(img, onFail) {
    if (hasFailed(img)) {
      onFail(img);
      return;
    }
    img.addEventListener("error", function () {
      onFail(img);
    });
  }

  Array.prototype.forEach.call(document.querySelectorAll(".photo-item img"), function (img) {
    watch(img, hideItem);
  });

  Array.prototype.forEach.call(document.querySelectorAll(".photo-collection-image img"), function (img) {
    watch(img, replaceCover);
  });
})();
