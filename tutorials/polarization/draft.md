

---

## Phase 2: Links with Behavior (20-25 minutes)

### Learning Objectives
- Use links to enable agent interaction
- Iterate over neighbors through links
- Modify link properties dynamically
- Break links under certain conditions

### Conceptual Frame
"Now that we can create links, let's use them to model how people influence each other. Links don't just represent connections—they're the channels through which interaction happens."

### Code: Influence Through Links

```netlogo
breed [people person]
undirected-link-breed [social-bonds social-bond]

people-own [
  opinion
  influenced?
]

social-bonds-own [strength]

to setup
  clear-all
  
  create-people 20 [
    set opinion random 100
    setxy random-xcor random-ycor
    set size 1
    set influenced? false
    
    ; Color by opinion: red = extreme, blue = moderate
    set color scale-color red opinion 0 100
  ]
  
  ask people [
    create-links-with n-of 3 other people [
      set strength 0.5  ; All links start with equal strength
      set color grey
      set thickness 0.3
    ]
  ]
  
  reset-ticks
end

to go
  ask people [ set influenced? false ]
  
  influence-through-links
  break-weak-ties
  
  tick
end

to influence-through-links
  ask people [
    let neighbors link-neighbors
    
    if any? neighbors [
      ; Calculate weighted average opinion from neighbors
      let neighbor-opinions []
      ask neighbors [
        set neighbor-opinions lput opinion neighbor-opinions
      ]
      
      let avg-neighbor-opinion mean neighbor-opinions
      
      ; Update opinion: 70% your opinion, 30% average neighbor opinion
      let new-opinion 0.7 * opinion + 0.3 * avg-neighbor-opinion
      
      ; Only update if change is significant (to prevent oscillation)
      if abs (new-opinion - opinion) > 0.1 [
        set opinion new-opinion
        set influenced? true
      ]
    ]
    
    ; Update color to reflect new opinion
    set color scale-color red opinion 0 100
  ]
end

to break-weak-ties
  ; If two linked people differ too much, the link breaks
  ask social-bonds [
    let opinion-diff abs ([opinion] of end1 - [opinion] of end2)
    
    if opinion-diff > 50 [
      die  ; Remove the link
    ]
  ]
end
```

### Classroom Activities - Phase 2

**Activity 2.1: Observe Influence**
- Run the model for 50 ticks
- Ask: "What happened to people's opinions? Did they converge?"
- Ask: "Which links broke and why?"

**Activity 2.2: Modify Influence Strength**
Add parameter:
```netlogo
to go-with-strength [influence-rate]
  ask people [ set influenced? false ]
  
  influence-through-links-with-rate influence-rate
  break-weak-ties
  
  tick
end

to influence-through-links-with-rate [rate]
  ask people [
    let neighbors link-neighbors
    
    if any? neighbors [
      let neighbor-opinions []
      ask neighbors [
        set neighbor-opinions lput opinion neighbor-opinions
      ]
      
      let avg-neighbor-opinion mean neighbor-opinions
      let new-opinion (1 - rate) * opinion + rate * avg-neighbor-opinion
      
      if abs (new-opinion - opinion) > 0.1 [
        set opinion new-opinion
        set influenced? true
      ]
    ]
    
    set color scale-color red opinion 0 100
  ]
end
```

Ask: "What happens if neighbors have MORE influence (rate = 0.5 instead of 0.3)?"

**Activity 2.3: Visualizing Link Dynamics**
Add:
```netlogo
to-report count-links
  report count social-bonds
end

to visualize-strong-ties
  ask social-bonds [
    let opinion-diff abs ([opinion] of end1 - [opinion] of end2)
    ; Thicker lines for people with similar opinions
    set thickness 0.1 + 0.4 * (1 - opinion-diff / 100)
  ]
end
```

Ask: "How do link patterns change as the model runs? What does this reveal about network structure during polarization?"

### Key Concepts Introduced
- Using `link-neighbors` to access connected turtles
- Iterating with `ask neighbors [...]`
- Dynamic link properties reflecting network state
- Link death as a mechanism (ties breaking when incompatible)
- How network structure affects agent behavior

---

## Phase 3: The Polarization Model (30-35 minutes)

### Learning Objectives
- Model homophily (preference for similar others)
- Create dynamic link formation
- Implement selective exposure
- Observe emergent polarization

### Conceptual Frame
"Now we'll build a complete model of polarization. The key insight: people tend to connect with others like themselves (homophily), and once they do, they become MORE like each other through interaction. This can fragment society into echo chambers."

### Code: Complete Polarization Model

```netlogo
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
  link-decay-rate        ; How quickly people stop being friends
  max-links-per-person   ; Network density control
]

to setup
  clear-all
  
  set link-formation-rate 0.1     ; 10% chance to form new link
  set link-decay-rate 0.05        ; Links break if opinion-diff > 50
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
to-report count-components
  ; Count disconnected components in network
  let components 0
  let visited (turtle-set)
  
  ask people [
    if not member? self visited [
      set components components + 1
      let to-visit (turtle-set self)
      let component (turtle-set)
      
      repeat count people [
        if any? to-visit [
          let current one-of to-visit
          set component (component with [self = current])
          set visited (visited with [self = current])
          set to-visit (to-visit with [self != current])
          set to-visit (to-visit | ([link-neighbors] of current with [not member? self visited]))
        ]
      ]
    ]
  ]
  
  report components
end

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
```

### Classroom Activities - Phase 3

**Activity 3.1: Run the Full Model**
```
; In the Command Center or as buttons
setup
repeat 100 [go]
```

Ask:
- "What patterns do you see in the network?"
- "Did groups form? How many?"
- "What happened to people's opinions?"

**Activity 3.2: Parameter Exploration**

Create procedures to test different settings:

```netlogo
to test-tolerance [tol]
  clear-all
  set link-formation-rate 0.1
  ask people [set tolerance tol]
  repeat 200 [go]
  show (word "Tolerance " tol ": Components = " count-components " Polarization = " precision polarization-index 2)
end

to test-formation-rate [rate]
  clear-all
  set link-formation-rate rate
  repeat 200 [go]
  show (word "Formation rate " rate ": Density = " precision network-density 3)
end
```

Have students run:
- `test-tolerance 15`
- `test-tolerance 30`
- `test-tolerance 50`

Ask: "How does tolerance affect polarization? Why?"

**Activity 3.3: Add Plotting**

In NetLogo, create two plots:

Plot 1: "Opinion Distribution"
```
plot-pen "opinions"
histogram [opinion] of people
```

Plot 2: "Network Metrics Over Time"
```
plot-pen "components"
plot count-components

plot-pen "polarization"
plot polarization-index
```

**Activity 3.4: Intervention Experiment**

Add a procedure to introduce bridge-builders:

```netlogo
to add-bridge-builders [num]
  ; Create people with high tolerance who try to connect different groups
  ask n-of num people [
    set tolerance 50
    set influence-rate 0.05
    set color yellow
  ]
end
```

Ask: "What if 10% of people are 'bridge-builders' who willingly connect across opinion lines? Does this prevent polarization?"

Run:
```
setup
add-bridge-builders 5
repeat 100 [go]
```

---

## Phase 4: Evaluation & Analysis (20-30 minutes)

### Learning Objectives
- Critically evaluate the model against reality
- Design experiments to test model behavior
- Understand model limitations
- Connect model insights to social theory

### Key Questions for Evaluation

#### Structural Analysis
"What does the network structure tell us about polarization?"

1. **Component Analysis**: How many separated groups formed?
   - Reporter: `count-components`
   - Reality check: "Can groups that don't talk to each other really exist?"

2. **Link Density**: What proportion of possible connections became actual?
   - Reporter: `network-density`
   - Reality: People can't link to everyone; homophily constrains networks

3. **Bridge Links**: How many links connect people with different opinions?
   - Extension: Create a reporter that counts cross-opinion links

```netlogo
to-report cross-cutting-links
  let count-cross 0
  ask social-bonds [
    let opinion-diff abs ([opinion] of end1 - [opinion] of end2)
    if opinion-diff > 30 [
      set count-cross count-cross + 1
    ]
  ]
  report count-cross
end
```

#### Behavioral Dynamics
"How does the model evolve over time?"

1. **Convergence vs. Divergence**: Do opinions cluster or spread?
   - Use plot: `polarization-index` over time
   - Ask: "At what point does polarization become irreversible?"

2. **Opinion Bifurcation**: Does the model create two distinct camps?
   - Analyze: Histogram of final opinions
   - Reality check: "How well does this match real polarization?"

3. **Tie Strength Decay**: Do links actually break?
   - Track: `count social-bonds` over time
   - Ask: "When do bridges between groups disappear?"

#### Model Critique: The Imperfect Model Lens

**What does the model capture well?**
- Self-reinforcement: Once people are similar, they become more similar
- Network fragmentation: Interaction networks can break into components
- Homophily as driver: Preference for similarity can amplify polarization

**What does the model oversimplify?**

1. **Single-dimensional opinions**: Real politics is multidimensional
   - Discussion: "What if people disagreed on multiple issues independently?"
   - Extension challenge: Modify model to use 2D opinions (economic, social)

2. **Deterministic influence**: Real influence is more complex
   - Reality: People can resist influence, selectively expose themselves
   - Question: "Should influence depend on emotional appeal, not just similarity?"

3. **No external information**: Real people encounter media, campaigns, etc.
   - Extension: Add "news events" that shift opinions exogenously

4. **No leadership effects**: Real polarization often has charismatic leaders
   - Extension: Create "influencer" agents with higher influence weight

5. **Symmetric influence**: Why should weak ties matter equally?
   - Reality: Some people are more influential than others
   - Extension: Weight influence by follower count or credibility

**What would make the model more realistic?**

Discussion prompts:

- "How would adding media consumption change this?"
- "What if some people actively try to bridge divides?"
- "What happens if new people enter with diverse opinions?"
- "Could we model confirmation bias more explicitly?"
- "How would anonymous social networks differ from face-to-face?"

### Experimental Design Assignment

Have students design an experiment to test a research question:

**Example 1**: "Can bridge-builders prevent polarization?"
- Manipulate: Percentage of people with high tolerance
- Measure: Final `polarization-index` and `count-components`
- Report findings

**Example 2**: "Does network density matter?"
- Manipulate: `max-links-per-person` parameter
- Measure: How quickly does `network-density` stabilize?
- Interpret: "Why might denser networks polarize differently?"

**Example 3**: "What's the critical tolerance threshold?"
- Test: Run model with tolerance from 5 to 50 in increments of 5
- Create: Line plot of polarization vs. tolerance
- Conclude: "Below what tolerance do groups inevitably separate?"

### Critical Thinking Prompts

1. **Validity**: "To what extent does this model explain real polarization?"
   - What evidence supports the homophily mechanism?
   - What factors does it ignore?

2. **Generalization**: "In what contexts would this model apply best?"
   - Online communities vs. offline societies?
   - Specific issues vs. general worldview?

3. **Normative**: "If this model is accurate, what should we do?"
   - Design policies that increase tolerance?
   - Create institutions that connect divided groups?
   - Foster information diversity?

4. **Reflexivity**: "What biases might influence how we built this model?"
   - Did we oversimplify certain mechanisms?
   - Did we make assumptions that aren't justified?

---

## Complete Starter Code (All Phases Combined)

For instructor reference, here's the full model with all features available:

```netlogo
breed [people person]
undirected-link-breed [social-bonds social-bond]

people-own [
  opinion
  tolerance
  influence-rate
]

social-bonds-own [
  link-age
]

globals [
  link-formation-rate
  link-decay-rate
  max-links-per-person
]

to setup
  clear-all
  
  set link-formation-rate 0.1
  set link-decay-rate 0.05
  set max-links-per-person 5
  
  create-people 50 [
    set opinion random 100
    set tolerance 25 + random 15
    set influence-rate 0.2 + random-float 0.1
    
    setxy random-xcor random-ycor
    set size 1
    set color scale-color red opinion 0 100
  ]
  
  ask people [
    if random 100 < 30 [
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
  update-opinions-through-influence
  form-new-links
  decay-weak-links
  update-visuals
  
  tick
end

to update-opinions-through-influence
  ask people [
    let neighbors link-neighbors
    
    if any? neighbors [
      let total-influence 0
      let weighted-sum 0
      
      ask neighbors [
        let similarity 1 - (abs ([opinion] of myself - opinion) / 100)
        set total-influence total-influence + similarity
        set weighted-sum weighted-sum + (opinion * similarity)
      ]
      
      let avg-influence weighted-sum / total-influence
      set opinion (1 - [influence-rate] of self) * opinion + [influence-rate] of self * avg-influence
      
      if opinion < 0 [set opinion 0]
      if opinion > 100 [set opinion 100]
    ]
  ]
end

to form-new-links
  ask people [
    if random 100 < link-formation-rate * 100 [
      if count link-neighbors < max-links-per-person [
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
  ask social-bonds [
    set link-age link-age + 1
    
    let opinion-diff abs ([opinion] of end1 - [opinion] of end2)
    
    if opinion-diff > 40 [
      if random 100 < link-decay-rate * 100 [
        die
      ]
    ]
  ]
end

to update-visuals
  ask people [
    set color scale-color red opinion 0 100
  ]
  
  ask social-bonds [
    let opinion-diff abs ([opinion] of end1 - [opinion] of end2)
    set thickness 0.1 + 0.3 * (1 - opinion-diff / 100)
  ]
end

to-report link-neighbor? [target]
  report target != self and any? link-neighbors with [self = target]
end

to-report polarization-index
  let mean-opinion mean [opinion] of people
  let variance mean [((opinion - mean-opinion) ^ 2)] of people
  report sqrt variance
end

to-report network-density
  let actual-links count social-bonds
  let possible-links (count people * (count people - 1)) / 2
  report actual-links / possible-links
end

to-report average-opinion-distance
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
  let count-cross 0
  ask social-bonds [
    let opinion-diff abs ([opinion] of end1 - [opinion] of end2)
    if opinion-diff > 30 [
      set count-cross count-cross + 1
    ]
  ]
  report count-cross
end

to add-bridge-builders [num]
  ask n-of num people [
    set tolerance 50
    set influence-rate 0.05
    set color yellow
  ]
end

; For testing different parameters
to test-tolerance [tol]
  setup
  ask people [set tolerance tol]
  repeat 200 [go]
  show (word "Tolerance " tol ": Components = " count-components " Polarization = " precision polarization-index 2)
end

; Simplified component counting for classroom use
to-report count-components
  ; Returns approximate number of opinion clusters
  let clusters 0
  let opinions sort-on [opinion] people
  let current-cluster-start 0
  
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
```

---

## Teaching Workflow

### Before Class
1. Test the complete model code in NetLogo
2. Create plots for "Opinion Distribution" and "Network Metrics"
3. Decide which activities to emphasize based on class time
4. Prepare parameter variations for demonstration

### Phase 1 (15-20 min)
- Live coding: Build setup and initial link creation
- Students write commands in Command Center
- Focus: Understanding `create-links-with`, `link-neighbors`, `end1`/`end2`

### Phase 2 (20-25 min)
- Introduce influence mechanism
- Live run the model, observe behavior
- Have students modify parameters (influence-rate)
- Focus: Links enable interaction; network structure matters

### Phase 3 (30-35 min)
- Present complete polarization model
- Run experiments with different parameters
- Use plots to track metrics over time
- Focus: How homophily + influence = emergent polarization

### Phase 4 (20-30 min)
- Guided critique: What does the model do well/poorly?
- Design experiment: Students propose a research question
- Discuss: Extensions that would make model more realistic
- Focus: Critical thinking about model validity and social theory

---

## Common Student Questions & Answers

**Q: Why does polarization happen?**
A: In this model, it emerges from two simple mechanisms: people preferentially connect to those similar to them (homophily), and then similar people influence each other further. Over time, this creates separated groups with divergent opinions.

**Q: Can we prevent polarization in this model?**
A: Yes! If you increase tolerance (so people are willing to connect across opinion differences), or add bridge-builders who connect different groups, polarization slows or stops.

**Q: Is this realistic?**
A: It captures some real mechanisms, but reality is more complex. Real polarization involves media, misinformation, leadership, economic interests, and other factors this model doesn't include.

**Q: What if opinions were 2D instead of 1D?**
A: Great question! You could create `[economic-opinion social-opinion]` and check distance in 2D space. Then homophily might work differently—people might agree on economics but disagree on social issues.

**Q: Why do some links break?**
A: When people become too different, the social tie strain becomes too high. In the real world, this happens when disagreements become too fundamental to maintain the relationship.

---

## Extensions for Advanced Students

1. **Multi-dimensional opinions**: Add economic-opinion and social-opinion
2. **Influence dynamics**: Make influence probabilistic and emotion-dependent
3. **Media effects**: Add external shocks that shift all opinions on some issues
4. **Leadership**: Create high-influence agents who persuade others more effectively
5. **Confirmation bias**: Make people preferentially read info confirming existing beliefs
6. **Interface design**: Test how platform algorithms affect polarization (only show content from like-minded people)
7. **Cross-cultural comparison**: How do different tolerance/influence-rate parameters reflect different societies?

---

## Assessment Options

### In-Class Assessment
- Can students write command to count network components?
- Can they explain why links broke in Phase 3?
- Can they predict what happens if tolerance increases?

### Experiment Assignment
- Design a hypothesis about what causes polarization
- Run 3 model variations
- Report findings with evidence from plots
- Reflect on model limitations

### Reflection Prompt
"Our model shows that polarization can emerge from simple mechanisms (homophily + influence + tie decay). What does this tell us about real-world polarization? What would our model need to include to be more realistic?"