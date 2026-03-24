---
layout: archive
title: "Updates"
permalink: /updates/
author_profile: true
---

This page highlights recent research, publications, datasets, and academic milestones.

<div class="updates-feed">
  {% for item in site.data.updates %}
    <article class="update-card">
      <div class="update-card__meta">
        <span class="update-card__type">{{ item.type }}</span>
        <time datetime="{{ item.date }}">{{ item.date | date: "%B %d, %Y" }}</time>
      </div>
      <h2 class="update-card__title">
        {% if item.link %}
          <a href="{{ item.link }}">{{ item.title }}</a>
        {% else %}
          {{ item.title }}
        {% endif %}
      </h2>
      <p class="update-card__summary">{{ item.summary }}</p>
    </article>
  {% endfor %}
</div>
