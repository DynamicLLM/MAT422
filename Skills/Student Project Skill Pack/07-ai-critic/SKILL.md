---
name: mat422-ai-critic
description: Critically inspect AI-generated reasoning, code, model selection, execution evidence, and conclusions before final acceptance.
---
# AI Critic Skill

Use this skill before final documentation. Codex should critique its own modeling recommendations and outputs, and the student should use domain judgment to decide what to trust, correct, or reject.

## Questions to ask

- Did the solution address the original problem, objective, constraints, and success criteria?
- Were assumptions stated, justified, and checked where possible?
- Were at least two candidate models or methods considered when reasonable?
- Was the final model chosen using quantitative evidence rather than convenience?
- Did the selected software actually execute the code or workflow?
- Are reported values traceable to actual outputs, metrics, logs, figures, or result files?
- Could data leakage, overfitting, sample bias, numerical error, model misspecification, or invalid causal interpretation matter?
- Were constraints satisfied and limitations documented?
- Is the workflow reproducible from the GitHub repository?
- What result, error, or assumption would invalidate the conclusion?

## Agent responsibilities

1. Identify at least three substantive risks, limitations, possible AI errors, or alternative interpretations.
2. Separate student-specified requirements from Codex-generated recommendations.
3. Check whether final claims are supported by executed evidence.
4. Flag any places where Codex may have overclaimed, hallucinated, ignored constraints, or selected an easy but weak method.
5. Recommend corrections, caveats, additional validation, or narrower conclusions.
6. Produce wording the student can adapt for the final report's limitations and AI errors/human corrections section.

## Output format

Produce an AI critique record with:

- Claims reviewed
- Evidence supporting each claim
- Risks or possible errors
- Human corrections or judgments required
- Remaining limitations
- Final claims that are justified
- Claims that should be softened or removed
- Suggested final-report paragraph

## Quality bar

A good critique is specific and evidence-based. Do not write generic statements such as "AI may be wrong" without connecting them to this project's model choice, data, code, assumptions, outputs, or conclusions.
