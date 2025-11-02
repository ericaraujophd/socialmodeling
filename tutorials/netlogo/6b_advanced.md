# Extending Models with New Features (15 min)

Once you have a working model, you can add sophisticated features to address new research questions.

## Adding Social Networks

**Basic network formation:**

```ruby
turtles-own [
  social-connections  ; List of other turtles this one knows
]

to setup
  ; ... basic setup ...
  ask turtles [
    set social-connections []
  ]
  create-social-network
end

to create-social-network
  ; Each turtle connects to nearby turtles
  ask turtles [
    let potential-friends other turtles in-radius 5
    let num-connections min list 5 count potential-friends
    
    ask n-of num-connections potential-friends [
      ; Create bidirectional social connection
      set social-connections lput myself social-connections
      ask myself [
        set social-connections lput myself social-connections
      ]
    ]
  ]
end

to spread-information
  ask turtles with [has-information?] [
    ; Share with social connections
    foreach social-connections [ friend ->
      ask friend [
        if random 100 < influence-probability [
          set has-information? true
        ]
      ]
    ]
  ]
end
```

## Dynamic Environment Changes

**Environmental shocks and changes:**

```ruby
to environmental-change
  ; Periodic environmental disruption
  if ticks mod 500 = 0 and ticks > 0 [
    ask n-of (count patches * 0.1) patches [  ; 10% of environment changes
      set resource-level resource-level * 0.5  ; Resources cut in half
      set pcolor scale-color green resource-level 0 100
    ]
  ]
  
  ; Gradual climate change  
  if ticks mod 100 = 0 [
    ask patches [
      set temperature temperature + 0.1  ; Gradual warming
      update-habitat-suitability
    ]
  ]
end
```

## Learning and Adaptation

**Agents that learn from experience:**

```ruby
turtles-own [
  strategy          ; Current behavior
  memory           ; List of recent experiences
  success-rate     ; How well current strategy works
]

to adapt-strategy
  ask turtles [
    ; Remember recent outcome
    set memory lput last-payoff memory
    if length memory > 10 [ set memory but-first memory ]  ; Keep only recent memories
    
    ; Calculate recent success rate
    if length memory > 5 [
      set success-rate mean memory
      
      ; Change strategy if doing poorly
      if success-rate < 0.3 [
        set strategy one-of ["cooperate" "defect" "tit-for-tat"]
        set memory []  ; Reset memory with new strategy
      ]
    ]
  ]
end
```

## Activity: Feature Addition

**Choose an existing model and add one new feature:**

1. **Social influence:** Agents adopt opinions from friends
2. **Environmental change:** Resources or conditions change over time
3. **Learning:** Agents adapt behavior based on success
4. **Heterogeneity:** Different types of agents with different capabilities

```{admonition} Extension Guidelines
:class: tip

**Start with research question:**
- What new phenomenon do you want to explore?
- How does this relate to your original model?
- What predictions can you make?

**Implement incrementally:**
- Add basic version first
- Test that it works correctly
- Add complexity gradually

**Maintain model clarity:**
- Keep original functionality intact
- Use clear variable names for new features
- Document new behaviors in comments

**Test systematically:**
- Does new feature work as intended?
- Does it interact well with existing features?
- Do results make sense?
```
