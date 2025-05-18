---
title: "Graph-Based Local Planning with Spatiotemporal Risk Assessment For Risk-Bounded and Prediction-Aware Autonomous Driving"
collection: publications
category: conference
permalink: /publication/2025-01-09-graph-risk-planning
excerpt: "A risk-aware graph-based local planner for autonomous driving that integrates spatiotemporal risk assessment and constrained shortest-path optimization."
date: 2025-01-09
venue: '2024 18th International Conference on Control, Automation, Robotics and Vision (ICARCV), pp. 1–8'
citation: '<b>Abdulrahman Ahmad</b>, Majid Khonji, Ameena Al-Sumaiti, Jorge Dias, Khaled Elbassioni. (2025). "Graph-Based Local Planning with Spatiotemporal Risk Assessment For Risk-Bounded and Prediction-Aware Autonomous Driving." <i>2024 18th International Conference on Control, Automation, Robotics and Vision (ICARCV)</i>, IEEE, pp. 1–8.'
rank: B  # Update based on conference ranking if known
graphical_abstract: /images/publications/graph-risk-planning.jpg
---

This paper addresses the challenge of risk-bounded motion planning for autonomous driving in dynamic environments. Ensuring continuous, real-time decision-making in nonconvex settings is difficult due to static and dynamic obstacles, traffic constraints, and user-specific risk tolerances.

We propose a **graph-based local planning method** using a lattice graph that respects vehicle curvature constraints. Trajectory planning is formulated as an integer linear program with a custom **risk-bounded and prediction-aware shortest path** algorithm.

At the core of our system is a **spatiotemporal risk assessment module** that conservatively evaluates collision risk with both static and moving objects. The planner successfully operates in urban driving scenarios while honoring safety margins and driving preferences.

<img src="/images/publications/graph-risk-planning.jpg" alt="Graphical Abstract" width="600" style="border-radius: 8px;" />
