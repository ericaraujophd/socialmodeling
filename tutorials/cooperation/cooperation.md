---
title: "Cooperation"
authors:
    - name: Eric Araujo
date: 2025-10-23
---

This module will handle the implementation of a few cooperation models using Netlogo. We'll start with the classic Prisoner's Dilemma and then explore more complex scenarios like the Iterated Prisoner's Dilemma and public goods games. The goal is to understand the dynamics of cooperation and the factors that influence it.

## Prisoner's Dilemma

The Prisoner's Dilemma is a classic example of a cooperation dilemma in game theory. In this scenario, two players must decide whether to cooperate with each other or betray each other (defect). The outcomes depend on the choices made by both players:

- If both players cooperate, they receive a moderate reward.
- If one player defects while the other cooperates, the defector receives a high reward while the cooperator receives a low reward.
- If both players defect, they both receive a low reward.

This creates a situation where each player must weigh the potential benefits of cooperation against the risks of betrayal. The dilemma illustrates the challenges of achieving cooperation in competitive environments and has been widely studied in various fields, including economics, political science, and biology.

### Mathematically Representing the Payoff Matrix

Let's consider that cooperation incurs a cost $c$, on the cooperator, and confers a benefit $b$ on the recipient. The payoff matrix for the Prisoner's Dilemma can be represented as follows:

|               | Cooperate          | Defect             |
|---------------|--------------------|--------------------|
| **Cooperate** | Player 1: $b - c$<br>Player 2: $b - c$ | Player 1: $-c$<br>Player 2: $b$ |
| **Defect**    | Player 1: $b$<br>Player 2: $-c$ | Player 1: $0$<br>Player 2: $0$ |

Where:

- $b$ is the benefit received from the other player's cooperation.
- $c$ is the cost incurred by cooperating.
- $0$ is the payoff when both players defect.
- $b > c > 0$ to ensure the dilemma structure.

Considering this payoff matrix, we can see that the dominant strategy for both players is to defect, leading to a suboptimal outcome for both. However, if both players choose to cooperate, they can achieve a better collective outcome.

Also, we can calculate the payoffs of agents who always cooperate (ALLC) and those who always defect (ALLD) in a population. Our model will represent agents distributed in a lattice, where each agent interacts with its neighbors. The lattice will be composed of L x L cells, and each cell will contain one agent, with toroidal boundary. In this case, $N = L \times L$.

Each agent is purely cooperative (ALLC) or purely defective (ALLD). When created, agents have a probability $p_0$ of being cooperative, otherwise, they are defective. Benefit (b) and cost (c) are defined as global variables.

Individually, each agent will keep track of their strategy, and its payoff.


## Stages of the Game

The game will have two stages:

1. **Game Play Stage:** Each agent plays the Prisoner's Dilemma with its 8 neighbors and accumulates payoffs based on the interactions.
2. **Evolutionary Stage:** After all interactions, agents update their strategies based on the payoffs received. An agent may adopt the strategy of a neighbor with a higher payoff, simulating natural selection.

### Game Play Stage

In the game play stage, the payoffs for each interaction will be calculated based on the strategies of the interacting agents. The total payoff for each agent will be the sum of the payoffs from all interactions with its neighbors.

To calculate the payoff, each agent will interact with its 8 neighbors (Moore neighborhood). The number of cooperative neighbors is $n_C$. The number of defective neighbors is $n_D = 8 - n_C$. This way, the payoff of an ALLC agent is:


$$\text{Payoff}_{\text{ALLC}} = n_C \cdot (b - c) + n_D \cdot (-c) = n_C \cdot b - 8 \cdot c$$

The payoff of an ALLD agent is:

$$\text{Payoff}_{\text{ALLD}} = n_C \cdot b + n_D \cdot 0 = n_C \cdot b$$

### Evolutionary Stage

In the evolutionary stage, each agent will compare its payoff with that of its neighbors. If a neighbor has a higher payoff, the agent may adopt the neighbor's strategy with a probability proportional to the difference in payoffs. This simulates the process of natural selection, where successful strategies are more likely to be adopted.

:::{admonition} Alternative Update Rule
:class: tip
A simpler way of implementing the evolutionary stage is to have each agent adopt the strategy of the neighbor with the highest payoff, if that payoff is greater than its own. This deterministic approach can lead to faster convergence but may reduce the diversity of strategies in the population.
:::

Now we can move to the implementation of the model in NetLogo.
