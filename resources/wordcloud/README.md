# NetLogo Commands Wordcloud Generator

This directory contains a Python script that generates a colorful wordcloud visualization of NetLogo programming language commands and primitives.

## Features

- **Comprehensive Command Collection**: Includes 200+ NetLogo commands from all categories (turtle, patch, agentset, control flow, math, etc.)
- **Random Sizing**: Commands have randomly assigned sizes for visual variety
- **Colorful Palette**: Uses a vibrant color scheme with 20+ distinct colors
- **High Quality Output**: Generates both matplotlib and clean PNG versions
- **Educational Purpose**: Perfect for teaching NetLogo vocabulary and command overview

## Installation

1. Make sure you have Python 3.6+ installed
2. Install the required packages:

```bash
pip install -r requirements.txt
```

Or install packages individually:
```bash
pip install wordcloud matplotlib numpy pillow
```

## Usage

Run the script from this directory:

```bash
python netlogo_wordcloud.py
```

## Output Files

The script generates two image files:

1. `netlogo_commands_wordcloud.png` - Full visualization with title and matplotlib frame
2. `netlogo_commands_wordcloud_clean.png` - Clean wordcloud image only

Both files are saved at 300 DPI for high-quality printing and presentation use.

## Customization

You can modify the script to:

- Change colors by editing the `colorful_colors` list
- Adjust word frequencies in the `create_frequency_dict()` function
- Modify wordcloud dimensions by changing `width` and `height` parameters
- Add or remove NetLogo commands from the various command lists

## NetLogo Command Categories Included

- **Turtle Commands**: movement, appearance, actions
- **Patch Commands**: patch properties and operations  
- **Agentset Operations**: asking, filtering, sorting
- **Creation Commands**: creating turtles and links
- **Control Flow**: conditionals, loops, procedures
- **World Commands**: setup, clearing, global properties
- **Mathematical Operations**: arithmetic, trigonometry, random numbers
- **List Operations**: list manipulation and processing
- **String Operations**: text processing
- **I/O Commands**: input/output and user interaction
- **File Operations**: reading and writing files
- **Plotting Commands**: graph and chart creation
- **Color Commands**: color manipulation
- **Link Commands**: network and connection operations
- **Observer Commands**: perspective and viewing
- **Boolean Logic**: logical operations

## Educational Use

This wordcloud is designed for:

- **Course Materials**: Visual overview of NetLogo vocabulary
- **Reference Posters**: Classroom displays showing available commands
- **Student Learning**: Helping students discover new NetLogo primitives
- **Documentation**: Supplementing NetLogo programming guides

## Technical Details

- **Font Sizing**: 12-80px range for readability
- **Layout**: 70% horizontal preference for better text readability  
- **Resolution**: 1600x800 pixels, 300 DPI output
- **Colors**: Custom color function with predefined palette
- **Frequency Weighting**: Core commands larger, specialized commands smaller

## Credits

Based on the official NetLogo Dictionary documentation from Northwestern University's Center for Connected Learning and Computer-Based Modeling.
