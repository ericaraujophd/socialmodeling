# Common Problems and Solutions (20 min)

Every modeler faces challenges. Here are the most common issues and how to resolve them systematically.

## Runtime Errors and How to Fix Them

**"I can't reproduce by" error:**

```
Problem: ask patches in-radius 5 [ set color red ]
Error: "I can't reproduce by -1.2345"
```

**Cause:** A patch coordinate calculation produced a non-integer value
**Solution:** Use `round` or explicitly create patch coordinates

```ruby
; Problem version:
let target-x xcor + distance * cos heading
ask patch target-x ycor [ set color red ]

; Fixed version:
let target-x round (xcor + distance * cos heading)
ask patch target-x ycor [ set color red ]

; Better version:
let target-patch patch-at (distance * dx) (distance * dy)
if target-patch != nobody [ ask target-patch [ set color red ] ]
```

**"Cannot access a property of a turtle/patch/link who doesn't exist" error:**

```ruby
; Problem: turtle died but code still tries to use it
ask turtle 5 [ set color red ]  ; What if turtle 5 is dead?

; Solution: Check if turtle exists first  
if turtle 5 != nobody [ ask turtle 5 [ set color red ] ]

; Better: Use breeds and with clauses
ask wolves with [energy > 0] [ hunt ]
```

**"Runtime error: Division by zero":**

```ruby
; Problem:
let average total-wealth / count turtles  ; What if no turtles?

; Solution:
let average 0
if count turtles > 0 [ 
  set average total-wealth / count turtles 
]

; Better: Handle edge cases explicitly
to-report calculate-average [value-list]
  if length value-list = 0 [ report 0 ]
  report sum value-list / length value-list
end
```

## Performance Issues

**Model runs very slowly:**

**Common causes and fixes:**

1. **Too many agents asking too many others:**

```ruby
; Slow version:
ask turtles [
  ask other turtles [  ; N × N operations!
    if distance myself < 5 [ ... ]
  ]
]

; Faster version:
ask turtles [
  ask other turtles in-radius 5 [  ; Only nearby turtles
    ; ... interaction code ...
  ]
]
```

2. **Unnecessary calculations every tick:**

```ruby
; Slow: recalculates every tick
ask turtles [
  let my-neighborhood turtles in-radius 5
  let similar count my-neighborhood with [color = [color] of myself]
  let satisfaction similar / count my-neighborhood
]

; Faster: only recalculate when needed
ask turtles [
  if moved-recently? [  ; Only when something changed
    calculate-satisfaction
    set moved-recently? false
  ]
]
```

3. **Complex patch operations:**

```ruby
; Slow: asking every patch every tick
ask patches [
  set pheromone pheromone * 0.95  ; Even patches with no pheromone
]

; Faster: only patches that need updating
ask patches with [pheromone > 0] [
  set pheromone pheromone * 0.95
  if pheromone < 0.01 [ set pheromone 0 ]
]
```

## Logic Errors

**Model produces unrealistic results:**

### Debugging Strategy

**Step 1: Verify basic mechanics**

- Are agents created correctly?
- Do they move as expected?
- Are calculations producing reasonable numbers?

**Step 2: Test edge cases**

- What happens with 1 agent? 1000 agents?
- What if all agents have the same properties?
- What if parameters are set to extreme values?

**Step 3: Add debugging output**

```ruby
; Add temporary monitors or print statements
if who = 0 and ticks mod 50 = 0 [  ; Only turtle 0, every 50 ticks
  print (word "Energy: " energy " Satisfaction: " satisfaction)
]
```

**Step 4: Simplify temporarily**

- Comment out complex behaviors
- Test one mechanism at a time
- Use simple movement patterns first

## Activity: Debug Challenge

**Here's a broken segregation model. Find and fix the errors:**

```ruby
to setup
  clear-all
  ask patches [
    if random 100 < density [
      sprout 1 [
        set color one-of [red blue]
        set tolerance random-float 1
      ]
    ]
  ]
end

to go
  ask turtles [
    let similar count turtles-here with [color = [color] of myself]
    let total count turtles-here
    if similar / total < tolerance [
      move-to one-of patches with [count turtles-here = 0]
    ]
  ]
  tick
end
```

**Hint:** There are at least 3 logical errors in this code.