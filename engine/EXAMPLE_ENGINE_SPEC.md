# Example Engine Specification

## Purpose

The Example Engine generates educational examples that reinforce understanding and bridge the gap between theory and practice.

It does not explain concepts from scratch.

Instead, it creates examples that strengthen the explanation produced by the Explanation Engine.

---

# Input

* Teaching Blueprint
* Explanation Output

---

# Output

A collection of educational examples for a single topic.

---

# Responsibilities

The Example Engine must generate:

1. Everyday Example
2. Academic Example
3. Professional / Industry Example
4. Counter Example (when appropriate)
5. Mini Exercise

---

# Processing Logic

For every topic:

Step 1

Read the learner profile.

↓

Step 2

Determine the concept difficulty.

↓

Step 3

Generate an everyday example.

↓

Step 4

Generate an academic example.

↓

Step 5

Generate a professional example.

↓

Step 6

Generate a short learner exercise.

---

# Example Rules

Every example must:

* Explain one specific idea.
* Be realistic.
* Be directly related to the concept.
* Increase intuition.
* Avoid unnecessary complexity.

Examples should become progressively more challenging.

---

# Example Types

## Everyday Example

Use familiar real-life situations.

Example:

Correlation → Height vs Weight

---

## Academic Example

Use educational scenarios related to the subject.

Example:

Statistics → Student Exam Scores

---

## Professional Example

Use real industry applications.

Example:

Machine Learning → Feature Correlation Analysis

---

## Counter Example

When useful, generate an example showing what the concept is NOT.

Example:

Correlation ≠ Causation

---

## Mini Exercise

Create one short question that allows the learner to immediately apply the concept.

The exercise should reinforce understanding rather than test memorization.

---

# Learner Adaptation

## Beginner

* Very simple examples.
* Everyday situations.

---

## Intermediate

* University-level examples.
* Practical reasoning.

---

## Advanced

* Professional datasets.
* Research scenarios.
* Technical applications.

---

# Validation Rules

A valid output must include:

* Everyday Example
* Academic Example
* Professional Example
* Mini Exercise

Counter Example is optional but recommended.

---

# Failure Conditions

Reject the output if:

* Examples are repetitive.
* Examples are unrelated to the concept.
* Examples require unexplained knowledge.
* Examples introduce new concepts without explanation.

---

# Success Criteria

After reading the examples, the learner should be able to recognize the concept in real life, academic study, and professional practice without additional explanation.
