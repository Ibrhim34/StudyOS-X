# Visual Engine Specification

## Purpose

The Visual Engine determines the most effective visual representation for each learning topic.

Its purpose is not to create beautiful graphics.

Its purpose is to improve understanding by selecting the best visual teaching method.

The engine recommends visuals based on educational value.

---

# Input

* Teaching Blueprint
* Knowledge Graph
* Explanation Output

---

# Output

A structured Visual Plan for each topic.

---

# Responsibilities

The Visual Engine must:

1. Analyze the concept type.
2. Determine whether a visual is beneficial.
3. Select the most effective visual format.
4. Generate instructions for creating the visual.
5. Connect the visual directly to the explanation.

---

# Supported Visual Types

## Concept Map

Use when explaining relationships between concepts.

Example:

Machine Learning

↓

Supervised Learning

↓

Regression

↓

Linear Regression

---

## Flowchart

Use when explaining:

* Processes
* Algorithms
* Decision Making
* Pipelines

---

## Comparison Table

Use when comparing:

* Two concepts
* Methods
* Algorithms
* Definitions

---

## Timeline

Use when explaining:

* Historical development
* Sequential events
* Learning progression

---

## Hierarchy Diagram

Use for:

* Categories
* Taxonomies
* Parent-child relationships

---

## Process Diagram

Use when showing:

Input

↓

Processing

↓

Output

---

## Mathematical Visualization

Use for:

* Equations
* Statistical relationships
* Geometric intuition
* Graphs

---

# Visual Selection Rules

Choose exactly one primary visual.

A secondary visual is optional.

Selection should maximize understanding.

Never choose visuals based on aesthetics.

---

# Visual Planning

Every visual should include:

* Visual Type
* Educational Objective
* Related Concepts
* Placement
* Caption
* Explanation Reference

---

# Learner Adaptation

## Beginner

Prefer:

* Diagrams
* Flowcharts
* Simple Tables

Avoid:

* Dense Graphs

---

## Intermediate

Prefer:

* Concept Maps
* Comparison Tables
* Process Diagrams

---

## Advanced

Allow:

* Mathematical Graphs
* Technical Diagrams
* Multi-layer Concept Maps

---

# Validation Rules

A valid visual plan must:

* Match the concept.
* Improve understanding.
* Avoid unnecessary complexity.
* Reference the explanation.
* Be understandable independently.

---

# Failure Conditions

Reject the visual if:

* It duplicates the explanation.
* It introduces new concepts.
* It is visually complex without educational benefit.
* It cannot be interpreted without external information.

---

# Success Criteria

The learner should understand the concept faster with the visual than without it.

The visual should reduce cognitive load rather than increase it.
