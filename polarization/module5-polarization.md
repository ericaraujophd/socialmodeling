# Module 5: Polarization

:::{warning}
This page is under construction. It is just a draft that will receive a lot of changes yet.
:::

Welcome to the Polarization Models module! This module explores how groups form opposing viewpoints, how moderate positions erode, and how social identities become divided. We'll examine the mechanisms that drive political, social, and ideological polarization using computational modeling approaches.

## Overview

Polarization models help us understand one of the most pressing challenges of contemporary society: how and why groups become increasingly divided in their beliefs, values, and behaviors. Through agent-based modeling, we'll explore opinion dynamics, the role of social networks, media influence, and institutional factors that contribute to societal polarization and potential interventions.

```{note}
**Module Duration:** 2 weeks | *Estimated time: 8-12 hours*
```

---

## Student Learning Objectives (SLOs)

By the end of this module, students will be able to:

::::{tab-set}

:::{tab-item} Core
- Articulate limiting assumptions or limitations to the conclusions that can be drawn from the use of these methods and identify appropriate and inappropriate uses of such methods, as informed by a Reformed, Christian perspective.
- Provide students with a sense of the nature and limits of scientific knowledge and the kinds of ethical questions that surround scientific research and its dissemination (revisited in the context of polarization, ethics, and justice).
:::

:::{tab-item} Conceptual
- Define different types of polarization (ideological, affective, social sorting)
- Explain mechanisms that drive opinion polarization and group formation
- Analyze the role of social networks, media, and algorithms in polarization
- Understand the relationship between polarization and democratic governance
:::

:::{tab-item} Technical Skills
- Implement opinion dynamics models (voter model, Hegselmann-Krause, etc.)
- Model the effects of network structure on opinion formation
- Simulate media influence and algorithmic filtering on belief systems
- Analyze polarization metrics and measurement approaches
:::

:::{tab-item} Critical Thinking
- Evaluate competing explanations for political and social polarization
- Assess the effectiveness of interventions designed to reduce polarization
- Critique the assumptions and limitations of polarization models
- Connect polarization theory to contemporary political and social challenges
:::

:::{tab-item} Communication
- Present complex polarization dynamics to diverse audiences
- Discuss the implications of polarization research for democratic society
- Articulate the tension between diversity and social cohesion
- Engage constructively with politically sensitive topics and research
:::
::::

---

## 📚 Slides and Readings

```{admonition} Course Materials
:class: note

**Lecture Slides:**
- **Lecture 1:** [Introduction to Polarization](slides/polarization-intro.pdf)
- **Lecture 2:** [Opinion Dynamics Models](slides/opinion-dynamics.pdf)
- **Lecture 3:** [Network Effects and Echo Chambers](slides/networks-polarization.pdf)
- **Lecture 4:** [Media, Algorithms, and Information](slides/media-polarization.pdf)

**Supplementary Videos:**
- 🎥 [Political Polarization Explained](https://youtu.be/example) (16 min)
- 🎥 [Echo Chambers and Filter Bubbles](https://youtu.be/example) (14 min)
- 🎥 [Opinion Dynamics Visualization](https://youtu.be/example) (12 min)
```

### Required Readings

```{dropdown} Core Reading Materials
:open:

1. **Hegselmann, R., & Krause, U. (2002).** *Opinion dynamics and bounded confidence models, analysis, and simulation.* Journal of Artificial Societies and Social Simulation, 5(3).
   - 📖 [PDF Download](readings/hegselmann-krause-2002.pdf)
   - 🎯 Focus on: Bounded confidence and opinion clustering

2. **Sunstein, C. R. (2001).** *Echo chambers: Bush v. Gore, impeachment, and beyond.* Princeton University Press. (Selected chapters)
   - 📖 [PDF Download](readings/sunstein-2001-excerpts.pdf)
   - 🎯 Focus on: Group polarization and deliberative democracy

3. **Bail, C. A., et al. (2018).** *Exposure to opposing views on social media can increase political polarization.* Proceedings of the National Academy of Sciences, 115(37), 9216-9221.
   - 📖 [PDF Download](readings/bail-2018.pdf)
   - 🎯 Focus on: Empirical evidence of social media polarization effects

4. **Mason, L. (2015).** *"I disrespectfully agree": The differential effects of partisan sorting on social and issue polarization.* American Journal of Political Science, 59(1), 128-145.
   - 📖 [PDF Download](readings/mason-2015.pdf)
   - 🎯 Focus on: Distinction between issue and affective polarization
```

---

## 📝 Homework

```{admonition} Assignment 1: Basic Opinion Dynamics
:class: important

**Due:** End of Week 1 | **Points:** 25 points

**Objectives:**
- Implement and analyze basic opinion dynamics models
- Explore the conditions that lead to consensus vs. polarization
- Understand the role of confidence bounds and influence mechanisms

**Tasks:**
1. Implement the Hegselmann-Krause bounded confidence model
2. Explore different confidence threshold values and their effects
3. Compare with other opinion dynamics approaches (voter model, etc.)
4. Analyze equilibrium outcomes and convergence patterns

**Deliverables:**
1. NetLogo opinion dynamics model with parameter controls
2. Systematic analysis of confidence threshold effects
3. Visualization of opinion evolution over time
4. Short report (3-4 pages) on model behavior and insights

**Resources:**
- [Opinion Dynamics Template](homework/opinion-dynamics-template.nlogo)
- [Parameter Space Exploration Guide](homework/parameter-exploration.md)
- [Visualization Techniques](homework/opinion-visualization.pdf)
```

```{admonition} Assignment 2: Network Polarization and Policy Analysis
:class: important

**Due:** End of Week 2 | **Points:** 40 points

**Objectives:**
- Model polarization on different network structures
- Analyze the role of homophily and social influence
- Explore interventions for reducing polarization
- Connect findings to contemporary polarization challenges

**Tasks:**
1. Implement opinion dynamics on various network topologies
2. Model homophily (like-minded connection preferences)
3. Test interventions: bridge-building, diverse exposure, fact-checking
4. Analyze polarization metrics and measurement approaches
5. Develop recommendations for addressing contemporary polarization

**Deliverables:**
1. Network-based polarization model with multiple mechanisms and documentation
2. Comparison of polarization outcomes across network types
3. Evaluation of intervention effectiveness with policy analysis
4. Technical report (6-8 pages) with contemporary applications
5. Brief presentation (5 minutes) of key findings and recommendations

**Resources:**
- [Network Polarization Template](homework/network-polarization-template.nlogo)
- [Homophily Implementation Guide](homework/homophily-guide.md)
- [Intervention Strategies Database](homework/polarization-interventions.pdf)
- [Policy Analysis Framework](homework/policy-analysis.md)
```

---

## 🌟 Extra Materials

```{admonition} Additional Resources
:class: note

**Interactive Demos:**
- 🖥️ [Political Polarization Simulator](http://example.com/polarization) - Interactive model exploration
- 🖥️ [Opinion Dynamics Lab](https://www.complexity-explorables.org/) - Complexity science visualizations
- 🖥️ [Echo Chamber Visualization](http://example.com/echo) - Network-based opinion formation

**Tools and Software:**
- 💻 **NetworkX:** Python library for network analysis and opinion dynamics
- 📊 **Gephi:** Network visualization with polarization analysis plugins
- 🎨 **D3.js:** Web-based visualization of opinion dynamics
- 📈 **R igraph:** Statistical network analysis and modeling

**Study Groups and Office Hours:**
- 👥 **Study Group Sessions:** Wednesdays 6-8 PM, Science Building 180
- 🕐 **Instructor Office Hours:** Tuesdays & Fridays 2-4 PM
- 💬 **Course Discord:** #polarization-models channel for constructive discussion
```

### Historical Context

```{dropdown} The Study of Polarization

**Early Foundations:**
- Sherif, M. (1936). *The psychology of social norms.* Harper & Brothers.
- Asch, S. E. (1951). Effects of group pressure upon the modification and distortion of judgments. *Journal of Social Psychology*, 33(2), 181-195.
- Festinger, L. (1957). *A theory of cognitive dissonance.* Stanford University Press.

**Political Science Perspectives:**
- Downs, A. (1957). *An economic theory of democracy.* Harper & Row.
- Converse, P. E. (1964). The nature of belief systems in mass publics. *Critical Review*, 18(1-3), 1-74.
- Fiorina, M. P., & Abrams, S. J. (2008). Political polarization in the American public. *Annual Review of Political Science*, 11, 563-588.

**Computational Approaches:**
- Axelrod, R. (1997). The dissemination of culture: A model with local convergence and global polarization. *Journal of Conflict Resolution*, 41(2), 203-226.
- Deffuant, G., et al. (2000). Mixing beliefs among interacting agents. *Advances in Complex Systems*, 3(01n04), 87-98.
```

### Real-World Applications

```{dropdown} Understanding Contemporary Polarization

**Political Polarization:**
- Congressional voting patterns and partisan sorting
- Public opinion on policy issues over time
- Electoral competition and geographic polarization
- Media consumption and selective exposure

**Social Media and Technology:**
- Algorithmic filtering and recommendation systems
- Online echo chambers and information bubbles
- Misinformation spread and fact-checking effectiveness
- Platform design and user behavior

**Cultural and Social Issues:**
- Science communication and public understanding
- Religious and cultural value conflicts
- Immigration attitudes and intergroup contact
- Climate change and environmental policy

**Discussion Questions:**
- Is political polarization necessarily harmful to democracy?
- How do social media algorithms contribute to polarization?
- What role should platforms play in moderating content?
- Can exposure to opposing views actually increase polarization?

**Current Research:**
- Computational social science approaches to polarization measurement
- Cross-cultural studies of opinion dynamics
- Intervention design and evaluation
- Long-term trends in social and political division
```

---

## 🗓️ Weekly Schedule

```{admonition} Module Timeline
:class: note

| Week | Topic | Readings | Assignments |
|------|-------|----------|-------------|
| **Week 1** | Opinion Dynamics & Bounded Confidence | Hegselmann & Krause (2002), Classical Models | Opinion Dynamics Due |
| **Week 2** | Networks, Media & Policy Applications | Sunstein (2001), Mason (2015), Bail et al. (2018) | Network Analysis Due |
```

---

## 📞 Getting Help

```{admonition} Need Support?
:class: tip

- **Quick Questions:** Use the Moodle class forums
- **Technical Issues:** Visit our troubleshooting guide
- **Conceptual Help:** Attend office hours
- **Accessibility:** Contact the instructors for accommodations
```
