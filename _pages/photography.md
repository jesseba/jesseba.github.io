---
layout: page
permalink: /photography/
title: photography
# Curly quotes, not straight. This description is interpolated unquoted into
# the JSON-LD in _includes/metadata.liquid, so a bare " would break that object
# — the block is behind a config flag and emits nothing today, but the trap is
# still there for whoever turns it on.
description: “f/8 and be there” — Weegee
nav: true
nav_order: 2
# loads photo-fallback.js, so a cover deleted on Flickr degrades to a caption
photography: true
---

{% include photo_index.liquid %}
