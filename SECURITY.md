# Security Policy

[English](./SECURITY.md) | [简体中文](./SECURITY.zh-CN.md) | [繁體中文](./SECURITY.zh-TW.md)

## Reporting A Vulnerability

Please do not open a public issue for problems that could realistically be abused as a security vulnerability.
If a report involves unauthorized control, unsafe remote access, credential exposure, command injection, insecure update behavior, model or data tampering, or any exploit path that others could reuse, report it through the maintainer contact path first.

If you discover a vulnerability, report it privately through the repository owner's available contact channel and include:

- a clear summary
- affected files, nodes, or subsystem
- reproduction steps if known
- possible impact
- suggested mitigation if available

## What Counts As A Security Issue Here

Examples include:

- local or network control paths that could be abused by an attacker
- unsafe command handling across robotics or operator interfaces
- credential, token, or secret exposure once deployment or provisioning exists
- insecure task execution or update behavior
- vulnerabilities that could enable dangerous unintended motion through unauthorized or malicious control

## What Does Not Belong In The Private Security Process

The following are generally **not** security reports and should not be sent through the private vulnerability path:

- generic robotics bugs with no plausible security angle
- failed task execution, weak grasp performance, or poor planning quality without an exploit path
- prototype instability caused by unfinished setup
- third-party robot, sensor, actuator, or controller defects
- wiring mistakes, setup mistakes, or damaged parts
- user experimentation outside the documented safe envelope
- unsupported local modifications
- "it does not work" reports without a credible security impact

Those issues should usually be handled as:

- a normal public bug report
- a `Question / Support` issue
- or a local debugging task outside project maintenance scope

## Scope Boundaries

This repository is an early open robotics project, not a guarantee of correctness for every third-party robot, sensor, motor, controller, gripper, or user-built setup.

The project security process is intended for vulnerabilities in the repository's own design, code, documented behavior, or supported workflows.
It is not intended to triage every failure in:

- third-party hardware quality
- user-built setup quality
- unofficial modifications
- off-spec deployment
- undocumented operating procedures
- unsupported integrations or experiments

## Supported Scope

At this stage, the repository is in active planning and prototyping.
Support is best-effort, and response time may vary.

## Disclosure Guidance

Please allow time for review and mitigation before publishing detailed exploit steps.
Coordinated disclosure is preferred.
