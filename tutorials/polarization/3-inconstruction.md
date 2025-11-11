## Phase 3: The Polarization Model

**Duration**: 30-35 minutes
**Goals**: Students implement the complete model with homophily and observe emergent polarization

### Learning Objectives

By the end of Phase 3, students should be able to:
- Implement homophilic link formation
- Understand how simple local preferences create large-scale social fragmentation
- Measure polarization through multiple metrics
- Observe and analyze emergent network structures

### Conceptual Frame

"Now we'll build the complete model of polarization. The key insight: people tend to connect with others like themselves (homophily), and once they do, they become MORE like each other through interaction. This can fragment society into echo chambers. Nobody intends this outcome, but it emerges from following simple local rules."

### The Complete Feedback Loop

**Phase 3 demonstrates the full dynamic**:

1. **Homophily** creates initial clustering (people link with similar others)
2. **Influence** makes similar people more similar
3. **Tie decay** removes bridges between groups
4. Repeat → Positive feedback loop → Polarization

This feedback loop is **self-reinforcing**:
- Similarity → Connection → More Similarity → Fewer Bridges → More Separation

### Starter Code for Phase 3

```ruby
breed [people person]
undirected-link-breed [social-bonds social-bond]

people-own [
  opinion
  tolerance      ; How different someone needs to be to reject connection
  influence-rate ; How much neighbors affect you
]

social-bonds-own [
  link-age
]

globals [
  link-formation-rate    ; Probability of creating new link per tick
  link-decay-rate        ; Rate at which links break
  max-links-per-person   ; Network density control
]

to setup
  clear-all
  
  set link-formation-rate 0.1     ; 10% chance to form new link
  set link-decay-rate 0.05        ; Rate links break
  set max-links-per-person 5      ; Max neighbors
  
  create-people 50 [
    set opinion random 100
    set tolerance 25 + random 15   ; 25-40 opinion points
    set influence-rate 0.2 + random-float 0.1  ; 0.2-0.3
    
    setxy random-xcor random-ycor
    set size 1
    set color scale-color red opinion 0 100
  ]
  
  ; Initialize with sparse random network
  ask people [
    if random 100 < 30 [  ; 30% chance to form initial links
      let potential-friends other people
      let friend-count random 3
      repeat friend-count [
        if any? potential-friends [
          let new-friend one-of potential-friends
          if not link-neighbor? new-friend [
            create-link-with new-friend [
              set link-age 0
              set color grey
              set thickness 0.2
            ]
          ]
          set potential-friends potential-friends with [self != new-friend]
        ]
      ]
    ]
  ]
  
  reset-ticks
end

to go
  ; Main update sequence
  update-opinions-through-influence
  form-new-links
  decay-weak-links
  update-visuals
  
  tick
end

to update-opinions-through-influence
  ; People are influenced by their neighbors
  ask people [
    let neighbors link-neighbors
    
    if any? neighbors [
      ; Weight influence by opinion similarity
      let total-influence 0
      let weighted-sum 0
      
      ask neighbors [
        let similarity 1 - (abs ([opinion] of myself - opinion) / 100)
        set total-influence total-influence + similarity
        set weighted-sum weighted-sum + (opinion * similarity)
      ]
      
      let avg-influence weighted-sum / total-influence
      set opinion (1 - [influence-rate] of self) * opinion + [influence-rate] of self * avg-influence
      
      ; Clamp opinion to 0-100
      if opinion < 0 [set opinion 0]
      if opinion > 100 [set opinion 100]
    ]
  ]
end

to form-new-links
  ; Homophily: people preferentially connect to similar others
  ask people [
    if random 100 < link-formation-rate * 100 [
      if count link-neighbors < max-links-per-person [
        ; Find potential friends with similar opinions (within tolerance)
        let potential-friends people with [
          abs ([opinion] of myself - opinion) < [tolerance] of myself and
          not link-neighbor? myself and
          self != myself
        ]
        
        if any? potential-friends [
          create-link-with one-of potential-friends [
            set link-age 0
            set color grey
            set thickness 0.2
          ]
        ]
      ]
    ]
  ]
end

to decay-weak-links
  ; Links break if people become too different
  ask social-bonds [
    set link-age link-age + 1
    
    let opinion-diff abs ([opinion] of end1 - [opinion] of end2)
    
    ; Probability of breaking increases with opinion distance
    if opinion-diff > 40 [
      if random 100 < link-decay-rate * 100 [
        die
      ]
    ]
  ]
end

to update-visuals
  ; Update colors and link properties
  ask people [
    set color scale-color red opinion 0 100
  ]
  
  ask social-bonds [
    ; Thicker lines between similar people
    let opinion-diff abs ([opinion] of end1 - [opinion] of end2)
    set thickness 0.1 + 0.3 * (1 - opinion-diff / 100)
  ]
end

; Helper predicate for checking link neighbors
to-report link-neighbor? [target]
  report target != self and any? link-neighbors with [self = target]
end

; Measurement reporters for analysis
to-report polarization-index
  ; Measures spread: high = polarized, low = consensus
  let mean-opinion mean [opinion] of people
  let variance mean [((opinion - mean-opinion) ^ 2)] of people
  report sqrt variance
end

to-report network-density
  ; Proportion of possible links that exist
  let actual-links count social-bonds
  let possible-links (count people * (count people - 1)) / 2
  report actual-links / possible-links
end

to-report average-opinion-distance
  ; Average difference between linked people
  let total-distance 0
  ask social-bonds [
    set total-distance total-distance + abs ([opinion] of end1 - [opinion] of end2)
  ]
  
  if count social-bonds > 0 [
    report total-distance / count social-bonds
  ]
  report 0
end

to-report cross-cutting-links
  ; Links that connect people with different opinions
  let count-cross 0
  ask social-bonds [
    let opinion-diff abs ([opinion] of end1 - [opinion] of end2)
    if opinion-diff > 30 [
      set count-cross count-cross + 1
    ]
  ]
  report count-cross
end

; Simplified component counting for classroom use
to-report estimate-components
  ; Returns approximate number of opinion clusters
  let clusters 0
  let opinions sort-on [opinion] people
  let i 0
  repeat (length opinions - 1) [
    let curr-opinion [opinion] of item i opinions
    let next-opinion [opinion] of item (i + 1) opinions
    
    if (next-opinion - curr-opinion) > 20 [
      set clusters clusters + 1
    ]
    set i i + 1
  ]
  
  report clusters + 1
end

; Intervention: add bridge-builders
to add-bridge-builders [num]
  ; Create people with high tolerance who try to connect different groups
  ask n-of num people [
    set tolerance 50
    set influence-rate 0.05
    set color yellow
  ]
end
```

### Phase 3 Mechanics in Detail

#### Homophilic Link Formation

```netlogo
to form-new-links
  ask people [
    if random 100 < link-formation-rate * 100 [
      if count link-neighbors < max-links-per-person [
        ; Find potential friends with similar opinions (within tolerance)
        let potential-friends people with [
          abs ([opinion] of myself - opinion) < [tolerance] of myself and
          not link-neighbor? myself and
          self != myself
        ]
        
        if any? potential-friends [
          create-link-with one-of potential-friends [
            set link-age 0
            set color grey
            set thickness 0.2
          ]
        ]
      ]
    ]
  ]
end
```

This implements **homophily**:
- `link-formation-rate`: Probability each person tries to form a new link
- `tolerance`: How similar someone needs to be (in opinion points)
- `max-links-per-person`: Network density control (prevents network from becoming infinitely dense)
- `abs ([opinion] of myself - opinion) < [tolerance] of myself`: Only forms links with similar others

**Key insight**: This is not random link formation. It's preferential attachment to similar others.

#### Sophisticated Influence

```netlogo
to update-opinions-through-influence
  ask people [
    let neighbors link-neighbors
    
    if any? neighbors [
      ; Weight influence by opinion similarity
      let total-influence 0
      let weighted-sum 0
      
      ask neighbors [
        let similarity 1 - (abs ([opinion] of myself - opinion) / 100)
        set total-influence total-influence + similarity
        set weighted-sum weighted-sum + (opinion * similarity)
      ]
      
      let avg-influence weighted-sum / total-influence
      set opinion (1 - [influence-rate] of self) * opinion + [influence-rate] of self * avg-influence
    ]
  ]
end
```

This is more sophisticated than Phase 2:
- **Similarity weighting**: Neighbors closer to your opinion influence you more
- If neighbor's opinion is 45 and yours is 50, they influence you more than if their opinion was 20
- This models **selective exposure**: we're more influenced by those we already agree with

#### Measurement Reporters

Phase 3 includes several metrics to track polarization:

**polarization-index**: Standard deviation of opinions. High = polarized, low = consensus.

**network-density**: What proportion of possible links exist? Shows network connectivity.

**average-opinion-distance**: Average opinion difference between linked people. Should decrease as network fragments (because links only survive between similar people).

**cross-cutting-links**: How many links connect people with significantly different opinions? As polarization occurs, this should decrease sharply.

**estimate-components**: Approximate number of separated groups. Increases with polarization.

### Classroom Activities - Phase 3

#### Activity 3.1: Run the Full Model (8 minutes)

```
setup
repeat 100 [go]
```

Have students watch the model evolve. Ask:
- "What patterns do you see in the network?" (Initial sparse network → clustering → fragmentation)
- "What happens to colors?" (Initially spread across spectrum; gradually cluster into two zones)
- "Did groups form? How many?" (Usually 2-3 distinct opinion groups)
- "What happened to people's opinions?" (Converged within groups, diverged between groups)
- "Are there any links between different-colored people?" (Fewer and fewer as model progresses)

**Learning point**: The model shows how polarization emerges from simple local mechanisms.

#### Activity 3.2: Create Plots (5 minutes)

Create two plots in NetLogo:

**Plot 1: "Opinion Distribution"**
```
plot-pen "opinions"
histogram [opinion] of people
```

This shows the distribution of opinions. Should go from flat (uniform) to bimodal (two peaks).

**Plot 2: "Network Metrics Over Time"**
```
plot-pen "polarization"
plot polarization-index

plot-pen "density"
plot network-density

plot-pen "cross-links"
plot cross-cutting-links / max 1 (count social-bonds) ; Normalize
```

Ask:
- "What does the opinion distribution look like?" (Initially flat; becomes bimodal after ~50 ticks)
- "What happens to polarization-index?" (Increases over time, then levels off)
- "What happens to network-density?" (Usually stays relatively stable)
- "What happens to cross-cutting links?" (Decreases dramatically; bridges between groups disappear)

**Learning point**: Metrics give us objective measures of polarization.

#### Activity 3.3: Parameter Exploration (10 minutes)

Test different settings:

**Experiment 1: Tolerance**
```
setup
ask people [set tolerance 15]  ; Low tolerance
repeat 100 [go]
show polarization-index
```

vs.

```
setup
ask people [set tolerance 40]  ; High tolerance
repeat 100 [go]
show polarization-index
```

Ask:
- "How does tolerance affect polarization?" (Lower tolerance → more polarization)
- "Why?" (People with low tolerance only link to very similar others; this accelerates fragmentation)
- "What's the critical tolerance value?" (Around 25-30 in this model)

**Experiment 2: Link Formation Rate**
```
setup
set link-formation-rate 0.05  ; Slow link formation
repeat 100 [go]
show polarization-index
```

vs.

```
setup
set link-formation-rate 0.20  ; Fast link formation
repeat 100 [go]
show polarization-index
```

Ask:
- "Does faster link formation increase or decrease polarization?" (Usually increases; more homophily)
- "Why?" (More rapid homophily means bridges disappear faster)

**Experiment 3: Influence Rate**
```
setup
ask people [set influence-rate 0.1]  ; Weak influence
repeat 100 [go]
show polarization-index
```

vs.

```
setup
ask people [set influence-rate 0.4]  ; Strong influence
repeat 100 [go]
show polarization-index
```

Ask:
- "Does stronger influence increase or decrease polarization?" (Usually decreases)
- "Why?" (Stronger influence pulls people together before ties break)

**Learning point**: Different parameters matter in different ways. Understanding these relationships is key to understanding real polarization.

#### Activity 3.4: Intervention Experiment (7 minutes)

Test what happens with bridge-builders:

```
setup
repeat 50 [go]  ; Let polarization develop
add-bridge-builders 5  ; Add 5 people with high tolerance
repeat 50 [go]  ; Continue
```

Ask:
- "What happens to the polarization-index?" (Should decrease after bridge-builders are added)
- "What happens to cross-cutting-links?" (Should increase)
- "How many bridge-builders do we need?" (Test with 2, 5, 10, 20)
- "Can bridge-builders prevent polarization if added early?" (Probably yes)
- "Can they reduce polarization if added late?" (Yes, but less effectively)

**Learning point**: Interventions can work, but timing matters. Early interventions are more effective than late ones.

### Real-World Parallels

**Social Media Algorithm Case Study**:
- Platform algorithms do much of the homophilic link formation
- Your feed shows content similar to what you've liked (influence-weighted by similarity)
- If you don't engage with opposing views, those connections get hidden (tie decay)
- Result: algorithmic polarization without explicit intention

**Political Sorting Case Study**:
- Over the past 40 years, Americans have sorted into increasingly homogeneous geographic regions and online communities
- This sorting is homophily in action
- Within these communities, positions become more extreme (influence)
- Cross-cutting ties decrease (tie decay)
- Result: higher polarization

**Echo Chambers in Organizations**:
- New employees preferentially connect with similar others (homophily)
- These connections reinforce shared perspectives (influence)
- Bridges between departments fade (tie decay)
- Result: organizational silos

### Assessment - Phase 3

Students should be able to:
- Explain the three mechanisms (homophily, influence, tie decay) and how they interact
- Predict what happens with different parameter values
- Interpret the four key metrics (polarization-index, network-density, average-opinion-distance, cross-cutting-links)
- Design an experiment to test a research question about polarization
- Discuss trade-offs between intervention strategies

### Common Questions - Phase 3

**Q: Why do you weight influence by similarity?**
A: Because in reality, we're more influenced by those we agree with. If someone's worldview is opposite yours, you're less likely to be convinced by them. Similarity-weighted influence models this selective openness.

**Q: What if I set tolerance very high?**
A: Everyone links with everyone (no homophily). Everyone influences everyone equally. Opinions converge to a single global average. No polarization.

**Q: What if I set tolerance very low?**
A: People only link with near-identical others (strong homophily). Links form in very tight clusters. Polarization happens very quickly.

**Q: Can I run this for 1000 ticks?**
A: Yes! But usually the system stabilizes by 100-200 ticks. After that, the network structure and opinion distribution don't change much.

---