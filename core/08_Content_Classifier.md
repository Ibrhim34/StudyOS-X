# StudyOS X Content Classifier

## Mission

The Content Classifier identifies the educational role of every piece of information before knowledge extraction begins.

Not every sentence has the same value.

The classifier assigns a category to every content block.

---

# Why Classification Matters

A textbook contains different types of content.

Examples:

- Core concepts
- Definitions
- Examples
- Exercises
- Historical notes
- Images
- Tables
- Tips
- Warnings

The engine must treat each type differently.

---

# Content Categories

## Core Concept

The main learning idea.

Highest priority.

---

## Definition

Official academic definition.

Must always be preserved.

---

## Formula

Mathematical expression.

Must never be modified.

---

## Example

Clarifies understanding.

Can be improved but not removed.

---

## Exercise

Student practice.

Used later by the Question Generator.

---

## Diagram

Visual explanation.

Referenced by the Visual Organizer.

---

## Table

Structured information.

May be redesigned for better readability.

---

## Note

Supporting information.

Included only if it improves understanding.

---

## Warning

Common mistakes or important cautions.

Must be highlighted.

---

# Output

The classifier produces a structured content inventory.

Every content block is tagged with its educational role before knowledge extraction starts.

---

# Design Principle

Classification happens before understanding.

Extraction happens after classification.

This separation improves consistency and future scalability.
