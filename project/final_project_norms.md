---
title: Final Project
subtitle: Modeling Social Norm Formation and Fragility
---

## Project Summary

Students will design an **agent-based model of social norms**—how they emerge, spread, and break down in a community. The project asks: *How do shared norms of cooperation, fairness, or trust develop in societies, and what forces destabilize them?*

This model invites students to blend technical ABM design with social theory concepts like Durkheim's collective conscience, Goffman's micro-interactions, or Elinor Ostrom's work on commons governance.

:::{admonition}
:class: warning
If you want to work in a different idea, feel free to propose it to the instructors! We narrowed the focus to norms because it ties well to social theory and allows for rich modeling opportunities.
:::

---

## Project Overview: Six Steps

| Step | Phase | Description | Timeline |
|------|-------|-------------|----------|
| 1 | **Brainstorming** | Teams develop initial ideas and identify social phenomena | Nov 6 |
| 2 | **Idea Pitch** | Teams present 5–10 min pitches to the class | Nov 11 |
| 3 | **Design & Literature Review** | Teams structure their model and discuss relevant theory | Nov 13-20 |
| 4 | **Lab Sessions** | ~4 coding/building sessions where teams develop their model | Nov 25-Dec 4 |
| 5 | **Model Presentation** | Teams demonstrate working models to the class | Dec 9-11 |
| 6 | **Final Report** | Written synthesis with code, results, and reflection | Finals week (Dec 13) |

---

## Step 1: Brainstorming (Nov 6)

### What Students Should Do

- Form teams of **3–4 students**.
- Brainstorm social phenomena that involve **norm emergence, spread, or breakdown**.
- Consider phenomena from:
  - Everyday life (e.g., campus culture, study group dynamics, online communities)
  - Historical/social contexts (e.g., protest movements, cultural shifts, organizational behavior)
  - Theory from the course (e.g., Durkheim's collective conscience, Ostrom's commons governance, Goffman's micro-interactions)

### Expectations for Step 1

- **Scope**: Ideas should be **specific enough to model** but **flexible enough to simplify** where needed.
- **Theory link**: Teams should identify **at least one social theorist** whose framework will guide their model.
- **Feasibility**: The model should be buildable in **4–6 weeks** using NetLogo.

### Guidance Questions

- What question about norms are you trying to answer?
- Who are the agents in your system, and what are they trying to do?
- How do agents interact, and what causes norms to emerge or change?
- Under what conditions might norms become fragile or collapse?

Answer these questions and submit them as a one-page (500-words maximum) brainstorming document by Nov 9.

---

## Step 2: Idea Pitch (Nov 11)

### Presentation Content

Each team delivers a **5–10 minute presentation** covering:

1. **The Research Question** (1–2 min)
   - What social phenomenon are you modeling?
   - Why does it matter?

2. **Initial Concept** (2–3 min)
   - What agents are in your system?
   - What are the key behaviors or interactions?
   - What could cause norms to stabilize or break down?

3. **Theory Connection** (1–2 min)
   - Which social theorist(s) inform your model?
   - How will their ideas guide your modeling choices?

4. **First Prototype Sketch** (1 min)
   - Pseudocode, flowchart, or diagram showing model logic

### Expectations for Step 2

- Teams should demonstrate **clear thinking** about their problem space.
- Presentations should show **connection to course material** (readings, discussions, prior modules).
- Teams should be **open to feedback** and ready to refine their ideas.

Submit your slides presentation on Moodle .

### Pitch Deliverables

- **Slides** by **November 11 before class**
- **Peer feedback form** (provided by instructors)
- **Instructors feedback** on feasibility and scope

---

## Step 3: Design & Literature Review (Nov 13–20)

### Work for Step 3

After receiving feedback, teams move into **design and research**:

1. **Structure Your Model**

   - Define agent properties (attributes, initial states)
   - Outline agent behaviors (rules, decision logic)
   - Describe interactions (how agents affect each other)
   - Specify parameters and environment (landscape, resources, etc.)
   - Identify possible "shocks" or perturbations to test norm fragility

2. **Deep Dive into Social Theory**

   - Re-read relevant theorist(s) with your model in mind
   - Extract key concepts and translate them into model rules
   - Document **why each modeling choice connects to theory**
   - Consider critiques: what does your model capture? What does it miss?

3. **Literature Review**

   - Find **2–3 empirical or computational papers** related to your phenomenon
   - Summarize relevant findings and modeling approaches
   - Identify where your model builds on, differs from, or critiques prior work

### Design & Literature Deliverables

- **Pseudocode or flowchart** showing model logic (pseudocode + conceptual diagram) - one page
- **Theory memo** (1–2 pages) mapping theoretical concepts to model rules
- **Parameter table** specifying all model inputs and their ranges
- **Annotated bibliography** (at least 3 sources: 1–2 theory + 1–2 empirical)
- **Literature Review Summary** (1–2 pages, shared with class in SRG-style discussion)

These deliverables are due by **Nov 21** and will guide your coding in Step 4.


---

## Step 4: Lab Sessions (~4 sessions, Nov 25–Dec 4)

### Work for Step 4

Teams move into **hands-on coding and model building**:

**Lab 1 (Nov 25):** Model Setup & Basic Behavior

- Implement agent initialization and basic properties
- Code one or two core behaviors (e.g., agents observe neighbors, copy behavior)
- Test that agents move, interact, or update correctly

**Lab 2 (Dec 2):** Norm Emergence & Measurement

- Implement norm-tracking mechanisms (e.g., What % of agents follow a rule?)
- Add measurement/plotting of norm strength over time
- Run test simulations and check for expected patterns

**Lab 3 (Nov 25–Dec 4):** Shocks & Robustness

- Implement "shock" or perturbation (e.g., resource depletion, new agents entering)
- Run parameter sweeps to test sensitivity
- Analyze which conditions lead to norm stability vs. collapse

**Lab 4 (Dec 2–4):** Refinement & Final Tweaks

- Fix bugs, optimize code for clarity
- Run final simulation set
- Prepare data/visualizations for presentation

### Expectations for Step 4

- **Working code** (NetLogo, Python Mesa, or agreed-upon platform)
- **Clean, commented code** with clear variable names and logic
- **Simulation outputs** (plots, statistics, example runs)
- **Lab notes** (brief write-up of what worked, what didn't, what you learned)

### In-Class Support

- Instructors and peer teams available for **debugging and design discussion**
- Time for **peer code review** and feedback
- Access to **example models** and reference code as needed

### Lab Deliverables

- **Working model** (code repository or file)
- **Sample output** (plots, screenshots, video of simulation)
- **Lab journal** (brief notes from each session)

To be submitted on **December 9** before class.

---

## Step 5: Model Presentation (Dec 9–11)

### What to Present

Each team gives a **10–15 minute presentation** demonstrating:

1. **Live Model Demonstration** (3–5 min)
   - Show the model running with different parameter settings
   - Highlight key behaviors and norm dynamics
   - Explain what the visuals/outputs mean

2. **Key Findings** (2–3 min)
   - What surprised you?
   - Under what conditions do norms emerge or collapse?
   - How do your results connect to theory?

3. **Reflection on Modeling** (1–2 min)
   - What did you learn about the phenomenon by building this model?
   - What are the limits of your model? What did you have to simplify?
   - How might this model inform our understanding of real-world challenges?

4. **Q&A** (1–2 min)
   - Peers and instructors ask clarifying questions

### Expectations for Step 5

- **Clear, polished presentation** (slides + live demo)
- **Honest discussion of limitations** (a hallmark of good science)
- **Evidence of iterative refinement** (you learned and improved along the way)
- **Enthusiasm and engagement** with the material

### Presentation Deliverables

- **Presentation slides**
- **Live or video demo** of the model
- **Handout or supplementary material** (optional but encouraged)

---

## Step 6: Final Report (Finals Week – Dec 13)

### Report Structure

**1. Title and Abstract** (¼ page)

- Concise summary of research question, model, and key findings

**2. Introduction & Motivation** (1 page)

- Why does this social phenomenon matter?
- What question are you answering?
- How does your model contribute to understanding?

**3. Social Theory & Model Design** (2–3 pages)

- Which theorist(s) inform your model and why?
- How do theoretical concepts map to model rules?
- Pseudocode, diagrams, or detailed logic explaining agents, interactions, parameters

**4. Implementation & Computational Methods** (1–2 pages)

- Platform used (NetLogo, Python Mesa, etc.)
- Code structure (brief overview or appendix reference)
- How did you measure norms? (metrics, visualizations)

**5. Results & Findings** (2–3 pages)

- What patterns emerged?
- How sensitive is the model to parameter changes?
- Which conditions lead to norm stability vs. collapse?
- Plots, tables, or screenshots supporting your findings

**6. Interpretation & Real-World Connections** (1–2 pages)

- What do these results tell us about the real-world phenomenon?
- How do your findings relate to empirical research or theory?
- What are the limitations of your model? What did you simplify?

**7. Reflection: Imperfect Models in a Fallen World** (½–1 page)

- How does Smedes' concept of "imperfect models" apply to your work?
- What ethical or philosophical questions does modeling norms raise?
- What would a "better" model look like, and why is it hard to build?

**8. References & Appendices** (as needed)

- Bibliography (APA or Chicago format)
- Full code (if not already submitted)
- Additional plots or data tables

### Expectations for Step 6

- **7–10 pages** (single-spaced, including figures)
- **Academic writing style** (clear, organized, evidence-based)
- **Strong connection between theory and modeling**
- **Honest discussion of limitations and uncertainty**
- **Proper citations** for all sources (code, data, theory, prior models)

### Report Deliverables

- **Final Report** (PDF or Word document)
- **Code** (documented and runnable)
- **Data/Results** (plots, statistics, or supplementary files)

---

## Why Doing This Work?

- **Hands-on**: Requires real modeling work (parameter design, simulation runs, debugging).
- **Interdisciplinary**: Merges social theory with computation in a concrete way.
- **Theological/Philosophical Depth**: Students reflect on the "imperfect models" Smedes highlights—what are the limits of modeling moral/social order in a fallen world?
- **Scalable**: Strong students can push into advanced territory (network science, machine learning for calibration), while everyone can complete a meaningful baseline project.

---

## Evaluation Criteria

See **Course Policies** → **Grading Rubric** for the breakdown of project components and point values. Each milestone will be evaluated on:

- **Clarity & Communication**: Is your idea, design, and results clearly explained?
- **Technical Depth**: Does your model work? Is the code well-organized?
- **Theory Integration**: How well do you connect social theory to modeling choices?
- **Critical Reflection**: Do you honestly discuss what your model reveals and what it misses?
- **Collaboration & Teamwork**: (If applicable) How well did your team work together?
