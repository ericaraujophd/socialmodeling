---
title: "Phase 1: Link Fundamentals"
date: 2025-11-11
---

## Learning Objectives

By the end of this phase, you will be able to:

- Create links between turtles using `create-links-with`.
- Access connected neighbors using `link-neighbors`.
- Reference link endpoints using `end1` and `end2`.
- Modify link properties dynamically.
- Understand the difference between undirected and directed links.

## Conceptual Frame

Before we model polarization, let's learn how to represent relationships in NetLogo. Links are how we show that two people are connected—they have a relationship. Think of your own social network: you have friends, and your friends have friends. Links represent those friendships.

Links are the innovation that makes this module different from previous modules. In earlier modules (segregation, contagion), agents interacted based on proximity—who was nearby. Now, agents interact through choice. People link to whom they want to connect with. This opens up entirely new possibilities for modeling social phenomena where relationships matter.

## Key Concepts in Phase 1

### Undirected vs. Directed Links

**Undirected links** represent symmetric relationships (friendship, collaboration, mutual following):

- If A is linked to B, B is automatically linked to A
- Use `undirected-link-breed` for these

**Directed links** represent asymmetric relationships (following, parent-child, authority):

- If A links to B, B is not automatically linked to A
- Use `directed-link-breed` for these

In the polarization model, we use **undirected links** because friendship and social influence are symmetric.

### Link Properties

Just like turtles can have properties, links can too:

```ruby
undirected-link-breed [social-bonds social-bond]
social-bonds-own [strength]
```

This creates a link type called `social-bonds` with a property called `strength`. This allows us to track characteristics of relationships, not just their existence.

### Accessing Neighbors

Once links exist, accessing connected turtles is easy:

```ruby
ask turtle 0 [
  ask link-neighbors [set color green]  ; Highlight all neighbors
]
```

`link-neighbors` is incredibly useful—it returns an agentset of all turtles connected to the asking turtle.

### Starter Code for Phase 1

```ruby
breed [people person]
undirected-link-breed [social-bonds social-bond]

people-own [opinion]
social-bonds-own [strength]

to setup
  clear-all
  
  ; Create 20 people with random opinions
  create-people 20 [
    set opinion random 100
    setxy random-xcor random-ycor
    set size 1.5
    set color blue
  ]
  
  ; Each person creates links to 3 random others
  ask people [
    create-social-bonds-with n-of 3 other people [
      set strength random-float 1.0  ; Random strength 0-1
      set color grey
    ]
  ]
  
  reset-ticks
end

to go
  tick
end
```

After creating this code, add a Setup and Go button to run the model. When you click Setup, you should see 20 blue turtles connected by grey links.

:::{admonition} Torus Settings
:class: tip
Make sure your world settings have "Wrap edges" disabled (Torus) so that turtles can interact with their immediate neighbors without wrapping around the edges of the world.
:::

## Classroom Activities - Phase 1

### Activity 1.1: Explore the Network

Students run the setup and explore:

- "How many links were created?" (Should be 30: 20 people × 3 links ÷ 2 for undirected).
- Write: `ask links [set color red]` to turn all links red.
- Write: `ask links [set thickness 0.5]` to make links thicker.
- Write: `ask links [set thickness thickness * 2]` repeatedly to watch links grow.

**Learning point**: Links are agents too; they can be modified just like turtles.

### Activity 1.2: Understanding link-neighbors

Add a command button called `highlight-neighbors` with this code:

```ruby
to highlight-neighbors
  ask people [set color blue]  ; Reset all to blue
  ask one-of people [
    ask link-neighbors [set color green]
  ]
end
```

Answer:

- "What does `link-neighbors` show us?" <!--  (All turtles connected to that turtle). -->
- "Why is this useful?" <!--  (Lets agents access those they interact with). -->
- "What if I click repeatedly?" <!--  (Different turtles get highlighted; they have different neighbors). -->

**Learning point**: `link-neighbors` gives us access to interaction partners.

### Activity 1.3: Accessing Link Endpoints

Add this code to your Code tab and create a button `show-link-info` to call it:

```ruby
to show-link-info
  let example-link one-of links
  ask example-link [
    show (word "Link between turtle " end1 " and turtle " end2)
    show (word "Strength: " strength)
  ]
end
```

Answer:

- "How do we refer to the two turtles at each end of a link?" <!-- (Using `end1` and `end2`) -->
- "Why would we need to access endpoints?" <!-- (To examine the turtles connected by a link, to check if they should still be connected) -->
- "Can we ask the endpoints questions? How?" <!-- (Yes: `ask end1 [set color red]`) -->

**Learning point**: Links connect turtles, and we can reference those turtles through `end1` and `end2`.

### Activity 1.4: Creating Links Conditionally

Add this code to your Code tab and create a button `create-links-by-color` to call it:

```ruby
to create-links-by-color
  ask people with [color = blue] [
    create-social-bonds-with other people with [color = blue] [
      set strength 0.8
      set color blue
    ]
  ]
end
```

Answer:

- "What does this do?" <!-- (Creates links only between blue people) -->
- "What if I run it multiple times?" <!-- (Some links already exist; no duplicates are created) -->
- "How could we prevent duplicate links?" <!-- (Check if link already exists before creating) -->

**Learning point**: We can use conditions to control link formation.

---

### Assessment - Phase 1

Students should be able to:

- Write code to count total links: `count links`
- Write code to find the most-connected person: `max-one-of people [count link-neighbors]`
- Write code to color links based on link strength: `ask links [set color scale-color red strength 0 1]`
- Explain what `link-neighbors` returns and why it's useful

---

## Final Code

The final code for Phase 1 [can be found here](codes/polarization-phase1.nlogox).

---
