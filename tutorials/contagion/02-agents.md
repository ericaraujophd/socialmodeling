# 2. Agents properties and rules

In this first model, our agents will have one property accounting for their infection status. They can be either susceptible (S) or infected (I). At each time step, each susceptible agent has a probability of becoming infected, defined by the slider `infection-probability`. Once infected, agents remain infected for the duration of the simulation.

## Characteristics of the agents

The agents will be moving randomly around the grid at a constant speed defined by the slider `speed`. At each time step, they will move to a random place based on their heading and speed. The heading is a random number, and the maximum angle change is defined by the slider `angle`.

For that reason, I will create the sliders for our simulation as our first step:

```{figure} imgs/01-sliders.png
:align: center
:label: sliders
Sliders for the spontaneous contagion model.
```

Remember that all these sliders are global variables, and you can access them from anywhere in your code. You can use them to define agent properties, behaviors, or environmental factors.

Now, let's create the agents. I want to use a new breed to make sure it reflects better the context of the model. The breed will be called `people`. Later, we will use the `create-people` command to create a number of agents defined by the slider `num-people`. Each agent will be represented as a turtle in NetLogo, and we will set their initial properties and behaviors.

```ruby
breed [people person]  ; Define a new breed called 'people'
people-own [infected?]  ; Each person has an 'infected?' property
```

For this model, I will use circles to represent the agents. Susceptible agents will be green, and infected agents will be red. You can use the `set color` command to change the color of the agents based on their infection status.

## Infection dynamics

Also, we need to start the simulation with some initial infected agents. We can use a new slider `initial-infected` to define how many agents will start as infected. We will randomly select that number of agents and set their `infected?` property to `true`.

```ruby
to setup-infected
    if initial-infected > num-people [
        set initial-infected 1
    ]
    if initial-infected < 1 [
        set initial-infected 1
    ]
    ask n-of initial-infected people [
        set infected? true
        set color red
    ]
end
```

The code above will be used to set the initial infected agents. It checks if the number of initial infected agents is valid (not more than the total number of agents and at least one). Then, it randomly selects that number of agents and sets their `infected?` property to `true` and changes their color to red. It will be used in the `setup` procedure.

We also need a method to infect susceptible agents. We can create a procedure called `infect` that will be called at each time step. This procedure will check if an agent is susceptible and, if so, will generate a random number between 0 and 1. If this number is less than the `infection-probability`, the agent will become infected.

```ruby
to infect
    ask people with [not infected?] [
        if random-float 1 < infection-probability [
            set infected? true
            set color red
        ]
    ]
end
```

The code above will be used to infect susceptible agents. It checks if an agent is not infected and generates a random number between 0 and 1. If this number is less than the `infection-probability`, the agent becomes infected, and its color changes to red. It will be called in the `go` procedure.

## Agent movement

Finally, we need to implement the movement of the agents. We can create a procedure called `move` that will be called at each time step. This procedure will update the position of each agent based on its heading and speed.

```ruby
to move
    ask people [
        right random angle
        left random angle
        forward speed
    ]
end
```

The code above will be used to move the agents. It updates the heading of each agent by a random angle and moves it forward by the distance defined by the `speed` slider. It will be called in the `go` procedure.

## Putting it all together

Now, we can put everything together in the `setup` and `go` procedures. The `setup` procedure will initialize the simulation, create the agents, set their initial properties, and call the `setup-infected` procedure. The `go` procedure will be called at each time step and will call the `move` and `infect` procedures.

```ruby
to setup
    clear-all
    create-people num-people [
        set shape "circle"
        set size 1.5
        set color green
        set infected? false
        setxy random-xcor random-ycor
    ]
    setup-infected
    reset-ticks
end
```

The `setup` procedure initializes the simulation by clearing the environment, creating the agents, setting their initial properties (shape, size, color, infection status, and position), and calling the `setup-infected` procedure to set the initial infected agents. It also resets the timer to track the simulation time.

```ruby
to go
    move
    infect
    tick
end
```

The `go` procedure is called at each time step and calls the `move` and `infect` procedures to update the position of the agents and infect susceptible agents. It also increments the simulation time by one tick.

:::{admonition} 💡 `go` and `setup` buttons on the Interface
:class: tip
:icon: false
Make sure you have the `go` and `setup` buttons on the Interface tab. The `setup` button should call the `setup` procedure, and the `go` button should call the `go` procedure. You can also set the `go` button to be a forever button, so it keeps running until you stop it.
:::

:::{admonition} 👩🏾‍💻 Code for the spontaneous contagion model
:class: important
:icon: false
You can find the code for this part [here](codes/tutorial01.nlogox).
:::
