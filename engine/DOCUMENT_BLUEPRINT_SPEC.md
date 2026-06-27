# Document Blueprint Specification

## Purpose

The Document Analysis Engine is responsible for analyzing the input document and producing a structured **Document Blueprint**.

The Blueprint is the single source of truth for all downstream engines.

After this stage, no other engine should read the original PDF directly.

---

# Input

* PDF Document

---

# Output

A structured Document Blueprint.

```yaml
document:
  title:
  subject:
  academic_field:
  language:

learner:
  level:
  goal:

structure:
  chapters:
  sections:
  estimated_topics:

difficulty:
  beginner: false
  intermediate: true
  advanced: false

content_type:
  theoretical:
  mathematical:
  practical:
  programming:
  mixed:

knowledge:
  definitions:
  formulas:
  algorithms:
  concepts:
  examples:
  diagrams:

dependencies:
  prerequisites:
  recommended_order:

generation:
  visual_priority:
  example_priority:
  practice_priority:
```

---

# Responsibilities

The Document Analysis Engine must:

* Detect the document title.
* Detect the subject.
* Detect the academic field.
* Detect the document language.
* Identify chapters and sections.
* Estimate the number of learning topics.
* Detect the overall difficulty level.
* Detect the document type.
* Identify educational elements such as:

  * Definitions
  * Concepts
  * Formulas
  * Algorithms
  * Examples
  * Diagrams
  * Tables
* Detect prerequisite knowledge.
* Recommend the optimal learning order.
* Determine whether the generated notes should emphasize:

  * Visual learning
  * Practical exercises
  * Theoretical explanations

---

# Validation Rules

The Blueprint is considered valid only if it contains:

* Subject
* Structure
* Difficulty
* Content Type
* Knowledge Summary

If any of these are missing, the pipeline must stop and report an error.

---

# Design Rules

* Read the PDF only once.
* Never summarize the content.
* Never explain concepts.
* Never generate notes.
* Produce metadata only.
* All downstream engines must consume the Blueprint instead of the original PDF.

---

# Success Criteria

A valid Blueprint should provide every downstream engine with enough structured information to generate educational content without reopening the original document.
