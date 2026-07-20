# Standards

This document defines the standards and conventions adopted across this repository.

These standards aim to provide a consistent, maintainable and reproducible workflow. Unless there is a justified reason, projects created from this template should follow them.

---

# Repository Structure

This repository follows a standardized structure to promote consistency across all projects created from this template.

The template includes:

* Standard documentation
* GitHub Issue Forms
* Pull Request Template
* GitHub configuration
* Common project files
* Repository conventions

---

# Branching Strategy

Branches must follow the naming convention:

```text
<type>/<issue-number>-<short-description>
```

Examples:

```text
feature/3-issue-templates
feature/6-pr-template
bugfix/12-fix-build-error
docs/5-update-readme
research/9-opentelemetry
chore/update-dependencies
```

## Branch Types

| Type       | Purpose                                    |
| ---------- | ------------------------------------------ |
| `feature`  | New functionality or repository capability |
| `bugfix`   | Bug fixes                                  |
| `docs`     | Documentation updates                      |
| `research` | Technical investigation and evaluation     |
| `chore`    | Repository maintenance                     |

### Branch Guidelines

* Branch names must use lowercase letters.
* Words must be separated using hyphens (`-`).
* Branches should be associated with a single Issue whenever possible.
* Branches should be short-lived and deleted after merging.

---

# Commit Convention

This repository follows the Conventional Commits specification.

Examples:

```text
feat: add pull request template
fix: resolve docker build failure
docs: update README
ci: add GitHub Actions workflow
refactor: simplify project structure
```

## Commit Guidelines

* Keep commits small and focused.
* Each commit should represent a single logical change.
* Use the appropriate Conventional Commit type.
* Reference the related Issue when applicable.

---

# Pull Requests

All changes must be integrated through Pull Requests.

Each Pull Request should:

* Reference the related Issue.
* Describe the implemented changes.
* Explain how the changes were validated.
* Complete the Pull Request checklist.

Direct commits to the default branch should be avoided.

---

# Merge Strategy

This repository uses **Squash and Merge**.

The objective is to maintain a clean and readable commit history.

Feature branches should be automatically deleted after merging.

---

# Issue Management

All work should start with an Issue.

The available Issue types are:

* 🚀 Feature
* 🐛 Bug Report
* 📖 Documentation
* 🔬 Research

Each Issue should include clear acceptance criteria before implementation begins.

---

# Versioning Strategy

This repository follows Semantic Versioning.

Examples:

```text
v0.1.0
v0.2.0
v1.0.0
```

Milestones follow the same versioning strategy.

Example:

```text
v0.1.0 - Foundation
```

---

# Repository Settings

The repository uses the following GitHub configuration:

* Issues enabled
* Projects enabled
* Wiki disabled
* Discussions disabled (for now)
* Squash Merge enabled
* Merge Commit disabled
* Rebase Merge disabled
* Automatically delete merged branches

These settings provide a simple and consistent workflow.

---

# General Principles

The standards defined in this document are based on the following principles:

* Keep things simple.
* Prefer consistency over customization.
* Build reusable solutions.
* Automate repetitive tasks whenever possible.
* Document important decisions.
* Continuously improve the workflow.
