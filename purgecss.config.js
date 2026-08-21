module.exports = {
  content: ["_site/**/*.html", "_site/**/*.js"],
  css: ["_site/assets/css/*.css"],
  output: "_site/assets/css/",
  skippedContentGlobs: ["_site/assets/**/*.html"],
  safelist: {
    // photo-*/gallery-*: the lightbox builds its markup in JS and some gallery
    // states (empty collection, missing cover) never appear in the built HTML.
    deep: [/citation-count/, /altmetric-embed/, /publication-actions/, /^photo-/, /^gallery-/],
  },
};
