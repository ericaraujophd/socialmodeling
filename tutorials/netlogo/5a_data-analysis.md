# Why Data Matters in Modeling (10 min)

Models without data are just entertaining animations. To answer research questions, you need systematic measurement and analysis.

## Models Answer Questions with Evidence

**Without data:** "My segregation model seems to create clusters sometimes."
**With data:** "When tolerance is below 30%, segregation emerges in 95% of runs within 200 time steps."

**Without data:** "Cooperation appears to work in this model."
**With data:** "Cooperation is stable when the population is smaller than 50 agents, but collapses above 75 agents."

## What Makes Good Model Data?

**Systematic measurement:**

- Track the same variables consistently
- Measure at regular intervals
- Run multiple times to account for randomness
- Test different parameter values systematically

**Meaningful variables:**

- **Outcome measures:** What you're trying to explain (segregation level, cooperation rate, infection spread)
- **Input parameters:** What you're varying (tolerance levels, payoff values, transmission rates)
- **Process indicators:** How things change over time (movement patterns, network formation, learning rates)

## Activity: Identifying Key Variables

```{admonition} Think About Your Models
:class: question

For a model you've seen or built:

1. **What is the main research question?**
2. **What outcome would answer that question?**
3. **How could you measure that outcome numerically?**
4. **What inputs might affect that outcome?**
5. **What intermediate processes might be important to track?**

**Example - Segregation Model:**
- Research question: How do individual preferences create residential segregation?
- Outcome: Percentage of agents living near similar neighbors
- Measurement: Count neighbors of same type / total neighbors
- Inputs: Tolerance threshold, population size, neighborhood size
- Processes: Movement rate, satisfaction levels over time
```
