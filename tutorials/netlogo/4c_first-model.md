# Documentation and Sharing (10 min)

Good models need clear documentation so others can understand and use them.

## Writing Clear Comments in Code

**Comment every major section:**

```ruby
to go
  ; MOVEMENT PHASE: Ants move based on pheromone trails
  ask turtles [
    if not carrying-food? [
      follow-pheromone-trail
    ] else [
      return-to-nest
    ]
  ]
  
  ; ENVIRONMENT PHASE: Update pheromone trails
  evaporate-pheromones
  
  tick
end
```

**Explain complex calculations:**

```ruby
; Calculate pheromone gradient (difference between current and best patch)
let current-pheromone [pheromone] of patch-here
let best-nearby max [pheromone] of patches in-radius 2
let gradient best-nearby - current-pheromone
```

## Using the Info Tab Effectively

**Include these sections in your Info tab:**

```
**WHAT IS IT?**
Brief description of the phenomenon and research question

**HOW IT WORKS**
Explanation of agent behaviors and interactions

**HOW TO USE IT**  
Instructions for running the model and interpreting results

**THINGS TO NOTICE**
Key patterns to watch for

**THINGS TO TRY**
Suggested experiments with different parameters
```

## Preparing Models for Others to Understand

**Model Documentation Checklist**

**Code Quality:**

- Clear, meaningful variable names
- Comments explaining complex sections
- Organized into logical procedures

**User Interface:**

- Sliders for key parameters
- Buttons for setup and go
- Monitors showing important statistics
- Plots tracking key variables over time

**Documentation:**

- Complete Info tab
- Clear instructions
- Background information and references

**Testing:**

- Model runs without errors
- Results are reasonable and interesting
- Different parameter values produce different outcomes

## Activity: Code Review

**Pairs review each other's models:**

1. **Can you understand what the model does** without explanation?
2. **Are variable names clear and meaningful?**
3. **Are there enough comments** to follow the logic?
4. **Does the Info tab explain** how to use the model?
5. **What questions does the model raise** that could be explored further?

```{admonition} Giving Good Feedback
:class: tip

**Focus on understanding, not perfection:**

- "I'm confused about what this variable represents"
- "This section could use more comments"
- "The Info tab could explain the research question more clearly"

**Ask questions rather than giving commands:**

- "What happens if you change this parameter?"
- "How does this relate to real-world ant behavior?"
- "What other factors might be important to include?"
```
