# Reading Code Before Writing (15 min)

Let's practice reading and understanding NetLogo code together.

## Activity 1: Code Reading

**Look at this simple procedure. What do you think it does?**

```ruby
to setup
  clear-all
  create-turtles 100 [
    setxy random-xcor random-ycor
    set color one-of [red green blue yellow]
  ]
  reset-ticks
end
```

```{admonition} "What Do You Think This Does?"
:class: seealso

Before looking at the answer, discuss with a partner:
1. What happens when you run this procedure?
2. How many turtles get created?
3. Where do they appear?
4. What colors might they be?
```

```{dropdown} Answer (only click after discussing)
This procedure:

1. Clears everything from the world
2. Creates 100 turtles
3. Places each turtle at a random location  
4. Gives each turtle a random color (red, green, blue, or yellow)
5. Resets the tick counter to 0
```

## Activity 2: Spot the Difference

**Compare these two procedures. What's different?**

**Procedure A:**

```ruby
to move-turtles
  ask turtles [
    forward 1
  ]
end
```

**Procedure B:**  

```ruby
to move-turtles
  ask turtles [
    right random 360
    forward 1  
  ]
end
```

**What's the difference in behavior? TTYN**

```{dropdown} Answer (only click after discussing)

- Procedure A: All turtles move straight forward
- Procedure B: All turtles turn randomly first, then move forward
```

## Activity 3: Human Computer

**Let's act out NetLogo commands!**

**Setup:** 

- 5 students are "turtles" 
- Classroom is the "world"
- One student is the "computer" giving commands

**Commands to try:**

1. `create-turtles 5` - 5 students enter the "world"
2. `ask turtles [ forward 2 ]` - everyone takes 2 steps forward
3. `ask turtles [ right 90 ]` - everyone turns right  
4. `ask turtle 0 [ set color red ]` - student #0 puts on red hat
5. `ask turtles [ if color = red [ forward 3 ] ]` - only red turtle moves

```{admonition} Connect Code to Visual Outcomes
:class: tip

**Key insight:** Every line of code creates a visible change in the world. When reading code, always ask:
- "What would I see happening?"
- "How would the world look different?"
- "Which agents would be affected?"
```
