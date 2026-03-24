---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

{% assign projects = site.portfolio | sort: "order" %}
{% assign publication_count = site.publications | size %}
{% assign journal_count = site.publications | where: "category", "manuscripts" | size %}
{% assign conference_count = site.publications | where: "category", "conference" | size %}

<section class="home-hero">
  <div class="home-hero__content">
    <p class="home-hero__eyebrow">Research Agenda</p>
    <h2 class="home-hero__title">Decision-making, control, and data for deployable autonomous systems</h2>
    <p class="home-hero__lead">My research is centered on autonomous driving and intelligent transportation systems, with emphasis on decision-making under uncertainty, risk-aware planning, connected mobility, and deployable autonomy stacks. I work across optimization, control, learning, and dataset-driven research infrastructure to address problems that matter in real traffic environments.</p>
  </div>

  <aside class="home-hero__panel">
    <p class="home-hero__panel-label">Current focus</p>
    <ul class="home-hero__facts">
      <li><strong>Autonomous driving:</strong> Local planning, spatiotemporal risk, and online decision-making.</li>
      <li><strong>Transportation systems:</strong> Signal-aware control, eco-driving, and emergency-vehicle prioritization.</li>
      <li><strong>Learning and control:</strong> Reinforcement learning, optimal control, and practical system design.</li>
      <li><strong>Data infrastructure:</strong> Trajectory prediction, multi-task datasets, and privacy-aware release workflows.</li>
    </ul>
  </aside>
</section>

<section class="home-stat-grid" aria-label="Research summary">
  <div class="home-stat">
    <span class="home-stat__value">{{ projects.size }}</span>
    <span class="home-stat__label">Research Threads</span>
  </div>
  <div class="home-stat">
    <span class="home-stat__value">{{ publication_count }}</span>
    <span class="home-stat__label">Publications</span>
  </div>
  <div class="home-stat">
    <span class="home-stat__value">{{ journal_count }}</span>
    <span class="home-stat__label">Journal Articles</span>
  </div>
  <div class="home-stat">
    <span class="home-stat__value">{{ conference_count }}</span>
    <span class="home-stat__label">Conference Papers</span>
  </div>
</section>

<section class="home-section">
  <div class="home-section__header">
    <div>
      <h2 class="home-section__title">Research Threads</h2>
      <p class="home-section__lede">The main lines of my work, each organized as a focused project page with methods, questions, and representative outputs.</p>
    </div>
    <a class="home-section__link" href="/projects/">All projects</a>
  </div>

  <div class="project-grid">
    {% for project in projects %}
      {% include project-card.html project=project %}
    {% endfor %}
  </div>
</section>

<section class="home-section">
  <div class="home-section__header">
    <div>
      <h2 class="home-section__title">Methodological Toolkit</h2>
      <p class="home-section__lede">A mix of optimization, simulation, control, and learning methods used across research problems.</p>
    </div>
  </div>

  <div class="home-card-grid">
    <article class="home-card">
      <p class="home-card__kicker">Planning and Optimization</p>
      <h3 class="home-card__title">Risk-aware decision-making under uncertainty</h3>
      <p>I develop local planning and optimization methods that account for uncertainty, safety constraints, and real-time feasibility in dynamic traffic environments.</p>
      <div class="tag-list">
        <span class="tag-pill">Graph-Based Planning</span>
        <span class="tag-pill">Constrained Shortest Path</span>
        <span class="tag-pill">Online Optimization</span>
        <span class="tag-pill">Risk Bounds</span>
      </div>
    </article>

    <article class="home-card">
      <p class="home-card__kicker">Control and Learning</p>
      <h3 class="home-card__title">Data-informed control for engineering systems</h3>
      <p>I combine reinforcement learning with classical control and systems modeling to design controllers that remain interpretable and engineering-relevant.</p>
      <div class="tag-list">
        <span class="tag-pill">Reinforcement Learning</span>
        <span class="tag-pill">Optimal Control</span>
        <span class="tag-pill">LQR and PID</span>
        <span class="tag-pill">Simulation-Driven Design</span>
      </div>
    </article>

    <article class="home-card">
      <p class="home-card__kicker">Transportation Systems</p>
      <h3 class="home-card__title">Infrastructure-aware autonomy in mixed traffic</h3>
      <p>I study how connected and autonomous vehicles can interact with traffic infrastructure to improve travel time, energy efficiency, and emergency response.</p>
      <div class="tag-list">
        <span class="tag-pill">Eco-Driving</span>
        <span class="tag-pill">Signal Preemption</span>
        <span class="tag-pill">Dynamic Path Planning</span>
        <span class="tag-pill">Mixed Traffic</span>
      </div>
    </article>

    <article class="home-card">
      <p class="home-card__kicker">Datasets and Evaluation</p>
      <h3 class="home-card__title">Benchmarks, prediction, and research infrastructure</h3>
      <p>I contribute to trajectory-prediction surveys, multi-task benchmark datasets, anonymization workflows, and data-driven evaluation pipelines for autonomous-driving research.</p>
      <div class="tag-list">
        <span class="tag-pill">Trajectory Prediction</span>
        <span class="tag-pill">Benchmark Design</span>
        <span class="tag-pill">Privacy-Aware Data Release</span>
        <span class="tag-pill">Perception Workflows</span>
      </div>
    </article>
  </div>
</section>

<section class="home-section">
  <div class="home-section__header">
    <div>
      <h2 class="home-section__title">Platforms and Research Stack</h2>
      <p class="home-section__lede">The software and simulation ecosystem behind the research.</p>
    </div>
  </div>

  <div class="home-card-grid">
    <article class="home-card">
      <p class="home-card__kicker">Autonomous Driving and Robotics</p>
      <h3 class="home-card__title">Simulation and autonomy tooling</h3>
      <div class="tag-list">
        <span class="tag-pill">CARLA</span>
        <span class="tag-pill">ROS 2</span>
        <span class="tag-pill">NAV2</span>
        <span class="tag-pill">RViz2</span>
        <span class="tag-pill">Foxglove</span>
        <span class="tag-pill">Autoware</span>
        <span class="tag-pill">CommonRoad</span>
        <span class="tag-pill">RoadRunner</span>
      </div>
    </article>

    <article class="home-card">
      <p class="home-card__kicker">Traffic and Control Infrastructure</p>
      <h3 class="home-card__title">Traffic simulation and modeling</h3>
      <div class="tag-list">
        <span class="tag-pill">PTV Vissim</span>
        <span class="tag-pill">SUMO</span>
        <span class="tag-pill">MATLAB</span>
        <span class="tag-pill">Simulink</span>
      </div>
    </article>

    <article class="home-card">
      <p class="home-card__kicker">Engineering Workflow</p>
      <h3 class="home-card__title">Development and experimentation</h3>
      <div class="tag-list">
        <span class="tag-pill">Python</span>
        <span class="tag-pill">C++</span>
        <span class="tag-pill">C#</span>
        <span class="tag-pill">Linux</span>
        <span class="tag-pill">Docker</span>
        <span class="tag-pill">Jupyter</span>
        <span class="tag-pill">Git</span>
      </div>
    </article>

    <article class="home-card">
      <p class="home-card__kicker">Research Style</p>
      <h3 class="home-card__title">Practical, reproducible, deployment-aware</h3>
      <ul class="home-card__list">
        <li>Problem-driven research tied to real traffic or robotic settings.</li>
        <li>Emphasis on tractable methods, implementation realism, and validation.</li>
        <li>Integration of theory, simulation, datasets, and system-level evaluation.</li>
      </ul>
    </article>
  </div>
</section>

<section class="home-section">
  <div class="home-section__header">
    <div>
      <h2 class="home-section__title">Representative Outputs</h2>
      <p class="home-section__lede">Selected publications that illustrate the breadth of the research program.</p>
    </div>
    <a class="home-section__link" href="/publications/">Full publication list</a>
  </div>

  <div class="home-card-grid">
    <article class="home-card home-card--publication">
      <p class="home-card__kicker">Motion Planning</p>
      <h3 class="home-card__title"><a href="/publication/2025-07-01-online-risk-bounded-local-planning/">Online Risk-Bounded Graph-Based Local Planning for Autonomous Driving with Theoretical Guarantees</a></h3>
      <p>Develops a real-time local planner with explicit risk bounds and theoretical guarantees for autonomous driving.</p>
    </article>

    <article class="home-card home-card--publication">
      <p class="home-card__kicker">Transportation Systems</p>
      <h3 class="home-card__title"><a href="/publication/2025-01-01-multiple-intelligent-control/">Multiple Intelligent Control Strategies for Travel-Time Reduction of Connected Emergency Vehicles</a></h3>
      <p>Presents intelligent control strategies for connected emergency vehicles using path planning and signal intervention.</p>
    </article>

    <article class="home-card home-card--publication">
      <p class="home-card__kicker">Prediction and Survey</p>
      <h3 class="home-card__title"><a href="/publication/2026-01-01-trajectory-prediction/">Trajectory Prediction for Autonomous Driving: Progress, Limitations, and Future Directions</a></h3>
      <p>Surveys recent trajectory-prediction methods and maps the field’s unresolved technical gaps.</p>
    </article>

    <article class="home-card home-card--publication">
      <p class="home-card__kicker">Datasets</p>
      <h3 class="home-card__title"><a href="/publication/2025-02-01-emt-benchmark-dataset/">EMT: A Visual Multi-Task Benchmark Dataset for Autonomous Driving in the Arab Gulf Region</a></h3>
      <p>Introduces a benchmark dataset tailored to multi-task autonomous-driving research and evaluation.</p>
    </article>
  </div>
</section>
