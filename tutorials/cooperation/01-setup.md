---
title: "1. Setup"
date: 2025-10-23
---

## Global Variables

We will need three global variables for this model:

- `b` (benefit): The benefit conferred to the recipient when an agent cooperates.
- `c` (cost): The cost incurred by the cooperator when they choose to cooperate.
- `p0` (initial cooperation probability): The probability that a newly created agent is a cooperative agent (ALLC) rather than a defective agent (ALLD).

We will also create a slider to define the size of the lattice (L x L). The total number of agents (N) will be calculated as `N = L * L`.

Our initial lattice will have size 31. So, $N = 31 \cdot 31 = 961$ agents.

These four variables will be adjustable in the interface.

:::{figure} imgs/01-interface.png
:::

For our code, I'm defining the limits for the interface sliders as follows:

- benefit (`b`): min 0, max 10, initial value 5, step 1
- cost (`c`): min 0, max 10, initial value 1, step 1
- prob-coop (`p0`): min 0, max 1, initial value 0.5, step 0.01
- lattice (`L`): min 10, max 100, initial value 31, step 1

In our setup we will need to make sure that `b > c > 0`. We can do this by adding a check in the `setup` procedure that resets the values if they don't satisfy this condition. Also, we need to configure the size of the world to be a toroidal lattice of size L x L.

```ruby
to setup
  clear-all
  if not (benefit > cost and cost > 0) [
    set benefit 5
    set cost 1
  ]
  resize-world 0 (lattice - 1) 0 (lattice - 1) ; resize the world
  ; rest of setup code...
end
```

## Creating Agents

Our agents will be a new breed called `players`. Each agent will have two attributes: `strategy` (which can be "ALLC" or "ALLD") and `payoff` (to keep track of the agent's accumulated payoff).

```ruby
breed [players player]
players-own [
    strategy  ; "ALLC" or "ALLD"
    payoff    ; accumulated payoff
]
```

We will create `N = L x L` agents and distribute them in a lattice structure. Each agent will be assigned a strategy (ALLC or ALLD) based on the probability `p0`.

```ruby
to make-players
    ask patches [
        sprout-players 1 [
            set strategy ifelse-value (random-float 1 < prob-coop) [ "ALLC" ] [ "ALLD" ]
            set payoff 0
            set shape "circle"
        ]
    ]
end
```

A procedure to recolor the agents is needed after each strategy update.

```ruby
to recolor-players
    ask players [
        set color ifelse-value (strategy = "ALLC") [ green ] [ red ]
    ]
end
```

So far, our code looks like this:

```ruby
breed [players player]

players-own [
    strategy  ; "ALLC" or "ALLD"
    payoff    ; accumulated payoff
]

to setup
  clear-all
  ;; checking the validity of the values for benefit and cost
  if not (benefit > cost and cost > 0) [
    set benefit 5
    set cost 1
  ]
  resize-world 0 (lattice - 1) 0 (lattice - 1) ; resize the world to match the slider lattice
  make-players
  recolor-players
  reset-ticks
end

to make-players
    ask patches [
        sprout-players 1 [
            set strategy ifelse-value (random-float 1 < prob-coop) [ "ALLC" ] [ "ALLD" ]
            set payoff 0
            set shape "circle"
        ]
    ]
end

to recolor-players
    ask players [
        set color ifelse-value (strategy = "ALLC") [ green ] [ red ]
    ]
end
```

:::{admonition} Code so far
:class: tip
The code we have so far is available [through this link](codes/A-Setup.nlogox).
:::
