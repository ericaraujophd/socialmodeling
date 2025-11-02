# 1. Spontaneous Contagion

The first model we will build is a simple contagion model where individuals can spontaneously become infected. This could represent a disease that can be contracted from the environment, or a behavior that individuals can adopt on their own.

## Model Overview

In this model, each individual has a certain probability of becoming infected at each time step. The infection can spread through direct contact with infected individuals or through environmental exposure. For this model we will assume that the world is populated by a number of individuals defined in the interface's slider `num-people` and placed randomly in a 2D grid. They move randomly around the grid.

## Key Components

1. **Agent Representation**: Each individual is represented as an agent with an infection status.
2. **Infection Dynamics**: Each agent has equal probability of becoming infected at each time step.
3. **Environmental Factors**: There are no explicit environmental factors in this model.

## Implementation Steps

1. Define the agent properties and behaviors.
2. Set up the grid environment and initialize the population.
3. Implement the contagion dynamics and update rules.
4. Run simulations and collect data on infection spread.
