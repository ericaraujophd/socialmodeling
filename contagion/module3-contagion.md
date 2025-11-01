# Module 3: Contagion

## 📋 Weekly Breakdown

::::{tab-set}

:::{tab-item} Lecture 9
**Week 5: Tuesday, September 30**

*Heckman Library 406C*

**Session A:** *Collective behavior: from contagion to thresholds.*

- **Summary:**
  - Historical approaches: Le Bon's crowd psychology, modern collective behavior theory.
  - Threshold models: Granovetter's framework for understanding collective action.
  - Applications: riots, social movements, technology adoption.
- **Slides:** [Collective Behavior](slides/Collective_Behavior_Presentation.pptx)

**Session B (SRG):** Discussion of readings.

- **Summary:**
  - Mark Granovetter, "Threshold Models of Collective Behavior" (*AJS*, 1978).
  - Deliverable: SRG prep sheet due (per role).
:::

:::{tab-item} Lecture 10
**Week 5: Thursday, October 2**

*Heckman Library 406C*

**Session A:** Contagion models: a brief overview.

- **Summary:**
  - Overview of contagion models: SIR, SEIR, and agent-based approaches.
  - Discussions on limitations: norms, emotions, networks.
- **Slides:** [Contagion Models](https://www.beautiful.ai/player/-OaZoGXdCLpuBZxYlVP9)

**Session B (Lab):** Contagion Model in NetLogo.

- **Summary:** Building contagion models in NetLogo for spontaneous infections.
  - Code can be found [here](../contagion/codes/spontaneous.nlogox).
  - Slides with some of my research from the past (some of it might be outdated) [Link](slides/Social-Modeling.pdf)  
  - Deliverable: Lab memo #4 due next week.
:::

:::{tab-item} Lecture 11
**Week 6: Tuesday, October 7**

<!-- :::::{admonition} Note
:class: warning
::::: -->
**We won't have class on Tuesday, due to the Tech Week.**

<!-- *Heckman Library 406C*

**Session A:** *Social movements: mobilization, resources, grievances.*

- **Summary:**
  - Resource mobilization theory vs. grievance-based explanations.
  - Network effects in movement recruitment and organization.
  - Role of social media in contemporary movements.
- **Slides:** [Social Movements](slides/social-movements-lecture.pptx) -->

<!-- **Session B (SRG):** Discussion of readings.

- **Summary:**
  - Centola, D. (2010). The Spread of Behavior in an Online Social Network Experiment. Science, 329(5996), 1194–1197. 10.1126/science.1185231
    - [Link to Article](10.1126/science.1185231)
  - Centola, D., & Macy, M. (2007). Complex Contagions and the Weakness of Long Ties. American Journal of Sociology, 113(3), 702–734. 10.1086/521848
    - [Link to Article](10.1086/521848)
  <!-- - Charles Tilly, *Social Movements, 1768–2004*, Ch. 1.
  - Deliverable: SRG prep sheet due (per role). -->
:::

:::{tab-item} Lecture 12
**Week 6: Thursday, October 9**

*Heckman Library 406C*

**Session A (SRG):** Discussion of readings.

- **Summary:**
  - Centola, D. (2010). The Spread of Behavior in an Online Social Network Experiment. Science, 329(5996), 1194–1197. 10.1126/science.1185231
    - [Link to Article](10.1126/science.1185231)
  - Centola, D., & Macy, M. (2007). Complex Contagions and the Weakness of Long Ties. American Journal of Sociology, 113(3), 702–734. 10.1086/521848
    - [Link to Article](10.1086/521848)
  <!-- - Charles Tilly, *Social Movements, 1768–2004*, Ch. 1. -->
  - Deliverable: SRG prep sheet due (per role).
  - **Slides:** [Complex Contagion Networks](slides/Complex_Contagions_Networks.pptx)

**Session B (Lab):** Modeling the SI and SIR models.

- **Summary:**
  - We will build the SI and SIR models in NetLogo during this class. The starting point is the code from [previous lecture](../contagion/codes/spontaneous.nlogox).
  - Slides for the start of the class [can be found here](https://www.beautiful.ai/player/-ObAjfolFYaZefqIfcOl).
  - This is [where we left off](../contagion/codes/tutorial02.nlogox). We will continue building the SIR model next class.
:::

::::

---

## 📝 Assignments & Due Dates (Weeks 3–4)

::::{tab-set}

:::{tab-item} Lab Memo #4
**Due:** 10/16 before class | **Points:** 20 points

**Prompt (1-2 pages):**

Contagion model implementation & analysis

1. Implement a contagion model in NetLogo using the SEIR framework.
2. Analyze the model's behavior under different parameters (e.g., transmission rate, recovery rate).
3. Write your Lab Memo. You can [download the template in here](../resources/lab-memos/Lab_Memo_1_Worksheet.docx).
4. Make sure you add the codes you've changed, as well as interface modifications.
5. Submit your Lab Memo in PDF format through Moodle.

:::

:::{tab-item} Lab Memo #5
**Due:** 10/23 before class | **Points:** 20 points

**Prompt (1-2 pages):**

Contagion model implementation & analysis

1. Use the model we started in class (SIR) as a base.
2. Analyze the model's behavior under different parameters (e.g., transmission rate, recovery rate).
3. Build at least two new plots or monitors to track additional metrics (e.g., peak infection time, total recovered).
4. Write your Lab Memo. You can [download the template in here](../resources/lab-memos/Lab_Memo_1_Worksheet.docx).
5. Make sure you add the codes you've changed, as well as interface modifications.
6. Submit your Lab Memo in PDF format through Moodle.

:::
<!-- 
:::{tab-item} Lab Memo #5
**Due:** 10/16 before class | **Points:** 30 points

**Prompt (1-2 pages):**

1. Take the code for the Schelling model implemented in class in the link above (Lecture 6). Your task is to analyze the results of the model. You will run a batch experiment varying the parameters of the model (e.g., tolerance level, density of agents) and collect data on the outcomes (e.g., number of happy agents, segregation index). You can use the BehaviorSpace tool in NetLogo to set up and run the batch experiment. Here are some steps to guide you:
   - Define the parameters you want to vary and their ranges.
   - Set up the metrics you want to record during the simulations.
   - Run the batch experiment and collect the data.
   - Analyze the results using statistical or graphical methods. Look for patterns or trends in how the parameters affect the outcomes. You may use LLM tools to help you with the analysis. Make sure you are bringing up your own insights and interpretations also.
2. Write your Lab Memo. You can [download the template in here](../resources/lab-memos/Lab_Memo_1_Worksheet.docx).
3. Make sure you add the codes you've changed, as well as interface modifications.
4. Submit your Lab Memo in PDF format through Moodle.

::: -->
::::

<!-- ### Week 5 (Sep 30 & Oct 2)

| **Assignment Type** | **Details** | **Due Date** | **Weight** |
|:------------------:|:------------|:------------:|:----------:|
| 📖 **SRG Prep Sheet #4** | Granovetter threshold models reading | Tue Sep 30 (start of class) | Participation |
| 🧪 **Lab Memo #4** | Contagion model implementation & analysis | Thu Oct 9 (start of class) | 5% | -->

### Week 6 (Oct 7 & Oct 9)

| **Assignment Type** | **Details** | **Due Date** | **Weight** |
|:------------------:|:------------|:------------:|:----------:|
| 📖 **SRG Prep Sheet #5** | Centola Spread of Behavior in an Online Social Network readings | Thu Oct 9 (start of class) | Participation |
| 🎓 **Project Ideas Brainstorming** | Meet with your teams & brainstorm initial ideas | Thu Oct 9 | Project milestone (optional) |

---

## 📚 Reading and Extra Materials

### Required Readings

::::{tab-set}

:::{tab-item} Week 5 Reading
**Mark Granovetter (1978)**  
*"Threshold Models of Collective Behavior"*  
American Journal of Sociology, 83(6), 1420-1443.

**Key concepts:**

- Individual thresholds for participation
- Collective outcomes from individual decisions
- Applications to riots, strikes, and social movements
- Mathematical formalization of social influence

**Discussion questions:**

1. How do individual threshold distributions affect collective outcomes?
2. What role does information play in threshold models?
3. Can threshold models explain the unpredictability of social movements?
:::

:::{tab-item} Week 6 Reading
**Damon Centola (2010)**  
*"The Spread of Behavior in an Online Social Network Experiment"*  
Science, 329(5996), 1194–1197.  
[Link to Article](https://doi.org/10.1126/science.1185231)

**Damon Centola & Michael Macy (2007)**  
*"Complex Contagions and the Weakness of Long Ties"*  
American Journal of Sociology, 113(3), 702–734.  
[Link to Article](https://doi.org/10.1086/521848)

**Key concepts:**

- Complex contagion vs. simple contagion
- The role of network structure in behavior spread
- Weak ties vs. strong ties in social diffusion
- Experimental validation of contagion theories

**Discussion questions:**

1. How does complex contagion differ from simple contagion?
2. Why might weak ties be less effective for spreading behavior than for spreading information?
3. What are the implications for social movement organization and technology adoption?
:::

::::

### Supplementary Materials

::::{tab-set}

:::{tab-item} Videos

- How Behavior Spreads: The Science of Complex Contagions (Damon Centola) [Link](https://www.youtube.com/watch?v=j5PTukNU4gU)
- Nicholas Christakis, "Social Contagion" [Link](https://www.youtube.com/watch?v=NjgPJi-FBP4)
- Nicholas Christakis: The hidden influence of social networks [Link](https://www.youtube.com/watch?v=2U-tOghblfE)
- Feeling Their Vibes? Uncovering the Mystery of Emotional Contagion 🧠💫 [Link](https://www.youtube.com/watch?v=gjc-wH-r-UA)
- Are Your Emotions Contagious? | On Mirror Neurons [Link](https://www.youtube.com/watch?v=HTFdMwCXpMw)
:::

:::{tab-item} Articles

- **Centola, D.** (2018). ["How Behavior Spreads". Chapter 3: "Social Contagion"](https://press.princeton.edu/books/hardcover/9780691175317/how-behavior-spreads?srsltid=AfmBOop9fIQRI8p5_8EL2MteLDdIIbitq0gWFPS5yhASPYfTWtbPuP0r)
- **Watts, D. J.** (2002). ["A simple model of global cascades on random networks"](https://www.pnas.org/doi/10.1073/pnas.082090499)
- **González-Bailón, S.** (2011). ["The dynamics of protest recruitment through online social networks"](https://www.nature.com/articles/srep00197)
- **Steinert-Threlkeld, Z. C.** (2017). ["Spontaneous collective action: Peripheral mobilization during the Arab Spring"](https://ideas.repec.org/a/cup/apsrev/v111y2017i02p379-403_00.html)

:::

:::{tab-item} NetLogo Models

- **Virus** (Biology section) - Basic epidemic spreading
- **Rebellion** (Social Science section) - Threshold-based uprising
- **Diffusion on a Directed Network** - Information spread
- **Preferential Attachment** - Network formation dynamics

:::

:::{tab-item} Online Resources

- [Complexity Explorer: Social Dynamics](https://www.complexityexplorer.org/)
- [NetLogo Models Library: Social Science](http://ccl.northwestern.edu/netlogo/models/)
- [Stanford Encyclopedia: Social Epistemology](https://plato.stanford.edu/entries/epistemology-social/)
- [Collective Behavior Research Group](https://www.collectivebehavior.org/)

:::

::::
