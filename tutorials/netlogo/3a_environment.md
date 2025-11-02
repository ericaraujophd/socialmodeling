# The World Patches Live In (10 min)

## Patches = Grid Squares That Make Up the World

Think of the NetLogo world as a **grid of squares**, like:

- **Chessboard squares** where pieces can move
- **City blocks** where people live and work  
- **Pixels on a screen** that create an image
- **Cells in a spreadsheet** that hold information

Each square is called a **patch** and has:

- **Coordinates:** `pxcor` (x-position) and `pycor` (y-position)
- **Color:** `pcolor` (what color is this patch?)
- **Custom properties:** anything you define (temperature, resources, ownership, etc.)

## Each Patch Has Properties (Color, Variables)

**Built-in properties:**

- `pxcor` and `pycor` - location coordinates
- `pcolor` - color of this patch
- `plabel` - text label on this patch

**Custom properties you might add:**

- `temperature` - how hot/cold is this location?
- `resources` - how much food/oil/wealth is here?
- `population-density` - how crowded is this area?
- `pollution-level` - how contaminated is this spot?

## Environment Shapes Agent Behavior

The environment isn't just decoration - it **actively influences** what agents do:

**Examples:**

- **Foraging:** Animals move toward resource-rich patches
- **Urban planning:** People prefer low-pollution, high-amenity areas
- **Disease spread:** Infection rates vary by population density
- **Economic development:** Businesses locate near transportation hubs

```{admonition} Key Insight
:class: tip

**Environment and agents interact dynamically.** Agents respond to their environment, but they can also change it through their actions, creating feedback loops.
```
