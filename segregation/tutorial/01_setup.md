# 1. Setup Instructions

It is always a good practice to start your model by setting up the environment and initializing the agents. In this section, we will create the setup procedure for our segregation model.

To do so, we want to make sure we understand the model we are creating. The intention is to build a grid of agents, where each agent has a color (red or blue) and a preference for the color of its neighbors. If an agent is unhappy with its neighbors, it will move to a new location.

The grid has a certain percentage of empty spaces, which allows agents to move around. The model will also include a slider to adjust the percentage of similar neighbors an agent wants in order to be happy.

For these reasons, the setup procedure will need to:

1. Clear the environment
2. Define the color of the patches
3. Create a certain number of agents (turtles) with random colors (red or blue) in each patch using the density as probability for an agent to be created
4. Update the characteristics of the agents (color, shape, size) based on their neighborhood
5. Define the global variables and update them based on the initial setup

We will need some global variables to keep track of the model's state. These include:

- `similar-wanted`: The percentage of similar neighbors an agent wants to be happy (controlled by a slider)
- `density`: The percentage of patches that will be occupied by agents (controlled by a slider)
- `happy`: The number of happy agents in the model
- `unhappy`: The number of unhappy agents in the model

Notice that the `similar-wanted` and `density` variables will be controlled by sliders in the NetLogo interface, allowing us to easily adjust these parameters during the simulation.

:::{image} imgs/01_sliders.gif
:align: center
:::

Also, to account for the happiness of the turtles, we will create a variable called `happy?` for each turtle. This variable will be a boolean (true/false) indicating whether the turtle is happy or not based on its neighbors. We also want to make sure each agent (household) can keep track of the number of similar neighbors, different neighbors, and total neighbors it has. This will help us determine if the agent is happy or not.

Here is the code for the creation of global variables, the breed households, and the creation of attributes for our agents:

```ruby
globals [
    happy-households ; The number of happy agents in the model
    unhappy-households ; The number of unhappy agents in the model
    proportion-similarity ; proportion of similar households for the overall population
]

breed [households household] ; define a breed for the agents as a household

households-own [
  happy?          ; boolean indicating if the household is happy
  similar-neighbors ; number of similar neighbors
  different-neighbors ; number of different neighbors
  total-neighbors ; total number of neighbors
  similarity ; proportion of neighbors of the same color
]
```

Now we can create the `setup` procedure. This procedure will clear the environment, set the patch colors, create the agents, and initialize their attributes. Also, we want the `setup` to include the initialization of the global variables. Before we start, it is important to note that we will be using procedures (functions) to organize our code better. This will make it easier to read and maintain.

Here is how you can implement it:

```ruby
to setup
    clear-all ; clear the environment
    make-households ; procedure to create the households
    update-households ; procedure to update the shape of the households based on their happiness
    update-global-variables ; procedure to update the global variables
    reset-ticks ; reset the tick counter
end
```

This is the procedure to create the households:

```ruby
to make-households
ask patches [ 
    set pcolor white ; set all patches to white
    if random-float 100 < density [
      sprout-households 1 [ ; create a household with a probability defined by density
        set color one-of [red blue] ; randomly assign red or blue color
        set size 1 ; set the size of the household
      ]
    ]
  ]
end
```

For now, we will create empty procedures for `update-households` and `update-global-variables`. We will fill them in the next sections.

```ruby
to update-households
    ; This procedure will be filled in the next section
end

to update-global-variables
    ; This procedure will be filled in a later section
end
```

Finally, we need to create a button in the NetLogo interface to call the `setup` procedure.

:::{image} imgs/02_button.gif
:align: center
:::

Now you can run the `setup` procedure by clicking the button, and it will initialize the model with a grid of agents (households) randomly assigned as red or blue, based on the density slider.
