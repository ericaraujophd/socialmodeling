# Creating and Controlling Turtles (20 min)

Let's learn how to bring agents to life and give them instructions.

## Bringing Agents to Life: `create-turtles`

The most basic command for creating a population:

```ruby
create-turtles 100
```

This creates 100 turtles, each with:

- Random color
- Random location  
- Random heading (direction)
- Size 1, ID numbers 0-99

**Create specific numbers:**

```ruby
create-turtles 50    ; Create 50 turtles
create-turtles 200   ; Create 200 turtles
```

## Giving Instructions to All or Some Agents: `ask turtles`

The `ask` command lets you give instructions to turtles:

**Ask all turtles to do something:**

```ruby
ask turtles [
  forward 1           ; Every turtle moves forward
  set color red       ; Every turtle turns red
]
```

**Ask specific turtles to do something:**

```ruby
ask turtle 0 [         ; Ask turtle #0 specifically
  set color blue
  set size 3
]

ask turtles with [color = red] [    ; Ask only red turtles
  forward 2
]

ask n-of 10 turtles [  ; Ask 10 randomly chosen turtles
  set color green
]
```

## Basic Turtle Commands

**Movement commands:**

- `forward 1` - move forward 1 step
- `right 90` - turn right 90 degrees
- `left 45` - turn left 45 degrees  
- `back 1` - move backward 1 step

**Property commands:**

- `set color red` - change color to red
- `set size 2` - make turtle twice as big
- `set heading 0` - face north (heading 0)

**Try it yourself:**

```ruby
create-turtles 20 [
  setxy random-xcor random-ycor    ; Random position
  set color one-of [red blue green yellow]  ; Random color
]

ask turtles [
  right random 360    ; Turn random direction
  forward 3           ; Move forward
]
```

```{admonition} What went wrong?
:class: danger

What were the problems to follow up these instructions? What was missing to make it work?
```

## Activity 1: Build a Flock

**Goal:** Create turtles that move in the same direction

**Step 1:** Create the turtles

```ruby
create-turtles 50 [
  setxy random-xcor random-ycor
  set color yellow
  set heading 90  ; All face east
]
```

**Step 2:** Make them move together

```ruby
ask turtles [
  forward 1
]
```

**Step 3:** Run this repeatedly and watch your flock move across the screen!

```{admonition} What Do You Observe?
:class: question

- Do the turtles stay together as they move?
- What happens when they reach the edge of the world?
- How could you make them turn together?
```

```{admonition} What went wrong?
:class: danger

What were the problems to follow up these instructions? What was missing to make it work?
```
