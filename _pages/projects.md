---
layout: archive
title: "Projects"
permalink: /projects/
author_profile: true
---

These project pages organize my main research threads into focused areas of work, each connecting methods, systems, and representative publications.

{% assign projects = site.portfolio | sort: "order" %}

<div class="project-grid">
  {% for project in projects %}
    {% include project-card.html project=project %}
  {% endfor %}
</div>
