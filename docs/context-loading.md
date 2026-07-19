# Context Loading

## Purpose

This document defines how an AI should build its working context before generating any response.

The objective is to minimize inconsistencies and avoid decisions based on incomplete information.

---

# Loading Order

Always load context in this order.

1. PROJECT_RULES.md
2. PROJECT.md
3. SESSION.md
4. ROADMAP.md
5. TODO.md
6. Architecture
7. Relevant documentation
8. Templates
9. Prompts
10. Current task

---

# Context Levels

## Level 1 · Global

Project identity.

Includes:

- objectives
- architecture
- conventions
- rules

Loaded once.

---

## Level 2 · Operational

Current documentation.

Includes:

- processes
- decisions
- glossary
- knowledge

Loaded when required.

---

## Level 3 · Task

Specific information related to the current request.

Examples:

- feature
- prompt
- documentation
- code

---

## Level 4 · Temporary

Short-lived context.

Examples:

- current conversation
- temporary notes
- experiments

Never becomes permanent automatically.

---

# Validation

Before generating any response verify:

- project objective understood
- constraints loaded
- terminology consistent
- required documents available

---

# Missing Context

If essential information is unavailable:

- identify what is missing
- continue only with verified information
- avoid assumptions

---

# Context Priority

When conflicts exist:

1. PROJECT_RULES
2. Architecture
3. Documentation
4. Session
5. Conversation

Higher priority overrides lower priority.

---

# Context Refresh

Reload context whenever:

- project changes
- architecture changes
- major documentation changes
- new requirements appear

---

# Permanent Knowledge

May include:

- accepted decisions
- architecture
- conventions
- reusable assets

---

# Temporary Knowledge

Must not become permanent without review.

Examples:

- ideas
- drafts
- experiments
- hypotheses

---

# Output Verification

Before answering ensure:

- context is sufficient
- terminology matches repository
- response follows conventions
- no conflicting information exists

---

# Goal

Every response should be generated from the minimum required context while remaining fully consistent with the repository.