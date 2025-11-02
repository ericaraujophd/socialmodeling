# 2. Update Households

We turn now to the aesthetic aspects of the model. Using arrowheads makes it hard to see the state of the agents (if they are happy or not). We can think of many ways to represent the state of the agents. Let's remember that the color represent the households opinions/ideas/ideologies (red or blue). We can use the shape of the agents to represent their happiness. For example, we can use circles for happy agents and squares for unhappy agents. This way, we can easily see the state of the agents in the model.

For this model, we will use an x for the unhappy agents and a square for the happy agents. That is for the sake of visualization. You can use any shape you want. The important thing is to be consistent and to use shapes that are easy to distinguish.

As the agents will be moving around the environment and changing their state, we will need to update their shape accordingly. We can do this by filling the procedure called `update-households` create before. This procedure will be called any time we need to change the shape of the agents.

```ruby
to update-households
  ask households [
    ifelse happy?   [ set shape "square" ][ set shape "x" ] ; set shape to x if unhappy and square if happy
  ]
end
```

As you will soon notice, we have a problem in here. How do we know if an agent is happy or not? We need to define the rules for happiness. In this model, an agent is happy if the percentage of similar neighbors is greater than or equal to the `similar-wanted` threshold. We can calculate the percentage of similar neighbors by dividing the number of similar neighbors by the total number of neighbors. We also need to make sure that we are not dividing by zero. If an agent has no neighbors, we will consider it as happy.

Let's fix our `update-households` procedure to include the calculation of happiness:

```ruby
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
```

So we now have the setup procedure that creates the households and updates their shape based on their happiness.
