# Core Concepts (25 min)

Let's learn the basic building blocks that all programming uses.

## Variables: Things That Can Change

### Variables store information that can change over time.

Examples in real life:

- Your age (changes every year)
- Your bank account balance (goes up and down)
- Your location (changes as you move)

Examples in NetLogo:

- `age` - how old is this turtle?
- `wealth` - how much money does this turtle have?
- `xcor` - what is the turtle's x-coordinate?
- `color` - what color is this turtle?

### Think of Variables as Labels

Imagine each turtle wearing name tags:

```{admonition} Conversation
:class: tip

- "Hi, my name is **Turtle #42**"
- "My age is **25**"  
- "My wealth is **$1,500**"
- "My location is **(10, 15)**"

Variables are just labels that can be updated!
```

## Commands: Actions Agents Can Take

**Commands tell agents what to do.**

### Basic movement commands

- `forward 1` - move forward 1 step
- `right 90` - turn right 90 degrees  
- `left 45` - turn left 45 degrees

### Property change commands

- `set color red` - change color to red
- `set size 2` - make turtle bigger
- `die` - remove this turtle from the world

### Social commands:

- `create-link-with turtle 5` - form connection with turtle #5
- `ask neighbors` - give instructions to nearby turtles

## Reporters: Questions Agents Can Answer  

### Reporters ask questions and get answers.

About myself:

- `who` - what is my ID number?
- `xcor` - what is my x-coordinate?
- `count my-links` - how many connections do I have?

About others:

- `count turtles` - how many turtles exist?
- `count neighbors` - how many turtles are near me?
- `mean [wealth] of turtles` - what's the average wealth?

About the environment:

- `pcolor` - what color is the patch I'm on?
- `patches in-radius 3` - which patches are within 3 units?

## Procedures: Grouping Instructions Together

**Procedures are like recipes - they group related instructions.**

```{code-block} ruby
:caption: Simple Procedure Example

to move-randomly
  right random 360    ; turn a random amount
  forward 1           ; move forward 1 step  
end
```

This procedure called `move-randomly` does two things:

1. Turn a random direction (0-360 degrees)
2. Move forward 1 step

Now you can just say `move-randomly` instead of repeating those two lines!

## Why use procedures?

- Organize related instructions
- Avoid repeating the same code
- Make code easier to read and understand
- Break complex tasks into smaller pieces
