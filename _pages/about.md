---
permalink: /
title: "Abdulrahman Ahmad"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

{% assign journal_count = site.publications | where: "category", "manuscripts" | size %}
{% assign conference_count = site.publications | where: "category", "conference" | size %}
{% assign publication_count = site.publications | size %}

<section class="home-hero">
  <div class="home-hero__content">
    <p class="home-hero__eyebrow">Computer Science Ph.D. Candidate | Khalifa University</p>
    <h2 class="home-hero__title">Building risk-aware autonomy for intelligent transportation systems</h2>
    <p class="home-hero__lead">I am Abdulrahman Ahmad, a final-year Ph.D. candidate in Computer Science working at the intersection of autonomous driving, motion planning under uncertainty, intelligent transportation systems, and data-driven perception. My research focuses on decision-making and control methods that remain safe, tractable, and deployable in real traffic environments.</p>
    <div class="home-hero__actions">
      <a class="btn btn--primary" href="/files/cv.pdf">Download CV</a>
      <a class="btn btn--inverse" href="/publications/">View Publications</a>
      <a class="btn btn--inverse" href="https://scholar.google.com/citations?user=-yqOHxIAAAAJ&hl=en">Google Scholar</a>
      <a class="btn btn--inverse" href="mailto:abdulrahman_hamdy@ieee.org">Email</a>
    </div>
  </div>

  <aside class="home-hero__panel">
    <p class="home-hero__panel-label">Current profile</p>
    <ul class="home-hero__facts">
      <li><strong>Position:</strong> Final-year Ph.D. candidate and Graduate Research and Teaching Assistant at Khalifa University.</li>
      <li><strong>Dissertation:</strong> Online risk-bounded motion planning for autonomous driving under uncertainty.</li>
      <li><strong>Expected graduation:</strong> December 2026.</li>
      <li><strong>Research settings:</strong> Autonomous Vehicles Lab, operations research, robotics, and intelligent transportation systems.</li>
    </ul>
  </aside>
</section>

<section class="home-stat-grid" aria-label="Professional summary">
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
  <div class="home-stat">
    <span class="home-stat__value">2019</span>
    <span class="home-stat__label">Teaching Since</span>
  </div>
</section>

<section class="home-section">
  <div class="home-section__header">
    <div>
      <h2 class="home-section__title">Research Focus</h2>
      <p class="home-section__lede">My work connects optimization, control, and learning for safer and more efficient autonomous systems. Each area below links to a dedicated project page.</p>
    </div>
    <a class="home-section__link" href="/projects/">Projects page</a>
  </div>

  <div class="home-card-grid">
    <article class="home-card">
      <p class="home-card__kicker">Autonomous Driving</p>
      <h3 class="home-card__title"><a href="/projects/risk-aware-autonomous-driving/">Risk-aware motion planning and control</a></h3>
      <p>I develop local planning and control methods that account for uncertainty, spatiotemporal risk, and real-time decision constraints in mixed urban traffic.</p>
      <p class="home-card__meta">Planning, online optimization, theoretical guarantees, mixed traffic</p>
    </article>

    <article class="home-card">
      <p class="home-card__kicker">Transportation Systems</p>
      <h3 class="home-card__title"><a href="/projects/intelligent-transportation-systems/">Signal control, eco-driving, and emergency prioritization</a></h3>
      <p>I study how connected and autonomous vehicles can improve traffic efficiency through signal-aware control, network-level coordination, and emergency-vehicle prioritization.</p>
      <p class="home-card__meta">ITS, travel-time reduction, energy efficiency, connected mobility</p>
    </article>

    <article class="home-card">
      <p class="home-card__kicker">Learning and Control</p>
      <h3 class="home-card__title"><a href="/projects/learning-based-control-and-optimization/">Interaction-aware and learning-based autonomy</a></h3>
      <p>My research combines reinforcement learning with classical control and optimization to design robust controllers for challenging autonomous systems.</p>
      <p class="home-card__meta">Reinforcement learning, active suspension, robotics, optimal control</p>
    </article>

    <article class="home-card">
      <p class="home-card__kicker">Perception and Data</p>
      <h3 class="home-card__title"><a href="/projects/trajectory-prediction-and-datasets/">Trajectory prediction and benchmark datasets</a></h3>
      <p>I contribute to trajectory-prediction surveys, dataset design, anonymization tooling, and data-driven benchmarks that support real-world autonomous-driving research.</p>
      <p class="home-card__meta">Prediction, datasets, scene understanding, reproducible research</p>
    </article>
  </div>
</section>

<section class="home-section">
  <div class="home-section__header">
    <div>
      <h2 class="home-section__title">Selected Publications</h2>
      <p class="home-section__lede">Representative work across motion planning, transportation systems, and perception for autonomous driving.</p>
    </div>
    <a class="home-section__link" href="/publications/">Full publication list</a>
  </div>

  <div class="home-card-grid">
    <article class="home-card home-card--publication">
      <p class="home-card__kicker">ICRA 2025</p>
      <h3 class="home-card__title"><a href="/publication/2025-07-01-online-risk-bounded-local-planning/">Online Risk-Bounded Graph-Based Local Planning for Autonomous Driving with Theoretical Guarantees</a></h3>
      <p>Introduces an online graph-based local planner with explicit risk bounds for autonomous driving in uncertain traffic environments.</p>
    </article>

    <article class="home-card home-card--publication">
      <p class="home-card__kicker">Information Fusion</p>
      <h3 class="home-card__title"><a href="/publication/2026-01-01-trajectory-prediction/">Trajectory Prediction for Autonomous Driving: Progress, Limitations, and Future Directions</a></h3>
      <p>Surveys the trajectory-prediction landscape, identifies major limitations, and outlines open directions for robust real-world forecasting.</p>
    </article>

    <article class="home-card home-card--publication">
      <p class="home-card__kicker">IEEE T-ITS</p>
      <h3 class="home-card__title"><a href="/publication/2025-01-01-multiple-intelligent-control/">Multiple Intelligent Control Strategies for Travel-Time Reduction of Connected Emergency Vehicles</a></h3>
      <p>Develops intelligent control strategies for connected emergency vehicles to reduce travel time and improve network responsiveness.</p>
    </article>

    <article class="home-card home-card--publication">
      <p class="home-card__kicker">Dataset and Benchmarking</p>
      <h3 class="home-card__title"><a href="/publication/2025-02-01-emt-benchmark-dataset/">EMT: A Visual Multi-Task Benchmark Dataset for Autonomous Driving in the Arab Gulf Region</a></h3>
      <p>Presents a benchmark dataset tailored to multiple perception and scene-understanding tasks for autonomous driving research.</p>
    </article>
  </div>
</section>

<section class="home-section">
  <div class="home-section__header">
    <div>
      <h2 class="home-section__title">Recent Updates</h2>
      <p class="home-section__lede">Selected recent publications, datasets, and research milestones.</p>
    </div>
    <a class="home-section__link" href="/updates/">All updates</a>
  </div>

  <div class="updates-feed updates-feed--compact">
    {% for item in site.data.updates limit: 4 %}
      <article class="update-card">
        <div class="update-card__meta">
          <span class="update-card__type">{{ item.type }}</span>
          <time datetime="{{ item.date }}">{{ item.date | date: "%B %d, %Y" }}</time>
        </div>
        <h3 class="update-card__title">
          {% if item.link %}
            <a href="{{ item.link }}">{{ item.title }}</a>
          {% else %}
            {{ item.title }}
          {% endif %}
        </h3>
        <p class="update-card__summary">{{ item.summary }}</p>
      </article>
    {% endfor %}
  </div>
</section>

<section class="home-section">
  <div class="home-section__header">
    <div>
      <h2 class="home-section__title">Academic Profile</h2>
      <p class="home-section__lede">A concise overview of current roles, recognition, and research infrastructure.</p>
    </div>
  </div>

  <div class="home-card-grid">
    <article class="home-card">
      <p class="home-card__kicker">Current Roles</p>
      <h3 class="home-card__title">Research and academic appointments</h3>
      <ul class="home-card__list">
        <li>Graduate Research and Teaching Assistant at Khalifa University since 2021.</li>
        <li>Researcher in the Autonomous Vehicles Lab and former researcher in the Operations Research Lab.</li>
        <li>Teaching experience across programming, data science, control, algorithms, and robotics.</li>
      </ul>
    </article>

    <article class="home-card">
      <p class="home-card__kicker">Recognition</p>
      <h3 class="home-card__title">Awards and academic distinction</h3>
      <ul class="home-card__list">
        <li>Elite Young Researcher, Khalifa University, 2023-2024.</li>
        <li>Recognized as a Future Expert on the UAE Research Map national platform in 2026.</li>
        <li>M.Sc. in Electrical Engineering and Computer Science from Khalifa University with a CGPA of 4.0/4.0.</li>
      </ul>
    </article>

    <article class="home-card">
      <p class="home-card__kicker">Service</p>
      <h3 class="home-card__title">Peer review and community contribution</h3>
      <ul class="home-card__list">
        <li>Reviewer for IEEE Transactions on Intelligent Transportation Systems and IEEE Transactions on Industry Applications.</li>
        <li>Reviewer for IEEE Access, ICRA, IROS, and ICARCV.</li>
        <li>Educational outreach through the khawarizmiat YouTube channel and course playlists.</li>
      </ul>
    </article>

    <article class="home-card">
      <p class="home-card__kicker">Toolchain</p>
      <h3 class="home-card__title">Research platforms and engineering stack</h3>
      <ul class="home-card__list">
        <li>CARLA, ROS 2, NAV2, RViz2, Foxglove, Autoware, CommonRoad, RoadRunner.</li>
        <li>PTV Vissim, SUMO, MATLAB, Simulink, Jupyter, Docker, and Linux.</li>
        <li>Primary development in Python, C++, C#, MATLAB, and Git-based workflows.</li>
      </ul>
    </article>
  </div>
</section>

<section class="home-section home-section--compact">
  <div class="home-section__header">
    <div>
      <h2 class="home-section__title">Profiles and Contact</h2>
      <p class="home-section__lede">Additional academic profiles and direct contact information.</p>
    </div>
  </div>

  <div class="home-inline-links">
    <a href="mailto:abdulrahman_hamdy@ieee.org">Email</a>
    <a href="https://scholar.google.com/citations?user=-yqOHxIAAAAJ&hl=en">Google Scholar</a>
    <a href="https://orcid.org/0000-0002-1067-9745">ORCID</a>
    <a href="https://www.scopus.com/authid/detail.uri?authorId=58278769900">Scopus</a>
    <a href="https://github.com/abdohamdy7">GitHub</a>
    <a href="https://www.linkedin.com/in/abdurrahmanhamdy">LinkedIn</a>
  </div>
</section>
