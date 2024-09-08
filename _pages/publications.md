---
layout: page
permalink: /publications/
title: publications
description: publications by categories in reversed chronological order.
nav: true
nav_order: 1
---

<div class="publications">
  {% assign sorted_publications = site.data.publications | sort: "year" | reverse %}
  {% for publication in sorted_publications %}
    <div class="publication">
      <h3>{{ publication.title }}</h3>
      <p><strong>Authors:</strong> {{ publication.authors }}</p>
      <p>
        <strong>Journal:</strong> {{ publication.journal }}
        {% if publication.abbr %} ({{ publication.abbr }}){% endif %}
        {% if publication.volume %}, {{ publication.volume }}{% endif %}
        {% if publication.number %}({{ publication.number }}){% endif %}
        {% if publication.pages %}: {{ publication.pages }}{% endif %}, 
        {{ publication.year }}
      </p>
      {% if publication.publisher %}
        <p><strong>Publisher:</strong> {{ publication.publisher }}</p>
      {% endif %}
    </div>
  {% endfor %}
</div>
