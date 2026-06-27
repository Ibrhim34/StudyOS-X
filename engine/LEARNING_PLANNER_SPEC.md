# Learning Planner Specification

## Purpose

The Learning Planner Engine transforms the Knowledge Graph into an optimized educational roadmap.

Its goal is to determine **how the student should learn**, not simply **what exists in the document**.

---

# Input

* Knowledge Graph

---

# Output

```yaml
learning_plan:

  chapters:

    - id:
      title:

      topics:

        - id:
          concept:
          order:
          prerequisites:
          estimated_time:
          difficulty:
          learning_goal:

review_points:

practice_points:

visual_points:
```

---

# Responsibilities

The Learning Planner must:

* Build the optimal learning order.
* Respect prerequisite dependencies.
* Group related concepts.
* Separate independent concepts.
* Identify review checkpoints.
* Identify practice checkpoints.
* Estimate study time.
* Balance cognitive load.

---

# Learning Rules

The planner must always:

* Teach prerequisites first.
* Introduce simple ideas before complex ones.
* Group related concepts together.
* Delay advanced material until the learner is ready.

Never follow the PDF page order blindly.

---

# Topic Planning

Every topic must contain:

* Learning Goal
* Required Prerequisites
* Estimated Difficulty
* Estimated Study Time
* Suggested Example Type
* Suggested Visual Type

---

# Cognitive Load Rules

Avoid introducing:

* Multiple abstract concepts at once.
* Multiple formulas before intuition.
* Advanced terminology before definitions.

Learning should feel progressive.

---

# Review Planning

Automatically insert review points after major concept groups.

Each review should reinforce understanding before introducing new material.

---

# Practice Planning

Insert practice sessions whenever:

* A major concept is completed.
* A mathematical idea is introduced.
* A procedural skill is explained.

Practice should immediately follow learning.

---

# Visual Planning

The planner should recommend visuals such as:

* Comparison Tables
* Flowcharts
* Timelines
* Concept Maps
* Process Diagrams

Visuals should be selected based on educational value.

---

# Validation Rules

A valid Learning Plan must satisfy:

* Every topic has a learning goal.
* Every topic has prerequisites.
* Every topic belongs to a chapter.
* Review points exist.
* Practice points exist.
* Learning order respects dependencies.

---

# Success Criteria

The generated Learning Plan should minimize confusion, reduce cognitive load, and maximize long-term understanding.

The planner should produce the order a great teacher would naturally follow.
