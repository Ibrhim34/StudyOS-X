# Knowledge Graph Specification

## Purpose

The Knowledge Extraction Engine transforms the **Document Blueprint** into a structured **Knowledge Graph**.

The Knowledge Graph represents the educational understanding of the document.

All downstream engines must use this Knowledge Graph instead of extracting knowledge directly from the document.

---

# Input

* Document Blueprint

---

# Output

```yaml
knowledge_graph:
  concepts:
    - id:
      name:
      type:
      importance:
      difficulty:

  relationships:
    - source:
      target:
      relation:

  definitions:

  formulas:

  algorithms:

  examples:

  applications:

  misconceptions:

  prerequisites:

  learning_sequence:
```

---

# Responsibilities

The Knowledge Extraction Engine must:

* Extract all educational concepts.
* Detect formal definitions.
* Detect mathematical formulas.
* Detect algorithms and procedures.
* Detect practical examples.
* Detect real-world applications.
* Detect prerequisite concepts.
* Detect common misconceptions.
* Build relationships between concepts.
* Generate the optimal learning order.

---

# Concept Model

Every concept must contain:

```yaml
concept:
  id:
  name:
  type:
  importance:
  difficulty:
  prerequisites:
```

---

# Concept Types

Allowed concept types:

* Concept
* Definition
* Formula
* Algorithm
* Principle
* Rule
* Process
* Example
* Application

---

# Importance Levels

Each concept must be classified as one of:

* Critical
* Important
* Supporting

---

# Difficulty Levels

Each concept must be classified as:

* Beginner
* Intermediate
* Advanced

---

# Relationship Types

Allowed relationships:

* depends_on
* part_of
* used_for
* derived_from
* compares_with
* requires
* extends
* causes

Every relationship should connect exactly two concepts.

---

# Learning Sequence

The engine must produce a dependency-aware learning sequence.

The order should maximize understanding rather than follow the PDF layout.

---

# Validation Rules

A valid Knowledge Graph must satisfy:

* Every concept has a unique ID.
* Every concept has a name.
* Every concept has a type.
* Every concept has an importance level.
* Every concept has a difficulty level.
* Every concept has at least one relationship unless it is a root concept.
* Circular prerequisite chains are not allowed.

---

# Design Rules

* Never explain concepts.
* Never generate educational notes.
* Never summarize paragraphs.
* Focus only on extracting structured knowledge.
* Preserve logical relationships.
* Preserve educational dependencies.

---

# Success Criteria

A downstream engine should be able to generate complete educational material using only the Knowledge Graph, without reopening the original PDF.
