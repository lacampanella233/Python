# 24-Week Learning Roadmap

Week 0 is an environment and workflow orientation. Weeks 1-24 are the 24 teaching weeks. Each phase ends with a small assessment that must be attempted independently before review.

## Phase 1 — Python core language (Weeks 0-4)

- **Week 0 — Environment and workflow:** uv, the `src` layout, running tests, reading tracebacks, Git status, and the independent-work rule.
- **Week 1 — Values and control flow:** scalar types, expressions, names, conditionals, loops, and small hand traces.
- **Week 2 — Functions:** parameters, return values, scope, docstrings, decomposition, and pure functions.
- **Week 3 — Collections:** lists, tuples, dictionaries, sets, iteration patterns, comprehensions, and complexity intuition.
- **Week 4 — Files and errors:** `pathlib`, context managers, parsing text, exceptions, and a blank-file core-Python assessment.

## Phase 2 — Software engineering foundations (Weeks 5-8)

- **Week 5 — Modules and packages:** imports, public APIs, `src` layout, package metadata, and dependency boundaries.
- **Week 6 — Classes and data modeling:** state, invariants, dataclasses, composition, and when a function is preferable.
- **Week 7 — Tests and debugging:** pytest, parametrization, boundary cases, regression tests, debugger use, and assertions.
- **Week 8 — Typing and CI:** annotations, mypy, Ruff, pre-commit, GitHub Actions, and a small packaged project review.

## Phase 3 — Scientific Python (Weeks 9-13)

- **Week 9 — NumPy fundamentals:** arrays, shape, dtype, axes, indexing, copies, views, and broadcasting.
- **Week 10 — Numerical linear algebra:** vector and matrix operations, conditioning, decompositions, and solving systems without explicit inverses.
- **Week 11 — Matplotlib:** separating computation from plotting, labeled figures, scales, uncertainty, and reproducible visualizations.
- **Week 12 — SciPy:** integration, optimization, interpolation, differential equations, tolerances, and convergence checks.
- **Week 13 — SymPy:** exact expressions, assumptions, simplification, symbolic identities, lambdification, and the boundary between proof and numerical evidence.

## Phase 4 — Angular-momentum toolkit (Weeks 14-18)

- **Week 14 — Mathematical conventions:** basis order, units, normalization, commutators, Hermiticity, and hand-computable spin-1/2 cases.
- **Week 15 — Operator construction:** ladder operators and Cartesian angular-momentum matrices with invariant tests.
- **Week 16 — Tensor products:** coupled and uncoupled bases, Kronecker products, dimension checks, and subsystem operators.
- **Week 17 — Coupling coefficients:** Clebsch-Gordan coefficients, phase conventions, orthogonality, and symbolic-versus-numerical validation.
- **Week 18 — Toolkit integration:** a minimal public API, documentation, performance measurement, project rubric, and independent modification task.

## Phase 5 — Reproducible algorithms and introductory ML (Weeks 19-22)

- **Week 19 — Reproducible experiments:** explicit random generators and seeds, configuration, data provenance, result tables, and repeatable plots.
- **Week 20 — Algorithms:** complexity, profiling, transparent baselines, vectorization after correctness, and measured optimization.
- **Week 21 — Automatic differentiation:** computational graphs, forward and reverse modes, finite-difference checks, and differentiability assumptions.
- **Week 22 — Introductory PyTorch:** tensors, autograd, a small optimization problem, and tests against NumPy or analytic results. Begin only after the core scientific stack is secure.

## Phase 6 — Independent capstone (Weeks 23-24)

- **Week 23 — Capstone design and baseline:** choose a mathematical question, specify definitions and invariants, design tests, plan reproducibility, and implement a transparent baseline.
- **Week 24 — Validation and communication:** difficult cases, comparison with trusted results, quality checks, written limitations, independent demonstration, and final rubric review.

## Phase completion evidence

For each phase, retain tests, a brief progress entry, important mistakes in the error log, and an explanation of one central concept in the learner's own words. Passing means more than obtaining output: the learner should be able to test, explain, and modify the work.
