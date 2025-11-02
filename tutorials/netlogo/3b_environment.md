# Patch Properties and Visualization (15 min)

Let's learn how to use patch colors to visualize data and create meaningful environments.

## Using Patch Color to Show Data

**Basic color assignment:**

```ruby
ask patches [
  set pcolor green    ; All patches green
]

ask patch 0 0 [       ; Center patch only
  set pcolor red
]

ask patches with [pxcor > 0] [  ; Right half of world
  set pcolor blue
]
```

**Color based on data:**

```ruby
ask patches [
  ; Color based on distance from center
  let distance-from-center sqrt (pxcor ^ 2 + pycor ^ 2)
  set pcolor scale-color red distance-from-center 0 10
]
```

The `scale-color` command creates gradients:

- `scale-color red value 0 10` makes a red gradient from light (value=0) to dark (value=10)
- High values = dark red, low values = light red

## Creating Environmental Gradients

**Temperature gradient (hot in south, cold in north):**

```ruby
ask patches [
  set temperature pycor + 10        ; Temperature based on y-coordinate
  set pcolor scale-color red temperature 0 20  ; Red = hot, pink = cold
]
```

**Resource distribution (rich center, poor edges):**

```ruby
ask patches [
  let distance-from-center sqrt (pxcor ^ 2 + pycor ^ 2)
  set resources 100 - distance-from-center * 5
  if resources < 0 [ set resources 0 ]
  set pcolor scale-color green resources 0 100  ; Green = rich, black = poor
]
```

**Random patchy resources:**

```ruby
ask patches [
  set resources random 100
  set pcolor scale-color brown resources 0 100  ; Brown gradient
]
```

## Activity 1: Heat Map

**Goal:** Create a temperature gradient using patch colors

```ruby
to setup-heat-map
  ask patches [
    ; Create temperature based on distance from center
    let distance-from-center sqrt (pxcor ^ 2 + pycor ^ 2)
    set temperature 100 - distance-from-center * 3
    if temperature < 0 [ set temperature 0 ]
    
    ; Color patches based on temperature
    set pcolor scale-color red temperature 0 100
  ]
end
```

**Try different patterns:**

- East-west gradient: `set temperature pxcor + 15`
- Diagonal gradient: `set temperature (pxcor + pycor) + 20`  
- Multiple hot spots: Create several high-temperature centers

```{admonition} What Do You Observe?
:class: question

- How does the color pattern reflect the underlying data?
- What would this temperature map represent in real life?
- How might agents behave differently in hot vs. cold areas?
```
