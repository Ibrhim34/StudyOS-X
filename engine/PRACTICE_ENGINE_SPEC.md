# Practice Engine Specification

## Purpose

The Practice Engine generates educational activities that reinforce understanding immediately after learning.

Its purpose is to help the learner actively apply knowledge, identify misconceptions, and strengthen long-term retention.

The engine generates practice based on the Teaching Blueprint, Explanation Output, and Example Output.

---

# Input

* Teaching Blueprint
* Explanation Output
* Example Output

---

# Output

A structured Practice Set for one learning topic.

---

# Responsibilities

The Practice Engine must generate:

1. Knowledge Check
2. Conceptual Questions
3. Application Questions
4. Scenario-Based Questions
5. Reflection Question
6. Challenge Question (Optional)

---

# Processing Logic

For every topic:

Step 1

Analyze the learner profile.

↓

Step 2

Analyze concept importance.

↓

Step 3

Determine appropriate difficulty.

↓

Step 4

Generate progressively difficult activities.

↓

Step 5

Generate answer explanations.

---

# Practice Types

## Knowledge Check

Purpose:

Verify basic understanding.

Examples:

* Multiple Choice
* True / False
* Fill in the Blank

---

## Conceptual Questions

Purpose:

Require the learner to explain ideas using their own understanding.

Avoid memorization.

---

## Application Questions

Purpose:

Apply the concept to realistic situations.

Learners should use reasoning rather than recall.

---

## Scenario-Based Questions

Purpose:

Present a real-world situation.

Require selecting or applying the correct concept.

---

## Reflection Question

Purpose:

Encourage deeper thinking.

Example:

Why is this concept important?

What could happen if it is misunderstood?

---

## Challenge Question

Purpose:

Stretch advanced learners.

May combine multiple concepts.

Optional.

---

# Answer Generation

Every question must include:

* Correct Answer
* Explanation
* Learning Objective

Whenever possible include:

* Why common wrong answers are incorrect.

---

# Learner Adaptation

## Beginner

* Short questions.
* High guidance.
* Simple wording.

---

## Intermediate

* Mixed question types.
* Moderate reasoning.

---

## Advanced

* Complex scenarios.
* Multi-step reasoning.
* Cross-topic integration.

---

# Validation Rules

A valid Practice Set must contain:

* At least one Knowledge Check.
* At least one Conceptual Question.
* At least one Application Question.
* At least one Scenario Question.
* Answer explanations.

---

# Failure Conditions

Reject the Practice Set if:

* Questions only test memorization.
* Questions introduce unexplained concepts.
* Difficulty is inconsistent with the learner profile.
* Answer explanations are missing.

---

# Success Criteria

A learner who completes the Practice Set should demonstrate understanding, application, and reasoning rather than simple recall.
