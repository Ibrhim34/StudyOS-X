# Summary Engine Specification

## Purpose

The Summary Engine consolidates all generated educational content into concise, high-value learning summaries.

Its objective is to reinforce understanding, improve long-term retention, and support efficient revision.

The Summary Engine operates only after the Explanation, Example, Visual, and Practice Engines have completed their outputs.

---

# Input

* Teaching Blueprint
* Explanation Output
* Example Output
* Visual Plan
* Practice Output

---

# Output

A structured revision package for one learning topic.

---

# Responsibilities

The Summary Engine must generate:

1. Key Takeaways
2. Concept Summary
3. Formula Summary (if applicable)
4. Common Mistakes Recap
5. Visual Recap
6. Quick Revision Sheet
7. Memory Aids (when appropriate)
8. Next Topic Preview

---

# Processing Logic

For every topic:

Step 1

Collect outputs from all previous engines.

↓

Step 2

Extract only the essential learning points.

↓

Step 3

Remove redundancy.

↓

Step 4

Generate concise revision material.

↓

Step 5

Prepare the learner for the next topic.

---

# Summary Rules

Always:

* Preserve meaning.
* Keep summaries concise.
* Highlight critical concepts.
* Emphasize understanding over memorization.
* Maintain consistency with the explanation.

Never:

* Introduce new information.
* Change terminology.
* Omit critical concepts.
* Contradict previous engines.

---

# Output Structure

Every summary must include:

## Key Takeaways

The 3–7 most important ideas.

---

## Concept Summary

A concise explanation of the topic.

---

## Formula Summary

Include only formulas introduced in the topic.

Skip this section if not applicable.

---

## Common Mistakes

Highlight misconceptions that learners should avoid.

---

## Quick Revision Sheet

A one-minute review of the topic.

---

## Next Topic Preview

Explain how the next topic builds on the current one.

---

# Learner Adaptation

## Beginner

* Plain language.
* Short bullet points.
* Simple reminders.

---

## Intermediate

* Academic terminology.
* Moderate detail.

---

## Advanced

* Compact technical summaries.
* Emphasis on relationships and edge cases.

---

# Validation Rules

A valid summary must:

* Match the explanation.
* Contain no new concepts.
* Preserve all critical learning objectives.
* Be understandable independently.

---

# Failure Conditions

Reject the summary if:

* Important concepts are missing.
* New concepts are introduced.
* Terminology is inconsistent.
* The summary is longer than the explanation.

---

# Success Criteria

A learner should be able to revise the topic efficiently using only the generated summary without losing the essential understanding developed throughout the lesson.
