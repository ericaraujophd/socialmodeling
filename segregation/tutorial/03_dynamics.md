# 3. Dynamics

So far we have been working on the setup of the model and the update of the households. Now we need to define the dynamics of the model. The dynamics will be defined in a procedure called `go`. This procedure will be called every tick of the simulation. In this procedure, we will ask the unhappy agents to move to a new location. We will also update the shape of the agents based on their happiness and update the global variables.

```ruby
to go
  if all households [happy?] [ stop ] ; stop the simulation if all agents are happy
  move-unhappy-households ; procedure to move unhappy agents
  update-households ; update the shape of the agents based on their happiness
  update-global-variables ; update the global variables
  tick ; increment the tick counter
end
```

The procedure to move the unhappy agents is as follows:

```ruby
to move-unhappy-households
  ask households with [not happy?] [
    move-to one-of patches with [not any? households-here] ; move to a random empty patch
  ]
end
```

Finally, we need to fill the `update-global-variables` procedure. This procedure will count the number of happy and unhappy agents and update the global variables accordingly.

```ruby
to update-global-variables
  set happy-households count households with [happy?] ; count happy agents
  set unhappy-households count households with [not happy?] ; count unhappy agents
  set proportion-similarity (sum [similarity] of households) / count households
end
```

Now we can go back to the interface tab and create a button to call the `go` procedure. Make sure to set the button to "forever" so that it will keep calling the `go` procedure until all agents are happy. You can also create two buttons to call the `go` procedure (once and forever).

:::{image} imgs/interface-v1.png
:::

And this is the final code for our Segregation Model. You can now run the model and see how the agents move around the environment until they are all happy.

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

to setup
    clear-all ; clear the environment
    make-households ; procedure to create the households
    update-households ; procedure to update the shape of the households based on their happiness
    update-global-variables ; procedure to update the global variables
    reset-ticks ; reset the tick counter
end

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

to update-households
  ask households [
    set similar-neighbors count (households-on neighbors) with [color = [color] of myself]; count similar neighbors
    set different-neighbors count (households-on neighbors) with [color != [color] of myself] ; count different neighbors
    set total-neighbors similar-neighbors + different-neighbors ; total neighbors
    
    ifelse total-neighbors > 0 [ set similarity  (similar-neighbors / total-neighbors) * 100 ]
    [ set similarity 100  ] ; if no neighbors, consider happy
    
    set happy? (similarity >= similar-wanted)
    ifelse happy?   [ set shape "square" ][ set shape "x" ] ; set shape to x if unhappy and square if happy
  ]
end

to update-global-variables
  set happy-households count households with [happy?] ; count happy agents
  set unhappy-households count households with [not happy?] ; count unhappy agents
  set proportion-similarity (sum [similarity] of households) / count households
end

to go
  if all? households [happy?] [ stop ] ; stop the simulation if all agents are happy
  move-unhappy-households ; procedure to move unhappy agents
  update-households ; update the shape of the agents based on their happiness
  update-global-variables ; update the global variables
  tick ; increment the tick counter
end

to move-unhappy-households
  ask households with [not happy?] [
    move-to one-of patches with [not any? households-here] ; move to a random empty patch
  ]
end
```

:::{important} Download the Code
You can download the code for this model [here](code/segregation-model-v1.nlogox).
:::
