---
title: Coding Polarization using Links
subtitle: Teaching NetLogo Links Through Polarization
date: 2025-11-11
---

:::{figure} imgs/header.png
Rembrandt van Rijn style painting representing polarization in society, with two groups facing each other across a divide. Created by ChatGPT.
:::

---

## Course Context

This material is designed for HNRS-251-A: Agent-Based Modeling & Social Theory at Calvin University. It builds student understanding of NetLogo links from basic mechanics to a full polarization model, aligned with the course philosophy of creating imperfect models to better understand social phenomena.

---

## Why This Model Matters

Think about your own social circles. You probably spend most time with people who share your views. Your close friends likely agree with you on politics, values, or lifestyle choices. This seems natural—we gravitate toward people like us.

But here's the question: **What happens over time when everyone does this?**

If you only interact with people who already agree with you, do you become MORE confident in your views? Do the differences between your group and other groups grow larger? Does it become harder to find common ground?

This is the puzzle of **political polarization**, and it's one of the most pressing social problems today. Our model won't explain everything about why societies divide—but it will show us how polarization can emerge from simple, local interactions.

---

## The Core Mechanism: Three Simple Rules

Our model is built on three mechanisms that happen in real social networks:

### 1. **Homophily**: "Birds of a Feather Flock Together"

When people meet someone new, they're more likely to form a connection if that person shares similar views. On social media, you follow people whose posts you agree with. In neighborhoods, you befriend neighbors with similar values. This preference for similarity is called **homophily**.

**In our model**: Each person will try to form new connections with others whose opinions are close to their own.

### 2. **Influence**: "We Become Like Those We Spend Time With"

Once you're connected to someone, they influence you. Not through coercion, but through conversation. You hear their perspective, they hear yours, and both of you adjust slightly. This process is mutual and subtle—it's just what happens when people interact.

**In our model**: Connected people influence each other. If your friends average opinion is 60 and yours is 50, you'll move slightly toward 60.

### 3. **Tie Decay**: "We Drift Apart When We Disagree Too Much"

But there's a limit. If you and a friend become too different, the relationship strains. You stop talking. The friendship fades. Eventually, you're no longer connected.

**In our model**: When two connected people's opinions drift too far apart, their link breaks.

---

## What Makes This Interesting?

You might think: "Okay, people connect with similar people and influence each other. Of course they end up in groups." But here's what's surprising:

**These three simple, local mechanisms can create dramatic, large-scale polarization.**

People aren't deliberately trying to polarize society. Nobody wakes up thinking, "How can I make my society more divided?" Instead, they're just doing the natural things humans do—connecting with people they like, being influenced by those connections, and letting relationships fade when they diverge.

Yet from these individual choices emerges a fragmented society where:

- Different groups have almost no contact.
- People within groups think more and more alike.
- The opinion gap between groups grows wider.
- Finding common ground becomes nearly impossible.

This is **emergent polarization**—it emerges from the bottom up, even though no one intended it.

---

## What We'll Learn By Building This Model

### Technical Skills

- How to represent social networks in NetLogo using **links**.
- How to make agents interact through their connections.
- How to measure network properties (fragmentation, density, polarization).
- How to run experiments to test what factors matter most.

### Social Science Insights

1. **Structure shapes behavior**: The networks we're embedded in influence who we become.
2. **Local actions have global consequences**: Individual preferences aggregate into large-scale patterns.
3. **Feedback loops amplify**: Similarity → connection → increased similarity → wider gaps (positive feedback).
4. **Prevention is key**: Once polarized, it's hard to depolarize; better to prevent it early.
5. **Intervention points exist**: We can identify what reduces polarization (bridge-builders, increased tolerance, exposure to diversity).

### Critical Thinking

- How does this model capture real polarization? How does it oversimplify?
- What assumptions are we making? Are they justified?
- What would we need to add to make it more realistic?
- What does this tell us about solutions to polarization?

---

## How We'll Build It Step-by-Step

### Phase 1: Learn the Tools

First, we need to learn how **links** work in NetLogo. Links are how we represent connections. We'll create a simple network and learn to manipulate it.

**Key question**: How do we make turtles interact through their connections?

### Phase 2: Add Interaction

Then we'll add the rules for influence and tie decay. We'll watch what happens when people influence each other through their network connections.

**Key question**: Do people's opinions converge or diverge? What determines which?

### Phase 3: Add Homophily

Finally, we'll add the crucial mechanism: people form new connections with similar others. This is where the magic happens—this is where you'll see polarization emerge.

**Key question**: Can simple homophily + influence + tie decay create the large-scale polarization we see in society?

### Phase 4: Experiment and Evaluate

We'll design experiments to test what matters. We'll ask:

- What if people were more tolerant?
- What if we had bridge-builders?
- What if tolerance varied?
- Can we prevent polarization?

Then we'll think critically about what this means for understanding real-world polarization.

---

## The Philosophy Behind This Model

This course is built on a specific philosophy: **We learn about the world by building imperfect models of it.**

Our model won't be "true"—it will be a simplification. It won't include media, leadership, economics, psychology, or a thousand other factors that contribute to real polarization.

But that's okay. The point isn't to perfectly replicate reality. The point is to:

1. **Isolate mechanisms**: By removing everything except the essentials, we can understand which mechanisms matter most
2. **Build intuition**: Seeing a model run helps us understand dynamics that are hard to reason through in your head
3. **Test ideas**: We can ask "what if" questions and get clear answers
4. **Identify interventions**: By understanding the mechanisms, we can identify where to intervene

We're not trying to predict the future. We're trying to understand our world better by building it ourselves, piece by piece.

---

## What You'll See Happen

When you run this model, here's roughly what happens:

**Early on (ticks 0-30)**

- People form connections randomly, mostly with similar others.
- Opinions adjust slightly through influence.
- The network looks fairly connected—most people can reach most other people through links.

**Middle phase (ticks 30-100)**

- New links form between similar people (homophily effect).
- Weak links break between dissimilar people (tie decay).
- Opinion clusters start to form—groups of similar people.
- The network starts to fragment into separate components.

**End state (ticks 100+)**

- The network has broken into distinct groups.
- Within each group, opinions are very similar.
- Between groups, opinions are very different.
- Almost no links cross between groups.
- The system has reached a stable polarized state.

And here's the key: **This happened even though we never told anyone to polarize, and everyone was just following simple rules.**

---

## Questions to Keep in Mind

As we build this model, keep asking yourself:

1. **Does this match reality?** "Do people really form links preferentially with similar others? Do we really influence each other this way?"

2. **What's missing?** "What real-world factors would change this model's behavior?"

3. **So what?** "If this model is right, what should we do about polarization in society?"

4. **How do I know it's not just garbage in, garbage out?** "How can I trust that what emerges from the model tells us something real?"

These aren't rhetorical questions—they're the kinds of questions we'll return to at every phase.

---

## Connection to Social Theory

This model connects to several important ideas in social science:

- **Homophily** (social network research): People preferentially form ties with similar others
- **Echo chambers** (media studies): When we only hear voices like our own, we become more extreme
- **Polarization dynamics** (political science): Institutional and social structures can amplify differences
- **Emergent complexity** (complexity science): Simple local rules create complex global patterns
- **Agent-based modeling** (computational social science): We understand systems by simulating them

By building and experimenting with this model, you're engaging with real social science research. The mechanisms in our model are based on actual studies. The patterns we observe have been documented in real societies.

---

## What Success Looks Like

By the end of this module, you should be able to:

- **Build**: Write code to create links, iterate over neighbors, implement dynamic tie breaking.
- **Explain**: Describe how homophily + influence + tie decay leads to polarization.
- **Evaluate**: Run experiments, interpret data, and assess what the model does and doesn't explain.
- **Critique**: Identify model limitations, propose more realistic extensions, and think about implications for society.
- **Apply**: Design your own agent-based model to explore a social phenomenon you care about.

---

## Let's Begin

Ready to build a model of polarization? Let's start with the fundamentals: understanding how links work in NetLogo.

When you finish, you'll have a model that demonstrates one of the most important social dynamics of our time. More importantly, you'll understand more *how* to think about complex social systems by building models.

Let's go.
