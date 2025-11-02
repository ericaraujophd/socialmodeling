# Turtle-Patch Interactions (15 min)

Now let's make agents interact with their environment in meaningful ways.

## Turtles Asking Their Current Patch Questions

Turtles can ask the patch they're standing on for information:

```ruby
ask turtles [
  let current-temp [temperature] of patch-here
  if current-temp > 50 [
    set color red      ; Turn red if on hot patch
  ]
]
```

**Common patch queries:**

- `[pcolor] of patch-here` - what color is this patch?
- `[resources] of patch-here` - how many resources here?
- `[temperature] of patch-here` - what's the temperature?

## Moving Based on Patch Properties

**Move toward better patches:**

```ruby
ask turtles [
  ; Look at nearby patches
  let nearby-patches patches in-radius 2
  let best-patch max-one-of nearby-patches [resources]
  
  if best-patch != nobody [
    face best-patch     ; Turn toward resource-rich patch
    forward 1
  ]
]
```

**Avoid dangerous areas:**

```ruby
ask turtles [
  let current-pollution [pollution] of patch-here
  if current-pollution > 50 [
    ; Move away from polluted areas
    let clean-patches patches in-radius 3 with [pollution < 10]
    if any? clean-patches [
      move-to one-of clean-patches
    ]
  ]
]
```

## Turtles Modifying Their Environment

Agents don't just respond to environment - they change it:

**Consume resources:**

```ruby
ask turtles [
  let current-resources [resources] of patch-here
  if current-resources > 0 [
    ask patch-here [
      set resources resources - 1     ; Consume 1 unit
      set pcolor scale-color green resources 0 100  ; Update color
    ]
  ]
]
```

**Leave traces:**
```ruby
ask turtles [
  ask patch-here [
    set pheromone pheromone + 1       ; Leave pheromone trail
    set pcolor scale-color yellow pheromone 0 10
  ]
]
```

## Activity 2: Foraging

**Goal:** Turtles move toward resource-rich patches

```ruby
to setup-foraging
  ; Create resource patches
  ask patches [
    set resources random 50
    set pcolor scale-color green resources 0 50
  ]
  
  ; Create foraging turtles
  create-turtles 20 [
    setxy random-xcor random-ycor
    set color yellow
    set energy 100
  ]
end

to go-foraging
  ask turtles [
    ; Look for nearby resource patches
    let nearby-patches patches in-radius 2
    let best-patch max-one-of nearby-patches [resources]
    
    if best-patch != nobody [
      face best-patch
      forward 1
    ]
    
    ; Consume resources on current patch
    let current-resources [resources] of patch-here
    if current-resources > 0 [
      set energy energy + current-resources
      ask patch-here [
        set resources 0
        set pcolor black  ; Mark as depleted
      ]
    ]
    
    ; Use energy to survive
    set energy energy - 1
    if energy <= 0 [ die ]
  ]
end
```

**Run this model:**

1. Click "setup-foraging" to create resources and turtles
2. Click "go-foraging" repeatedly and watch turtles search for food
3. Notice how they deplete resources and change the environment

## Activity 3: Erosion

**Goal:** Turtles modify patch values as they pass through

```ruby
to setup-erosion
  ; Create terrain with different soil stability
  ask patches [
    set soil-stability 50 + random 50  ; Stability 50-100
    set pcolor scale-color brown soil-stability 50 100
  ]
  
  create-turtles 30 [
    setxy random-xcor random-ycor  
    set color white
  ]
end

to go-erosion
  ask turtles [
    ; Random movement
    right random 60 - 30
    forward 1
    
    ; Cause erosion on current patch
    ask patch-here [
      set soil-stability soil-stability - 0.5
      if soil-stability < 0 [ set soil-stability 0 ]
      set pcolor scale-color brown soil-stability 0 100
    ]
  ]
end
```

**What happens:** Watch how turtle movement creates "erosion paths" in the landscape!

```{admonition} Reflection Questions
:class: question

- How do the paths develop over time?
- What happens in areas with heavy turtle traffic?
- How does this relate to real-world erosion patterns?
- What if different turtles caused different amounts of erosion?
```

---

## Learning Objectives Achieved

By completing this tutorial, you can now:

✓ **Understand the role of environment in agent-based models**  
✓ **Create meaningful environmental visualizations**  
✓ **Implement agent-environment interactions**

---

## What's Next?

Now you have all the building blocks - agents, environment, and interactions. Time to put it all together into your first complete model from scratch!

```{admonition} Coming Up: Building Your First Complete Model
:class: note

- Planning before programming
- Step-by-step model building  
- Testing and debugging
- Documentation and sharing

**Mini-project preview:** Build a simple "ants following pheromone trails" model that combines everything you've learned!
```

**Think about:** What complete model would you like to build? What social phenomenon interests you? What agents and environment would you need?
