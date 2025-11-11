## Phase 4: Evaluation & Analysis

**Duration**: 20-30 minutes
**Goals**: Students critically evaluate the model, design experiments, and connect to social theory

### Learning Objectives

By the end of Phase 4, students should be able to:
- Critically evaluate what the model does and doesn't explain
- Identify model assumptions and limitations
- Design controlled experiments to test research questions
- Propose realistic extensions to the model
- Connect model insights to social theory

### Why This Phase Matters

Building a model is easy. Understanding what it means is hard. Phase 4 is where students develop critical thinking about models:

- **What does this model capture well?** (What mechanisms does it demonstrate effectively?)
- **What does it oversimplify?** (What complexity did we ignore?)
- **What's missing?** (What factors would change the outcome?)
- **So what?** (What should we do with these insights?)

### Evaluation Framework

#### 1. Structural Analysis: Network Topology

**Question**: How does the network structure reveal polarization?

**Metrics to examine**:
- **Number of components**: How many separated groups formed?
- **Largest component size**: Are people fragmented or still mostly connected?
- **Average path length**: How many hops to get from one random person to another?
- **Clustering coefficient**: Within groups, how densely connected are people?

**Code to explore**:
```netlogo
to-report count-components
  ; Count number of separated components
  ; (simplified version for classroom)
  report estimate-components
end

to-report largest-component-size
  ; How many people in the largest connected cluster?
  ; (Advanced: would require graph traversal)
end
```

**Discussion**:
- "In a polarized society, what should we expect for these metrics?"
- "A low number of large components suggests successful polarization"
- "High clustering coefficient means tight within-group connections"

#### 2. Behavioral Analysis: Opinion Dynamics

**Question**: How do opinions change over time?

**Metrics to examine**:
- **Polarization-index**: Standard deviation of opinions (high = polarized)
- **Number of opinion clusters**: How many distinct groups?
- **Convergence rate**: How fast do opinions stabilize?
- **Final opinion range**: Do groups span full spectrum or cluster?

**Visualization**:
```netlogo
to plot-opinion-distribution
  histogram [opinion] of people
end
```

Ask students:
- "Is the histogram unimodal or bimodal?" (Polarization = bimodal)
- "Are the two peaks symmetric?" (Real polarization often is)
- "How much overlap is there between groups?" (More overlap = less polarization)

#### 3. Mechanism Analysis: What Drives What?

**Question**: Which mechanisms matter most?

Test each mechanism independently:

**Experiment A: Just Influence (no Homophily, no Tie Decay)**
```netlogo
; Modify form-new-links to do nothing
; Modify decay-weak-links to do nothing
; Run 100 ticks
; Result: opinions converge but no fragmentation
```

**Experiment B: Just Homophily (no Influence, no Tie Decay)**
```netlogo
; Modify update-opinions-through-influence to do nothing
; Modify decay-weak-links to do nothing
; Run 100 ticks
; Result: network fragments but opinions don't change
```

**Experiment C: All Three Mechanisms**
```netlogo
; Run as normal
; Result: polarization emerges
```

**Discussion**:
- "Can polarization happen with just one or two mechanisms?"
- "Which mechanism is most important?"
- "Are all three necessary for realistic polarization?"

#### 4. Model Critique: What Does It Do Well? What's Missing?

**What the Model Captures Well**:

1. **Self-reinforcement**: Once people are similar, they become MORE similar
2. **Network fragmentation**: Interaction networks can break into separate components
3. **Homophily as driver**: Preference for similarity can amplify polarization
4. **Feedback loops**: Simple mechanisms create complex dynamics

**What the Model Oversimplifies**:

1. **Single-dimensional opinions**: Real politics is multidimensional (economic, social, cultural, etc.)
   - Extension: Use 2D or 3D opinion space
   - Question: "Would polarization look different with multidimensional opinions?"

2. **No external information**: Real people encounter media, news, campaigns
   - Extension: Add "news events" that shift opinions exogenously
   - Question: "How would media coverage of polarizing events affect this model?"

3. **Deterministic influence**: Real influence involves emotion, trust, credibility
   - Extension: Add influencer status; some people influence more than others
   - Question: "What if 1% of people are 10x more influential?"

4. **No cognitive biases**: Real people have confirmation bias, backfire effect, etc.
   - Extension: Make people resistant to information contrary to beliefs
   - Question: "Would cognitive biases speed up or slow down polarization?"

5. **Symmetric opinion space**: Real polarization often has distinct ideologies, not just a spectrum
   - Extension: Add categorical opinions (not just 0-100)
   - Question: "Would categorical opinions create more stable groups?"

6. **No leadership effects**: Real polarization often has charismatic figures who drive it
   - Extension: Create "leader" agents who shift others' opinions non-reciprocally
   - Question: "How many leaders would it take to prevent polarization?"

7. **Static population**: Real societies have immigration, generations, demographic change
   - Extension: Add new people with random opinions; remove old people
   - Question: "Would demographic turnover prevent or accelerate polarization?"

### Classroom Activities - Phase 4

#### Activity 4.1: Mechanism Decomposition (8 minutes)

Run experiments testing each mechanism:

```netlogo
; Experiment 1: Just Influence
; (disable form-new-links and decay-weak-links)
setup
repeat 100 [go]  ; Only influence-through-links runs
show polarization-index
show average-opinion-distance
```

Results: 
- Polarization-index decreases (opinions converge)
- Average-opinion-distance also decreases (linked people become similar)
- BUT network structure stays the same

```netlogo
; Experiment 2: Just Homophily
; (disable update-opinions-through-influence and decay-weak-links)
setup
repeat 100 [go]  ; Only form-new-links runs
show polarization-index
show network-density
```

Results:
- Network-density increases (more links form)
- But links only between already-similar people
- Opinions don't change

```netlogo
; Experiment 3: All Three
setup
repeat 100 [go]
show polarization-index
show network-density
show cross-cutting-links
```

Results: Polarization emerges

**Discussion**:
- "Homophily alone doesn't create opinion change"
- "Influence alone doesn't create fragmentation"
- "You need both (plus tie decay) for realistic polarization"
- "Which mechanism is most important for policy?"

#### Activity 4.2: Design Your Own Experiment (10 minutes)

Guide students through hypothesis-driven experimentation:

**Example Research Question 1: "Can tolerance be too high?"**
- Hypothesis: Very high tolerance prevents polarization
- Test: Run model with tolerance = 1, 5, 10, 20, 40, 80, 100
- Measure: Final polarization-index for each
- Visualize: Plot polarization vs. tolerance
- Interpret: Is there a critical point? Is the relationship linear?

**Example Research Question 2: "Do bridge-builders actually help?"**
- Hypothesis: Bridge-builders reduce polarization
- Control: No bridge-builders
- Treatment: 5% bridge-builders added at tick 0
- Treatment2: 5% bridge-builders added at tick 50 (late intervention)
- Measure: Final polarization-index for each
- Interpret: Does timing matter? How much effect do bridge-builders have?

**Example Research Question 3: "What's the minimum link formation rate for polarization?"**
- Hypothesis: Below some rate, polarization can't occur
- Test: Run with link-formation-rate = 0.01, 0.05, 0.10, 0.15, 0.20
- Measure: Does polarization reach polarization-index > 20?
- Interpret: What's the critical rate?

**Student Task**: Choose one research question and run the experiment.

#### Activity 4.3: Model Limitations Discussion (7 minutes)

Pose these critical questions:

1. **Validity**: "To what extent does this model explain real polarization?"
   - Evidence for model: Homophily is well-documented; influence through interaction is real
   - Limitations: Real polarization involves media, institutions, material interests
   - Context: Model is better at explaining online communities than entire societies

2. **Specificity**: "For what contexts would this model apply best?"
   - Strong: Online social media communities (homophily is amplified, external info is curated)
   - Moderate: Subgroups within organizations or institutions
   - Weak: Entire nation-states (too many other factors)

3. **Causation**: "Does this model prove that homophily CAUSES polarization?"
   - No: It shows homophily CAN cause polarization under certain conditions
   - Alternative explanations: People might polarize first, THEN preferentially connect
   - Real dynamics likely involve feedback between opinions and connections

4. **Assumptions**: "What assumptions did we make?"
   - Linear opinion space (0-100)
   - Opinions change continuously (not suddenly)
   - All people have same mechanisms (uniform model)
   - No external shocks or interventions

#### Activity 4.4: Extension Challenge (5 minutes)

Propose an extension challenge:

**Challenge 1: Multidimensional Opinions**
"Right now, opinions are 1D (0-100). What if people had two independent opinion dimensions (e.g., economic and social)? How would polarization look different?"

Hints:
- Use `[econ-opinion social-opinion]` for each person
- Distance = `sqrt((econ1 - econ2)^2 + (social1 - social2)^2)`
- Tolerance now applies to total distance

**Challenge 2: External Shocks**
"What if news events suddenly shifted everyone's opinion? Add a random shock every 25 ticks that moves all opinions toward an extreme."

Hints:
- `ask people [set opinion opinion + (random 20) - 10]`
- Run this every 25 ticks
- Does polarization recover? Does it get worse?

**Challenge 3: Leadership**
"What if 1% of people are 'leaders' who influence 10x more than others? Would this prevent or accelerate polarization?"

Hints:
- Create `is-leader?` property
- Multiply influence from leaders by 10
- Multiply influence on leaders by 0.1

**Challenge 4: Resistance to Influence**
"What if people resist influence that contradicts their existing views (confirmation bias)? Make people only influenced by those they already partially agree with."

Hints:
- Before influencing, check if neighbor is different by > 30 points
- If so, ignore their opinion
- Does confirmation bias prevent or accelerate polarization?

### Assessment - Phase 4

Students should be able to:
- Describe what the model does and doesn't explain
- Identify key assumptions and their implications
- Design an experiment to test a research question
- Interpret results from parameter variations
- Propose a realistic extension to make the model more sophisticated
- Discuss the connection between model and real-world polarization

### Reflection Prompt

Have students write a short reflection (1-2 paragraphs):

"Our model shows that polarization can emerge from simple mechanisms (homophily + influence + tie decay). What does this tell us about real-world polarization? What would the model need to include to be more realistic? How might these insights inform policy solutions?"

---

## Teaching Workflow

### Before Class

**Preparation (2-3 hours before)**:
1. Test the complete model code in NetLogo
2. Create plots for "Opinion Distribution" and "Network Metrics"
3. Prepare buttons for each main procedure (setup, go, highlight-neighbors, etc.)
4. Decide which activities to emphasize based on class time
5. Pre-run some scenarios to know what to expect
6. Prepare parameter variations for demonstration

**Materials**:
- NetLogo installed on classroom computers
- Starter code files (one for each phase)
- Handouts with learning objectives and key questions
- Laptop/projector for demonstration

### Phase 1 (15-20 minutes total)

**Instructor** (5 min):
- Live code the setup procedure
- Show students what a simple network looks like
- Ask: "How many links exist? Why?"

**Students** (10-15 min):
- Write commands in Command Center to modify links
- Practice `link-neighbors`, `end1`, `end2`
- Explore the network visually

**Wrap-up** (2-3 min):
- "Links represent connections; we'll use them to model interaction"

### Phase 2 (20-25 minutes total)

**Instructor** (5 min):
- Live code the influence and tie-decay procedures
- Run the model for 50 ticks
- Show how opinions change and links break

**Students** (10 min):
- Run the model and observe
- Complete Activities 2.1-2.3
- Modify parameters and see effects

**Discussion** (5-10 min):
- "What happened to the network?"
- "Why did some links break?"
- "What would happen if we added new links?"
- → Leads into Phase 3

### Phase 3 (30-35 minutes total)

**Instructor** (5-10 min):
- Present the three mechanisms again
- Show complete code (or build incrementally)
- Introduce measurement reporters

**Students** (15 min):
- Run the full model
- Observe emergent polarization
- Complete Activities 3.1-3.3

**Experimentation** (10 min):
- Students test different parameters
- See how outcomes change
- Predict what will happen before running

**Wrap-up** (2-3 min):
- "This is polarization emerging from simple rules"

### Phase 4 (20-30 minutes total)

**Guided Critique** (10 min):
- Instructor leads discussion of model limitations
- What does it capture? What's missing?
- When would you trust it? When would you doubt it?

**Experimentation** (10 min):
- Students design and run their own experiment
- Test a research question they propose
- Share findings with class

**Reflection** (5-10 min):
- Individual or group reflection on what model teaches
- Connection to real-world polarization
- Discussion of solutions/interventions

### Full Class Schedule

**60-minute class**:
- Phase 1: 15 min
- Phase 2: 20 min
- Phase 3: 20 min
- Q&A: 5 min

**90-minute class** (recommended):
- Phase 1: 15 min
- Phase 2: 20 min
- Phase 3: 35 min (more experimentation)
- Phase 4: 15 min
- Q&A: 5 min

**Two 60-minute classes** (most ideal):
- Class 1: Phases 1-2
- Class 2: Phases 3-4

---

## Technical Reference

### NetLogo Primitives Reference

#### Link Creation
- `create-link-with turtle`: Create single link to one turtle
- `create-links-with agentset`: Create links to multiple turtles
- `create-link-from turtle`: Create incoming link (directed only)

#### Link Access
- `link-neighbors`: Reports agentset of all connected turtles
- `my-links`: Reports all links connected to this turtle
- `links`: Reports all links in the world

#### Link Properties
- `end1`, `end2`: The two turtles at each end of a link
- Custom properties defined in `*-link-breed` declarations

#### Link Inspection
- `link who1 who2`: Access specific link between turtles
- `any? my-links with [...]`: Conditional link checking

#### Link Modification
- `set color`, `set thickness`, etc.: Modify link appearance
- `set` any custom property

#### Link Removal
- `die`: Remove the link

### Common Code Patterns

**Create conditional links**:
```netlogo
ask people [
  ask other people with [abs ([opinion] of myself - opinion) < tolerance] [
    if not link-neighbor? self [
      create-link-with myself
    ]
  ]
]
```

**Check if two turtles are linked**:
```netlogo
to-report link-neighbor? [target]
  report target != self and any? link-neighbors with [self = target]
end
```

**Count cross-cutting links**:
```netlogo
to-report cross-cutting-links
  let count-cross 0
  ask social-bonds [
    let diff abs ([opinion] of end1 - [opinion] of end2)
    if diff > 30 [ set count-cross count-cross + 1 ]
  ]
  report count-cross
end
```

**Weighted average from neighbors**:
```netlogo
let total-weight 0
let weighted-sum 0
ask link-neighbors [
  let weight 1 - (abs ([opinion] of myself - opinion) / 100)
  set total-weight total-weight + weight
  set weighted-sum weighted-sum + (opinion * weight)
]
let weighted-avg weighted-sum / total-weight
```

### Debugging Tips

**"Links aren't showing up"**:
- Make sure you have `reset-ticks` before `go`
- Check that `undirected-link-breed` or `directed-link-breed` is defined
- Verify people are actually created

**"My influence procedure isn't working"**:
- Check that `link-neighbors` is inside `ask people` context
- Use `show` to debug: `show [opinion] of link-neighbors`
- Remember that link-neighbors returns an agentset, not a single turtle

**"Opinions aren't changing"**:
- Make sure you're actually setting the opinion value
- Check the math: `set opinion (1 - rate) * opinion + rate * avg`
- Are people isolated (no link-neighbors)?

**"Links aren't breaking"**:
- Make sure you're calling `decay-weak-links` every tick
- Check the threshold: is `opinion-diff > 40`?
- Use `show` to debug: `ask social-bonds [show abs ([opinion] of end1 - [opinion] of end2)]`

---

## Common Student Questions

### Understanding Concepts

**Q: Why do we use links instead of just checking proximity?**
A: Because we want to model choice-based relationships, not spatial proximity. Links represent social connections that people choose, not just who happens to live nearby.

**Q: Is homophily realistic?**
A: Yes! Research consistently shows people preferentially connect with similar others. Online, it's even stronger because algorithms amplify homophily.

**Q: Why does polarization happen if nobody wants it?**
A: Because it emerges from individual choices that each seem reasonable. Linking with similar people is sensible. But globally, it fragments society.

**Q: Can this model explain real polarization?**
A: It captures some mechanisms but misses others (media, institutions, material interests). It's a simplified model, useful for understanding how networks matter, but not a complete explanation.

### Technical Questions

**Q: What's the difference between `link-neighbors` and `other-end`?**
A: `link-neighbors` gives you all connected turtles as an agentset. `other-end` doesn't exist in NetLogo. If you need the turtle at one end of a specific link, use `end1` or `end2`.

**Q: Can there be multiple links between the same two turtles?**
A: No. NetLogo prevents duplicate links automatically.

**Q: How do I access just the outgoing links (directed)?**
A: Use `my-out-links` for links I initiated, `my-in-links` for links others initiated.

**Q: Can I make links thicker or thinner?**
A: Yes: `ask links [set thickness 2]`. Thickness can be any number; try values 0.1-3.

### Research Questions

**Q: What happens if we make people more open-minded (higher tolerance)?**
A: Less polarization. More diverse links form. Opinions stay closer together.

**Q: What happens if we have people who refuse to influence (stubbornness)?**
A: More polarization. Even if linked, stubborn people don't change much, so ties break more often.

**Q: Can we prevent polarization?**
A: Yes, several ways: increase tolerance, add bridge-builders, reduce link-formation-rate, introduce regular external shocks. But each has costs/tradeoffs.

**Q: How is this different from Phase 2?**
A: Phase 2 only had influence and tie decay (people already knew each other). Phase 3 adds homophily (people choose who to link with). This choice is what drives polarization.

---

## Extended Resources

### Recommended Readings for Instructors

**General Polarization**:
- Sunstein, C. R. (2002). "The Law of Group Polarization." *University of Chicago Law Review*. [Group polarization effect]
- Pariser, E. (2011). *The Filter Bubble*. [Algorithmic polarization]

**Homophily**:
- McPherson, M., Smith-Lovin, L., & Cook, J. M. (2001). "Birds of a Feather: Homophily in Social Networks." *Annual Review of Sociology*. [Foundational homophily paper]

**Network Science**:
- Barabási, A. L. (2016). *Network Science*. [Network structure and dynamics]
- Granovetter, M. (1973). "The Strength of Weak Ties." *American Journal of Sociology*. [Bridge-builders and weak ties]

**Agent-Based Modeling**:
- Epstein, J. M., & Axtell, R. (1996). *Growing Artificial Societies*. [Foundations of ABM]
- Railsback, S. F., & Grimm, V. (2019). *Agent-Based and Individual-Based Modeling*. [Practical ABM guide]

### Classroom Resources

**For Students**:
- NetLogo User Manual: https://ccl.northwestern.edu/netlogo/docs/
- NetLogo Dictionary: https://ccl.northwestern.edu/netlogo/docs/dictionary.html
- Community Models Library: https://modelingcommons.org/

**For Instructors**:
- NetLogo Tutorials: https://ccl.northwestern.edu/netlogo/bind/
- Links Tutorial: https://ccl.northwestern.edu/netlogo/bind/primitive/links.html
- link-neighbors Primitive: https://ccl.northwestern.edu/netlogo/bind/primitive/link-neighbors.html

### Extension Ideas

1. **Multi-dimensional opinions**: Model opinions as [x, y] coordinates instead of single value
2. **External events**: Add random shocks that shift all opinions
3. **Selective exposure**: Make people ignore information from those they disagree with
4. **Leadership dynamics**: Create influencers who have 10x more persuasive power
5. **Demographic change**: Introduce new people with diverse opinions; remove old people
6. **Platform effects**: Model how different algorithms change network structure
7. **Cross-cultural comparison**: Run same model with different default parameters
8. **Historical simulation**: Run model for 500 ticks; intervene at different time points

---

## Assessment Rubric

### Phase 1 Assessment

**Emerging**: Can run setup and observe the network but doesn't understand how to create or modify links.

**Proficient**: Can create links, access link-neighbors, and modify link properties. Can predict what happens when you change parameters.

**Advanced**: Can explain the relationship between link density, network connectivity, and simulation speed. Understands implications for modeling choices.

### Phase 2 Assessment

**Emerging**: Runs the model but doesn't understand why links break or opinions change.

**Proficient**: Can explain influence and tie decay mechanisms. Correctly predicts what happens if you change influence-rate or decay-threshold.

**Advanced**: Understands why local similarity and global fragmentation can coexist. Can design an experiment to test a hypothesis about influence.

### Phase 3 Assessment

**Emerging**: Runs the polarization model but doesn't see polarization or understands it only vaguely.

**Proficient**: Observes polarization clearly. Can interpret all four metrics (polarization-index, network-density, average-opinion-distance, cross-cutting-links). Can run parameter variations and describe results.

**Advanced**: Understands the feedback loop (homophily → influence → tie decay → more homophily). Can design multi-part experiments testing interactions between parameters.

### Phase 4 Assessment

**Emerging**: Can identify model limitations but struggles with what they mean or how to address them.

**Proficient**: Can clearly articulate what the model captures and what it misses. Can design a controlled experiment to test research question. Can propose realistic extension.

**Advanced**: Critically evaluates model assumptions and their implications. Designs sophisticated experiments testing interactions. Proposes extensions grounded in real social science literature.

---

## Conclusion

This module teaches that **networks matter**. The structure of who talks to whom, combined with simple interaction dynamics, can create large-scale social outcomes that nobody intended. Understanding this is crucial for:

- **Technology**: Designing platforms that don't accidentally polarize
- **Policy**: Knowing when interventions can work and when they're too late
- **Citizenship**: Recognizing how our individual choices aggregate into collective patterns
- **Modeling**: Learning to think about complex systems by building them

By building this model themselves, students develop deep understanding of a critical social phenomenon. They also learn skills—NetLogo programming, experimental design, critical evaluation—that transfer to many domains.

Most importantly, they learn the power of **imperfect models**: not to perfectly predict the future, but to understand the mechanisms that shape our world.
