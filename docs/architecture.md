# Architecture

## Purpose

IA-Productiva is a repository designed to provide a consistent operating framework for any AI capable of generating software, documentation, content or business assets.

The repository is intentionally model-agnostic. Every document, template and prompt must be reusable by ChatGPT, Claude, Gemini, Codex, Cursor, Copilot or future AI systems.

---

# Core Principles

The repository follows seven principles.

## 1. Single Source of Truth

Each concept must exist in only one place.

Documents should reference each other instead of duplicating information.

---

## 2. Modular Design

Every document should be independent.

A prompt should work without requiring unrelated prompts.

Templates should not depend on implementation details.

Processes should be reusable.

---

## 3. Predictability

Given the same context and requirements, every AI should produce similar results.

The repository reduces randomness through:

- conventions
- templates
- checklists
- operating procedures

---

## 4. Scalability

The repository must support:

- small projects
- SaaS
- automation
- documentation
- content production
- internal tools

without structural changes.

---

## 5. Maintainability

Adding knowledge must never require reorganizing the repository.

Growth should happen by adding files, not redesigning folders.

---

## 6. AI First

Every document is written primarily for AI consumption.

Humans are secondary readers.

Documents must therefore be:

- explicit
- deterministic
- structured
- easy to parse

---

## 7. Continuous Improvement

Every project should improve the framework.

Lessons learned become reusable assets.

---

# Repository Layers

## Root

Contains project-wide documentation.

Examples:

- README
- PROJECT
- ROADMAP
- TODO
- CHANGELOG

---

## Docs

Contains operational knowledge.

Examples:

- architecture
- conventions
- behavior
- context
- glossary

---

## Content

Reusable production assets.

Includes:

- prompts
- templates

---

## Resources

Reusable supporting material.

Includes:

- snippets
- checklists

---

## Automation

Everything related to workflows and automation.

---

## Website

Documentation website.

---

## Branding

Visual identity.

---

## Assets

Static resources.

---

## Analytics

Project metrics.

---

## Archive

Historical information.

---

# Information Flow

```
Idea

↓

Documentation

↓

Planning

↓

Prompt

↓

Generation

↓

Review

↓

Delivery

↓

Learning

↓

Repository Update
```

---

# Dependency Rules

High-level documentation must never depend on prompts.

Prompts may depend on:

- documentation
- templates
- conventions

Templates may depend on:

- conventions

Processes may reference:

- templates
- prompts
- documentation

---

# Naming Rules

Folders:

lowercase

Files:

lowercase-with-hyphens.md

No spaces.

No duplicate concepts.

---

# Decision Hierarchy

When conflicts appear:

1. PROJECT_RULES.md
2. architecture.md
3. conventions.md
4. operating-system.md
5. prompts
6. templates

Higher priority always wins.

---

# Evolution Policy

The architecture is expected to grow.

It should never require breaking changes.

New knowledge is incorporated by:

- adding files
- extending documentation
- improving templates

Never by restructuring the repository unnecessarily.