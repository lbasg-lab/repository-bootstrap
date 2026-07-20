# Architecture

## Purpose

The GitHub Actions repository provides reusable automation that can be shared across the Engineering Lab ecosystem.

Its primary goal is to centralize GitHub Actions workflows and Composite Actions, reducing duplication and promoting consistency across repositories.

All automation published by this repository is versioned and intended to be consumed through GitHub Releases.

---

## Design Goals

The repository is designed around the following goals:

- Maximize reusability.
- Promote consistency across repositories.
- Keep workflows simple and maintainable.
- Encourage composition instead of duplication.
- Deliver reusable automation as versioned products.

---

## Architecture Principles

### Public API First

Reusable Workflows define the public interface of this repository.

Consumers should interact with published workflows instead of internal implementation details.

---

### Composition over Duplication

Complex workflows should be composed from reusable Composite Actions whenever possible.

Reusable logic should exist in a single location.

---

### Stable Public Interface

Reusable Workflows are considered public products.

Their interfaces should remain stable across compatible releases.

---

### Internal Components

Composite Actions encapsulate reusable implementation details.

Unless explicitly documented, Composite Actions are considered internal implementation components and are not part of the public API.

---

### Release-driven Adoption

Repositories should consume only published releases.

Development branches must never be referenced as dependencies.



## Repository Structure

```text
.github/
├── workflows/
│   ├── repository-validation.yml
│   ├── python-ci.yml
│   ├── release.yml
│   └── ...
│
└── actions/
    ├── validate-branch/
    ├── validate-commits/
    ├── validate-pr/
    ├── validate-documentation/
    └── ...
```

- **workflows/** contains the public automation products.
- **actions/** contains reusable internal building blocks.


## Naming Conventions

The repository follows consistent naming conventions to improve discoverability and maintainability.

### Reusable Workflows

Reusable workflows represent the public products of the repository.

Naming rules:

- Use lowercase.
- Separate words with hyphens.
- Use descriptive names based on the capability provided.
- One workflow per product.

Examples:

- repository-validation.yml
- python-ci.yml
- release.yml
- security.yml

### Composite Actions

Composite Actions represent reusable implementation components.

Naming rules:

- Use lowercase.
- Separate words with hyphens.
- Name actions according to the responsibility they implement.

Examples:

- validate-branch
- validate-commits
- validate-pr
- validate-documentation
- setup-python

### Documentation

Documentation files should use lowercase names and descriptive titles.

Examples:

- architecture.md
- standards.md
- roadmap.md



## Public Products

Public products are reusable workflows intended to be consumed by other repositories.

Examples include:

- Repository Validation Workflow
- Python CI Workflow
- Release Workflow
- Security Workflow

Each product is independently versioned through GitHub Releases.

---

## Internal Components

Composite Actions implement reusable pieces of functionality shared by one or more workflows.

They should remain implementation details unless explicitly promoted as public products.

---

## Versioning Strategy

This repository follows Semantic Versioning.

Every published workflow is consumed using a Git tag or Release.

Example:

```yaml
jobs:
  validation:
    uses: <owner>/github-actions/.github/workflows/repository-validation.yml@v1.0.0
```

Development branches such as `main` must never be used by consumers.

---

## Consumption Model

Consumers interact with reusable workflows.

Workflows orchestrate the execution of one or more Composite Actions.

```text
Consumer Repository
        │
        ▼
Repository Validation Workflow
        │
        ├── validate-branch
        ├── validate-commits
        ├── validate-pr
        └── validate-documentation
```

This separation allows internal implementation to evolve without affecting consumers.

---

## Future Evolution

As the Engineering Lab ecosystem grows, additional reusable workflows and Composite Actions will be published.

New automation should follow the architecture principles defined in this document to ensure consistency, maintainability and backward compatibility.