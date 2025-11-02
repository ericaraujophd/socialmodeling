# Step-by-Step Model Building (30 min)

Let's build a complete model together using systematic steps.

## Our Project: Ants Following Pheromone Trails

**Research question:** "How do individual ants create efficient collective foraging paths?"

**Agents:** Ants that search for food and leave pheromone trails
**Environment:** Food sources and evaporating pheromone trails
**Behavior:** Ants follow pheromone gradients and reinforce successful paths

## Start Simple: Create Agents

**Step 1:** Basic setup

```ruby
turtles-own [
  carrying-food?    ; Is this ant carrying food back to nest?
]

to setup
  clear-all
  
  ; Create nest at center
  ask patch 0 0 [
    set pcolor brown
    set plabel "NEST"
  ]
  
  ; Create food source
  ask patches with [pxcor > 10 and pycor > 10] [
    if random 100 < 30 [  ; 30% chance of food
      set pcolor green
    ]
  ]
  
  ; Create ants
  create-turtles 50 [
    setxy 0 0           ; Start at nest
    set color red
    set carrying-food? false
  ]
  
  reset-ticks
end
```

**Test it:** Run setup and verify you see nest, food, and ants.

## Add One Behavior at a Time

**Step 2:** Basic movement

```ruby
to go
  ask turtles [
    ; Simple random movement for now
    right random 60 - 30    ; Turn randomly
    forward 1
  ]
  tick
end
```

**Test it:** Run go repeatedly. Do ants move around randomly?

**Step 3:** Food collection

```ruby
to go
  ask turtles [
    ; Check if on food patch
    if pcolor = green and not carrying-food? [
      set carrying-food? true
      set color yellow        ; Carrying food
      ask patch-here [ set pcolor black ]  ; Remove food
    ]
    
    ; Check if back at nest with food
    if pcolor = brown and carrying-food? [
      set carrying-food? false
      set color red          ; Not carrying food
    ]
    
    ; Movement
    right random 60 - 30
    forward 1
  ]
  tick
end
```

**Test it:** Do ants pick up food and return to nest?

## Test Frequently, Fix Problems Early

After each step, ask:

- Does the behavior work as expected?
- Are there any error messages?
- Do you see the visual changes you expect?

**Common issues:**

- Ants getting stuck at world edges
- Food disappearing too quickly
- Ants not finding their way back to nest

## Build Complexity Gradually

**Step 4:** Add pheromone trails

```ruby
patches-own [
  pheromone          ; Amount of pheromone on this patch
]

to setup
  ; ... previous setup code ...
  
  ; Initialize pheromones
  ask patches [
    set pheromone 0
  ]
end

to go
  ask turtles [
    ; Leave pheromone if carrying food
    if carrying-food? [
      ask patch-here [
        set pheromone pheromone + 10
        set pcolor scale-color red pheromone 0 100
      ]
    ]
    
    ; ... previous behavior code ...
  ]
  
  ; Evaporate pheromones
  ask patches [
    set pheromone pheromone * 0.95  ; 5% evaporation
    if pheromone < 0.1 [ set pheromone 0 ]
    if pcolor != brown and pcolor != green [
      set pcolor scale-color red pheromone 0 100
    ]
  ]
  
  tick
end
```

**Test it:** Do you see red trails where ants have been?

**Step 5:** Follow pheromone gradients

```ruby
to go
  ask turtles [
    ; If not carrying food, follow pheromone gradients
    if not carrying-food? [
      let best-patch max-one-of patches in-radius 2 [pheromone]
      if best-patch != nobody and [pheromone] of best-patch > 0 [
        face best-patch
        forward 1
      ] else [
        right random 60 - 30  ; Random movement if no pheromone
        forward 1
      ]
    ] else [
      ; If carrying food, head toward nest
      face patch 0 0
      forward 1
    ]
    
    ; ... food collection code ...
    ; ... pheromone laying code ...
  ]
  
  ; ... pheromone evaporation code ...
  tick
end
```

## Activity: Mini-Project

**Complete the ant model by adding:**

1. **Better nest-finding:** Ants carrying food should move more directly toward nest
2. **Trail reinforcement:** Successful ants should lay stronger pheromone trails
3. **Energy system:** Ants use energy and must return to nest to refuel

## Model Building Tips

**Start simple, add complexity gradually:**

- Get basic movement working first
- Add one new behavior at a time
- Test after every change
- Fix problems immediately

**Use meaningful variable names:**

- `carrying-food?` not `cf?`
- `pheromone-strength` not `ps`
- `energy-level` not `el`

**Add comments explaining what code does:**

```ruby
; Ants lay pheromone when carrying food
if carrying-food? [
  ask patch-here [
    set pheromone pheromone + 10
  ]
]
```
