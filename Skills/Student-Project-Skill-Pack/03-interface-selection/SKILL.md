---
name: mat422-interface-selection
description: Choose a reliable reproducible mechanism for connecting Codex-generated work to the selected computational software.
---
# Interface Selection Skill

Use this skill after selecting the software platform or when deciding between platforms. A formal external API is not required. The goal is to define a reproducible computational loop from student requirements and data to Codex-generated implementation, software execution, quantitative results, Codex evaluation/revision, and final validated output.

## Interface priority

Prefer the simplest reliable mechanism that the student can actually run and document:

1. Native programming or scripting.
2. Notebook or interactive execution.
3. Command-line or batch execution.
4. Structured file/data exchange.
5. API, engine interface, plugin, add-in, or macro when useful and available.
6. GUI automation only as a fallback.

## Acceptable mechanisms

- Python: `.py` scripts, Jupyter/Colab notebooks, package APIs, CSV/JSON/Excel files.
- MATLAB: `.m` scripts/functions, Live Scripts, MAT/CSV/Excel files, optional MATLAB Engine API.
- R: `.R`, R Markdown, Quarto, notebooks, CSV/Excel/RDS files.
- SAS: `.sas` programs, SAS datasets, CSV/Excel inputs, preserved output files.
- Stata: `.do` files, DTA/CSV/Excel inputs, logs and output tables.
- Optional software: APIs, macros, plugins/add-ins, command files, structured model/data files, or documented reproducible manual execution.

## Agent responsibilities

1. Identify what the selected software exposes and what the student can access.
2. Choose the simplest reproducible interface that can execute the project workflow.
3. Explain what the interface can and cannot control.
4. Define input files, output files, commands, notebooks, scripts, logs, and result artifacts.
5. Specify how actual outputs/errors will be returned to Codex for diagnosis and revision.
6. Document any limitations, manual steps, license restrictions, or proprietary-file constraints.
7. Avoid requiring paid APIs, unavailable software, or unsupported integrations.

## Output format

Produce an interface plan with these headings:

- Selected software and version/environment
- Chosen interface mechanism
- Why this interface is sufficient
- Required input files and formats
- Generated code/scripts/notebooks/commands
- Expected output files, metrics, figures, logs, or tables
- Execution steps
- How Codex will receive outputs/errors for iteration
- Limitations and reproducibility notes
- Files to document in `software-info.md`

## Quality bar

The interface plan should be strong enough that another student or instructor can reproduce the execution path from the GitHub repository without needing the original chat context.
