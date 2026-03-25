---
layout: archive
title: "Freelance"
permalink: /freelance/
redirect_from:
  - /software/
author_profile: true
---

{% assign software_projects = site.data.software_projects %}
{% assign freelance_reviews = site.data.freelance_reviews %}

<section class="home-hero software-hero">
  <div class="home-hero__content">
    <p class="home-hero__eyebrow">Freelance Software Development</p>
    <h2 class="home-hero__title">Custom software projects across business systems, engineering tools, IoT, robotics, and interactive applications</h2>
    <p class="home-hero__lead">Alongside academic research, I have delivered freelance software work spanning desktop applications, engineering and scientific tools, IoT and automation systems, robotics-oriented prototypes, and C++ graphics applications. The portfolio reflects practical implementation work shaped by client requirements, technical constraints, and delivery discipline.</p>
    <div class="home-hero__actions">
      <a class="btn btn--primary" href="https://mostaql.com/u/abdoHamdy7/portfolio">View Mostaql Portfolio</a>
      <a class="btn btn--inverse" href="https://www.upwork.com/freelancers/~018e3a61645a677b31">View Upwork Profile</a>
    </div>
  </div>

  <aside class="home-hero__panel">
    <p class="home-hero__panel-label">Freelance focus</p>
    <ul class="home-hero__facts">
      <li><strong>Platforms:</strong> Mostaql and Upwork.</li>
      <li><strong>Typical work:</strong> Desktop systems, scientific computing tools, IoT automation, robotics, and graphics applications.</li>
      <li><strong>Implementation style:</strong> Direct, requirements-driven, and oriented toward usable deliverables.</li>
      <li><strong>Client profile:</strong> Business, academic, engineering, and technical support projects.</li>
    </ul>
  </aside>
</section>

<section class="home-stat-grid" aria-label="Freelance portfolio summary">
  <div class="home-stat">
    <span class="home-stat__value">2</span>
    <span class="home-stat__label">Freelance Platforms</span>
  </div>
  <div class="home-stat">
    <span class="home-stat__value">{{ software_projects.size }}</span>
    <span class="home-stat__label">Featured Projects</span>
  </div>
  <div class="home-stat">
    <span class="home-stat__value">5.0</span>
    <span class="home-stat__label">Client Rating Snapshot</span>
  </div>
  <div class="home-stat">
    <span class="home-stat__value">4</span>
    <span class="home-stat__label">Main Delivery Domains</span>
  </div>
</section>

<section class="home-section">
  <div class="home-section__header">
    <div>
      <h2 class="home-section__title">Client Feedback</h2>
      <p class="home-section__lede">Selected feedback adapted from the shared Mostaql and Upwork review screenshots. Arabic feedback is translated where noted.</p>
    </div>
  </div>

  <div class="testimonial-grid">
    {% for review in freelance_reviews %}
      <article class="testimonial-card">
        <div class="testimonial-card__meta">
          <span class="pub-badge pub-badge--category">{{ review.platform }}</span>
          <span class="testimonial-card__stars" aria-label="5-star review">★★★★★</span>
        </div>
        <h3 class="testimonial-card__project">{{ review.project }}</h3>
        <p class="testimonial-card__quote">“{{ review.quote }}”</p>
        <p class="testimonial-card__client">{{ review.client }}</p>
        {% if review.note %}
          <p class="testimonial-card__note">{{ review.note }}</p>
        {% endif %}
      </article>
    {% endfor %}
  </div>
</section>

<section class="home-section">
  <div class="home-section__header">
    <div>
      <h2 class="home-section__title">What I Build</h2>
      <p class="home-section__lede">The portfolio is strongest where software intersects with engineering, technical workflows, and implementation-heavy problem solving.</p>
    </div>
  </div>

  <div class="home-card-grid">
    <article class="home-card">
      <p class="home-card__kicker">Desktop and Business Systems</p>
      <h3 class="home-card__title">Operational software for real workflows</h3>
      <p>Custom desktop applications for stores, contracts, sales, and structured administrative tasks with practical interfaces and data handling.</p>
      <div class="tag-list">
        <span class="tag-pill">Desktop Apps</span>
        <span class="tag-pill">CRUD Workflows</span>
        <span class="tag-pill">Internal Tools</span>
      </div>
    </article>

    <article class="home-card">
      <p class="home-card__kicker">Scientific and Engineering Tools</p>
      <h3 class="home-card__title">MATLAB and technical computing support</h3>
      <p>Engineering-oriented software tasks including MATLAB GUIs, technical figure generation, image-processing workflows, and analytical support for research or coursework.</p>
      <div class="tag-list">
        <span class="tag-pill">MATLAB</span>
        <span class="tag-pill">GUI Tools</span>
        <span class="tag-pill">Scientific Computing</span>
      </div>
    </article>

    <article class="home-card">
      <p class="home-card__kicker">IoT, Automation, and Robotics</p>
      <h3 class="home-card__title">Embedded and control-oriented prototyping</h3>
      <p>Implementation work covering IoT communication, automation, robotics behavior, lab-scale control, and hardware-in-the-loop experimentation.</p>
      <div class="tag-list">
        <span class="tag-pill">IoT</span>
        <span class="tag-pill">Robotics</span>
        <span class="tag-pill">Automation</span>
      </div>
    </article>

    <article class="home-card">
      <p class="home-card__kicker">Graphics and Interactive Software</p>
      <h3 class="home-card__title">C++ and OpenGL-based visual applications</h3>
      <p>Interactive graphics projects involving 2D animation, game-style environments, 3D visualization, object development, and camera logic in OpenGL.</p>
      <div class="tag-list">
        <span class="tag-pill">C++</span>
        <span class="tag-pill">OpenGL</span>
        <span class="tag-pill">Visualization</span>
      </div>
    </article>
  </div>
</section>

<section class="home-section">
  <div class="home-section__header">
    <div>
      <h2 class="home-section__title">Selected Freelance Projects</h2>
      <p class="home-section__lede">Representative examples drawn from the shared portfolio material on Mostaql and related freelance work.</p>
    </div>
  </div>

  <div class="software-project-grid">
    {% for project in software_projects %}
      <article class="software-card">
        {% if project.image %}
          <div class="software-card__media">
            <img src="{{ project.image | replace: ' ', '%20' }}" alt="{{ project.title }}">
          </div>
        {% endif %}
        <div class="software-card__header">
          <span class="pub-badge pub-badge--category">{{ project.category }}</span>
        </div>
        <h3 class="software-card__title">{{ project.title }}</h3>
        <p class="software-card__summary">{{ project.summary }}</p>
        {% if project.stack %}
          <div class="tag-list">
            {% for item in project.stack %}
              <span class="tag-pill">{{ item }}</span>
            {% endfor %}
          </div>
        {% endif %}
      </article>
    {% endfor %}
  </div>
</section>

<section class="home-section home-section--compact">
  <div class="home-card software-cta">
    <p class="home-card__kicker">Collaboration</p>
    <h3 class="home-card__title">Freelance and technical project links</h3>
    <p>If you want to review the platform-facing portfolio directly, these are the public profile links I use for freelance software work and client-facing project history.</p>
    <div class="home-hero__actions">
      <a class="btn btn--primary" href="https://mostaql.com/u/abdoHamdy7/portfolio">Mostaql Portfolio</a>
      <a class="btn btn--inverse" href="https://www.upwork.com/freelancers/~018e3a61645a677b31">Upwork Profile</a>
      <a class="btn btn--inverse" href="mailto:abdulrahman_hamdy@ieee.org">Email</a>
    </div>
  </div>
</section>
