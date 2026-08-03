# Assessment Framework

## Four mastery levels

1. **Runs:** The program executes on a representative example and produces plausible output. This is the starting level, not mastery.
2. **Tests:** The learner can design and pass normal, boundary, invalid, regression, and invariant-based tests appropriate to the problem.
3. **Explains:** The learner can justify the algorithm, trace an example, state conventions and limitations, and explain failures in their own words.
4. **Modifies:** The learner can adapt the work to a new requirement, predict affected tests, and preserve correctness without copying a solution.

A topic is secure only when it reaches **modifies** after a delay, not merely when a guided implementation runs once.

## Monthly blank-file test

Once per month, start from a blank file without prior code, autocomplete-generated bodies, notes, or Codex. In 60-90 minutes:

1. Restate a small problem and its input/output contract.
2. Write a correct baseline implementation.
3. Write representative, boundary, and invalid-input tests.
4. Run the quality tools and repair failures.
5. Explain one design choice and one likely extension aloud or in writing.

After the attempt, compare against earlier work, record independent and assisted portions in `progress.md`, and add resolved misconceptions to `error_log.md`. A failed test is diagnostic evidence, not a reason to erase or weaken the test.

## Project rubric (100 points)

| Category | Points | Evidence |
| --- | ---: | --- |
| Mathematical correctness | 25 | Definitions, conventions, hand-computable examples, and valid conclusions |
| Tests and invariants | 20 | Normal, boundary, invalid, regression, and domain-invariant coverage |
| Numerical reliability | 15 | Shapes, dtypes, tolerances, conditioning, convergence, and difficult cases |
| Software design and API | 15 | Small responsibilities, clear interfaces, types, exceptions, and package structure |
| Reproducibility | 10 | Locked environment, explicit seeds, recorded configuration, and repeatable commands |
| Explanation and documentation | 10 | Rationale, assumptions, limitations, usage, and interpretation in the learner's own words |
| Independent modification | 5 | A new requirement completed without copying the original implementation |
| **Total** | **100** | |

Suggested interpretation: 90-100 independent and robust; 75-89 sound with limited gaps; 60-74 functional but not yet secure; below 60 requires a smaller baseline and renewed testing. A severe mathematical error or irreproducible result cannot receive a mastery rating regardless of the numeric total.
