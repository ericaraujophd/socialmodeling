# Using NetLogo's Built-in Analysis Tools (20 min)

NetLogo provides powerful tools for data collection without programming complex analysis routines.

## Monitors: Real-Time Data Tracking

**Monitors show live values** as your model runs:

```ruby
; In interface, create monitor that shows:
count turtles with [carrying-food?]
; Label it: "Ants with Food"

mean [pheromone] of patches with [pheromone > 0]
; Label it: "Average Pheromone"

ticks
; Label it: "Time Steps"
```

**Strategic monitor placement:**

- **Outcome variables:** Your main research question measures
- **Sanity checks:** Total population, conservation laws
- **Process indicators:** Rates of change, intermediate states

## Plots: Visualizing Change Over Time

**Plots track multiple variables** and show patterns:

**Basic setup in Interface tab:**

1. Click "Plot" button to create new plot
2. Name it (e.g., "Population Dynamics")
3. Set X and Y axis labels and ranges
4. Add "pens" for different variables

**Code to update plots:**

```ruby
to update-plots
  ; This automatically runs every tick
  
  ; Plot 1: Population by type
  set-current-plot "Population Dynamics"
  set-current-plot-pen "Cooperators"
  plot count turtles with [strategy = "cooperate"]
  
  set-current-plot-pen "Defectors"  
  plot count turtles with [strategy = "defect"]
  
  ; Plot 2: Average satisfaction
  set-current-plot "Satisfaction Levels"
  set-current-plot-pen "satisfaction"
  plot mean [satisfaction] of turtles
end
```

## Histograms: Understanding Distributions

**See how values are distributed** across your population:

```ruby
; In interface, create histogram
; Set pen update to:
histogram [age] of turtles

; Or show distribution of some other property:
histogram [count link-neighbors] of turtles  ; Network degree
histogram [money] of turtles                  ; Wealth distribution
histogram [satisfaction] of turtles           ; Satisfaction levels
```

## Activity: Build Analysis Dashboard

**Create a complete monitoring system:**

1. **Add 3-4 monitors** tracking key variables in your model
2. **Create 2 plots** showing how important things change over time  
3. **Add 1 histogram** showing distribution of agent properties
4. **Run your model and observe** what patterns emerge

```{admonition} Dashboard Design Tips
:class: tip

**Choose variables that answer your research question:**

- If studying segregation: track segregation index over time
- If studying cooperation: plot cooperation rates and payoffs
- If studying diffusion: monitor adoption rates and network effects

**Use meaningful scales:**

- Percentages (0-100) for rates and proportions
- Natural units (dollars, years, people) for quantities  
- Standardized scales (-1 to 1) for comparing different variables

**Update regularly but not obsessively:**

- Every tick for fast-changing variables
- Every 10-50 ticks for slow-changing variables
- At the end only for final outcome measures
```

## BehaviorSpace: Systematic Experiments

**BehaviorSpace runs multiple experiments automatically** with different parameter combinations.

**Setting up experiments:**

1. Tools menu → BehaviorSpace
2. Click "New" to create experiment
3. Vary parameters systematically:

```ruby
["tolerance" [0.1 0.2 0.3 0.4 0.5]]
["population-size" [100 200 500]]
```

4. Set number of repetitions (e.g., 10 runs per combination)
5. Choose which variables to measure:

```ruby
count turtles with [color = red]
segregation-index
mean [satisfaction] of turtles
```

6. Run experiment (can take a while!)

**BehaviorSpace generates spreadsheet** with all results for further analysis.
