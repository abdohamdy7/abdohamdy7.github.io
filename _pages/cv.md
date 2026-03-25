---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

<p>
  <span class="btn btn--primary btn--disabled" aria-disabled="true">PDF Download Temporarily Unavailable</span>
  <a class="btn btn--inverse" href="https://scholar.google.com/citations?user=-yqOHxIAAAAJ&hl=en">Google Scholar</a>
</p>

<p><em>The PDF version is temporarily unavailable while the CV is being updated.</em></p>

## Research Summary

Ph.D. candidate in Computer Science at Khalifa University, expected to graduate in December 2026. My research focuses on autonomous driving, intelligent transportation systems, and risk-aware decision-making under uncertainty. I work across motion planning, online optimization, combinatorial optimization, reinforcement learning, control, trajectory prediction, and data-driven scene understanding.

## Education

### Ph.D. in Computer Science, Khalifa University, Abu Dhabi, United Arab Emirates
2023-2026 (expected)

- Thesis: Online risk-bounded motion planning for autonomous driving under uncertainty.
- Coursework completed with a CGPA of 3.75/4.0.

### M.Sc. in Electrical Engineering and Computer Science, Khalifa University, Abu Dhabi, United Arab Emirates
2021-2022

- Thesis: Enhancing Internet of Things strategies for autonomous electric vehicles with existing transportation infrastructure and road users.
- Graduated with a CGPA of 4.0/4.0.

### B.Eng. in Computers and Systems Engineering, Minya University, Minya, Egypt
2012-2016

- Graduation project in industrial Internet-of-Things control of a lab-scale process.
- Graduated with a CGPA of 3.2/4.0 and grade of Excellent in the graduation project.

## Academic Appointments

### Graduate Research and Teaching Assistant, Khalifa University
2021-present

- Researcher in the Operations Research Lab and Autonomous Vehicles Lab.
- Worked on autonomous driving, traffic simulation, emergency-vehicle prioritization, and full-stack autonomy development.
- Assisted in teaching programming, data science, algorithms, and robotics courses.

### Graduate Research and Teaching Assistant, Minya University
2019-2020

- Conducted research in formal methods for mobile robots, symbolic control, and hybrid systems.
- Assisted in teaching mathematics, control, and programming courses.

### Programming Instructor, Egypt
2018-2021

- Designed and delivered programming and robotics courses for undergraduate students and professionals.

### Reserved Officer, Egyptian Army
2017-2019

- Participated in software engineering and embedded-systems development projects in addition to military duties.

### Embedded Systems Engineer Intern, Alfagr Advanced Systems
May 2015-August 2015

- Contributed to embedded systems development, RTOS integration, technical documentation, and Android application support.

## Publications

### Journal Articles

<ul>{% assign journal_pubs = site.publications | where: "category", "manuscripts" | sort: "date" | reverse %}
{% for post in journal_pubs %}
  {% include archive-single-cv.html %}
{% endfor %}</ul>

### Conference Papers

<ul>{% assign conference_pubs = site.publications | where: "category", "conference" | sort: "date" | reverse %}
{% for post in conference_pubs %}
  {% include archive-single-cv.html %}
{% endfor %}</ul>

### Theses

<ul>{% assign thesis_pubs = site.publications | where: "category", "thesis" | sort: "date" | reverse %}
{% for post in thesis_pubs %}
  {% include archive-single-cv.html %}
{% endfor %}</ul>

## Teaching

- Khalifa University: Python Programming, MATLAB Programming, Data Analytics, Data Science with AI, Data Structures, Algorithm Design and Analysis, Motion Planning Algorithms for Robotics.
- Minya University: Discrete Mathematics, Signals and Systems, Intelligent Control, C Programming, Computer-Controlled Systems.
- Co-advised undergraduate senior design teams in robotics and IoT.

## Honors and Awards

- 2026: Recognized as a Future Expert on the UAE Research Map national platform.
- 2025: Certificate of recognition for serving as a referee at RoboCup Asia-Pacific.
- 2023-2024: Elite Young Researcher, Khalifa University.
- 2024-2034: UAE Golden Visa for outstanding academic and research contributions.
- 2016: Graduation project funding prize from ITIDA, Egypt.

## Service and Reviewing

- Journal reviewer: IEEE Transactions on Intelligent Transportation Systems, IEEE Transactions on Industry Applications, IEEE Access.
- Conference reviewer: ICRA, IROS, ICARCV.

## Skills

- Programming: Python, C++, C#, MATLAB, LaTeX.
- Robotics and autonomy: ROS 2, NAV2, CARLA, RViz2, Autoware, CommonRoad, RoadRunner.
- Transportation and simulation: PTV Vissim, SUMO.
- Development tools: Linux, Docker, Jupyter, VS Code, Git, GitHub.

## Languages

- Arabic: native
- English: professional working proficiency
