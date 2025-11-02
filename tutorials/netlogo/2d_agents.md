# Making Turtles Unique (15 min)

Real people aren't identical - let's give our turtles individual differences.

## Giving Turtles Different Properties

**Random assignment:**

```ruby
create-turtles 100 [
  set age 18 + random 62        ; Age between 18-79
  set wealth random 10000       ; Wealth between $0-$9,999
  set social-activity random 11 ; Social activity 0-10
]
```

**Systematic assignment:**

```ruby
create-turtles 100 [
  set age 20 + who / 2          ; Age increases with ID
  if who < 50 [ set color red ] ; First 50 are red
  if who >= 50 [ set color blue ] ; Last 50 are blue
]
```

**Using probability distributions:**

```ruby
create-turtles 100 [
  ; Most people are middle-aged, few are very young or old
  set age 20 + random-normal 25 10
  
  ; 70% are cooperative, 30% are competitive  
  if random 100 < 70 [ set strategy "cooperative" ]
  if random 100 >= 70 [ set strategy "competitive" ]
]
```

## Random vs. Systematic Assignment

**Random assignment** creates natural variation:

- `random 10` gives numbers 0-9 randomly
- `one-of [red green blue]` picks one color randomly
- `random-normal 50 15` gives normally distributed numbers around 50

**Systematic assignment** creates patterns:

- Assign properties based on `who` number
- Create spatial gradients
- Assign roles or types deliberately

## Using `who` Numbers to Identify Specific Turtles

Every turtle has a unique `who` number (0, 1, 2, 3, ...):

```ruby
ask turtle 0 [ set color red ]        ; Color turtle #0 red
ask turtle 5 [ forward 10 ]           ; Move turtle #5 forward
ask turtles with [who < 10] [ ... ]   ; First 10 turtles
ask turtles with [who mod 2 = 0] [ ... ] ; Even-numbered turtles
```

## Activity 2: Random Walk

**Goal:** Make turtles explore randomly

```ruby
to setup
  clear-all
  create-turtles 20 [
    setxy random-xcor random-ycor
    set color one-of [red green blue yellow orange]
    set size 1 + random 2  ; Size between 1-3
  ]
end

to go
  ask turtles [
    right random 360       ; Turn random direction
    forward 1              ; Move forward
    if xcor > max-pxcor or xcor < min-pxcor [ 
      set xcor random-xcor ; Wrap around edges
    ]
    if ycor > max-pycor or ycor < min-pycor [
      set ycor random-ycor ; Wrap around edges  
    ]
  ]
end
```

**Run this:** Click "setup" once, then click "go" repeatedly to watch random exploration.

```{admonition} What went wrong?
:class: danger

What were the problems to follow up these instructions? What was missing to make it work?
```
