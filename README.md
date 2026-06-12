# ManipPilot

[English](./README.md) | [简体中文](./README.zh-CN.md) | [繁體中文](./README.zh-TW.md)

[![Status](https://img.shields.io/badge/status-planning%20%2F%20prototyping-4c8bf5)](#current-status)
[![License](https://img.shields.io/badge/license-Apache--2.0-1976d2)](./LICENSE)
![Tasking](https://img.shields.io/badge/tasking-declarative-2e7d32)
![Middleware](https://img.shields.io/badge/middleware-ROS%202-1565c0)
![Manipulation](https://img.shields.io/badge/manipulation-task%20executive-f57c00)

ManipPilot is a declarative task executive for `ROS 2` manipulation that turns one-off robot scripts into installable, reusable, replayable, and recoverable workflows.

## Table Of Contents

- [ManipPilot](#manippilot)
  - [Table Of Contents](#table-of-contents)
  - [What This Project Is](#what-this-project-is)
  - [What It Tries To Do](#what-it-tries-to-do)
  - [What This First Version Focuses On](#what-this-first-version-focuses-on)
  - [Current Status](#current-status)
  - [Repository Structure](#repository-structure)
  - [Quick Start](#quick-start)
    - [1. Clone The Repository](#1-clone-the-repository)
    - [2. Read The Overview](#2-read-the-overview)
    - [3. Follow The Documentation](#3-follow-the-documentation)
    - [4. If You Want To Contribute](#4-if-you-want-to-contribute)
  - [Contributing](#contributing)
  - [Safety Note](#safety-note)
  - [License](#license)

## What This Project Is

This repository is the home of the `ManipPilot` project.

ManipPilot is intended to make robot task execution easier to install, reuse, replay, and recover across supported `ROS 2` manipulation workflows.

The project is aimed at developers who already have, or plan to build, a manipulation stack and want a more structured way to run tasks than ad-hoc scripts.

ManipPilot is organized around:

- declarative task descriptions
- reusable execution flows for manipulation tasks
- replayable run history for debugging and review
- recoverable task behavior instead of one-shot scripts
- a workflow that can be installed and operated with clear inputs and outputs

The `README` files describe the project scope, usage direction, and contribution entry points.

## What It Tries To Do

ManipPilot is aimed at a practical execution workflow:

- define a manipulation task in a structured form
- execute that task through a supported `ROS 2` manipulation stack
- make the run observable and easier to review afterward
- allow recovery behavior when a task step fails
- help users move from fragile one-off scripts toward repeatable workflows

Typical examples include:

- picking an object from a known workspace
- placing it at a target location
- running a multi-step tabletop manipulation sequence
- retrying or aborting cleanly when the task cannot continue
- replaying a previous run for debugging or operator review

## What This First Version Focuses On

The first version is intentionally narrow.
It is mainly focused on:

- one `ROS 2` manipulation-oriented execution path
- one command-line-first user workflow
- one replayable run model for task review
- one recoverable task model for supported failures
- one first supported scenario centered on tabletop manipulators

That also means the first version is intentionally not trying to do everything at once.
For now, it does not aim to cover:

- every possible robot morphology
- broad autonomous perception claims
- unrestricted natural-language interaction
- every planning style or orchestration model at once
- broad support promises before the first reproducible baseline is stable

The first supported scenario is tabletop manipulation, but the project identity is not limited to tabletop-only usage.

## Current Status

`Planning / prototyping`

Right now the repository is focused on:

- project identity
- documentation
- contribution workflow
- support and security entry points
- early repository structure

Concrete capabilities will be added incrementally as the project moves from planning into a reproducible first baseline.

## Repository Structure

```text
.
|-- src/                      # ROS 2 workspace packages
|   |-- manippilot_msgs/      # Message, service, and action definitions
|   |-- manippilot_core/      # Shared execution domain and core logic
|   |-- manippilot_bt/        # Behavior tree nodes and tree assets
|   |-- manippilot_executor/  # Task executor runtime package
|   |-- manippilot_bringup/   # Launch files and runtime configuration
|   |-- manippilot_cli/       # Command-line entry package
|   `-- manippilot_examples/  # Demo tasks and example scenarios
|-- tools/                    # Repo-local helper tools and scripts
|-- tests/                    # Workspace-level integration and replay tests
|-- docs/                     # Project documentation
|-- .github/                  # Issue templates, PR template, CI workflows
|-- README.md                 # English overview
|-- README.zh-CN.md           # Simplified Chinese overview
|-- README.zh-TW.md           # Traditional Chinese overview
|-- CONTRIBUTING.md
|-- CODE_OF_CONDUCT.md
|-- SECURITY.md
|-- SUPPORT.md
|-- LICENSE
`-- NOTICE
```

## Quick Start

### 1. Clone The Repository

```bash
git clone https://github.com/Zw-awa/ManipPilot.git
cd ManipPilot
```

### 2. Read The Overview

Start with:

- [`README.md`](./README.md)
- [`README.zh-CN.md`](./README.zh-CN.md)
- [`README.zh-TW.md`](./README.zh-TW.md)

### 3. Follow The Documentation

This repository is still in the planning and prototyping stage.
Start with the `README`, [`docs/README.md`](./docs/README.md), `SUPPORT`, and issue templates.

### 4. If You Want To Contribute

Read:

- [`CONTRIBUTING.md`](./CONTRIBUTING.md)
- [`Issue templates`](./.github/ISSUE_TEMPLATE/)
- [`SUPPORT.md`](./SUPPORT.md)

## Contributing

Contributions around manipulation workflows, documentation, reproducibility, and usability are welcome.
Start with [`CONTRIBUTING.md`](./CONTRIBUTING.md).

For large changes, open an issue first so the project scope and workflow assumptions can stay coherent.

## Safety Note

This repository is intended for manipulation workflows that may eventually control physical robots.
Even early manipulation systems can pinch fingers, drop objects, collide with fixtures, or damage hardware if used without proper safeguards.
Treat motion, power, end-effector testing, and execution retries as hardware safety work.

## License

This project is licensed under the [Apache License 2.0](./LICENSE).
Copyright `2026` `Zw-awa`.
Additional attribution details are recorded in [`NOTICE`](./NOTICE).
