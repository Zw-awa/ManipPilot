# Contributing To ManipPilot

[English](./CONTRIBUTING.md) | [简体中文](./CONTRIBUTING.zh-CN.md) | [繁體中文](./CONTRIBUTING.zh-TW.md)

Thanks for considering a contribution.
ManipPilot is an early-stage robotics task-execution project, so useful contributions are not limited to code.

We welcome improvements in:

- documentation
- examples and task descriptions
- `ROS 2` integration
- manipulation workflow usability
- replay and debugging experience
- testing, safety, and reproducibility
- repository and contributor tooling

## Before You Start

For large changes, please open an issue first.
The project is still defining its first reproducible baseline, so early discussion helps avoid drift in scope, behavior promises, or safety assumptions.

Useful starting points:

- [`README.md`](./README.md)
- [`SUPPORT.md`](./SUPPORT.md)

## Contribution Principles

Contributions should try to improve at least one of these dimensions:

- clarity
- reproducibility
- safety
- maintainability
- evidence-backed performance

Please avoid changes that add complexity without making the system easier to understand, validate, or extend.

## Expected Pull Request Quality

### Documentation Changes

For docs-focused changes, explain:

- what was unclear or missing
- what was changed
- whether links, diagrams, screenshots, or wording also need follow-up

### Hardware Or Electronics Changes

If a change affects physical robot use, include:

- the affected robot or execution setup
- what user-visible behavior changes
- any assumptions that changed
- whether operator safety guidance also needs updates

### Robotics, AI, Or Software Changes

For code or behavior changes, include:

- what behavior changed
- how it was validated
- what hardware, software, or environment assumptions were made
- whether logs, tests, or documentation should also change

## Safety And Scope

This project is intended to support real manipulation workflows.
If your change affects motion behavior, collision assumptions, gripping behavior, execution retries, recovery logic, or operator safety, call that out explicitly in the pull request.

Do not silently change:

- baseline deployment assumptions
- task definition
- safety-related defaults
- subsystem responsibility boundaries

## Style Expectations

- Prefer clear, direct writing over marketing language.
- Keep docs understandable to contributors who are strong in only one area.
- Favor incremental changes over large speculative rewrites.
- Add rationale when a decision is not obvious from the diff itself.

## Questions And Support

If you are not sure where to start, open a `Question / Support` issue and describe:

- which area you want to help with
- what context you already have
- what is blocking you

## License

By contributing to this repository, you agree that your contributions will be licensed under the Apache License 2.0 included in this repository.
