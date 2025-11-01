#!/usr/bin/env python3
"""
NetLogo Commands Wordcloud Generator

This script creates a colorful wordcloud of NetLogo programming language commands
and primitives with random sizes to visualize the vocabulary of NetLogo.

Requirements:
    pip install wordcloud matplotlib numpy pillow

Usage:
    python netlogo_wordcloud.py
"""

import random
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np

def generate_netlogo_commands():
    """
    Generate a comprehensive list of NetLogo commands and primitives
    extracted from the NetLogo Dictionary.
    """
    
    # Core NetLogo commands and primitives organized by category
    turtle_commands = [
        'forward', 'fd', 'back', 'bk', 'left', 'lt', 'right', 'rt',
        'jump', 'move-to', 'setxy', 'face', 'facexy', 'towards', 'towardsxy',
        'home', 'hide-turtle', 'ht', 'show-turtle', 'st', 'pen-down', 'pd',
        'pen-up', 'pu', 'pen-erase', 'pe', 'stamp', 'stamp-erase', 'die',
        'hatch', 'sprout', 'distance', 'distancexy', 'dx', 'dy', 'can-move',
        'heading', 'xcor', 'ycor', 'color', 'shape', 'size', 'hidden',
        'pen-mode', 'pen-size', 'label', 'label-color', 'breed', 'who'
    ]
    
    patch_commands = [
        'pcolor', 'plabel', 'plabel-color', 'pxcor', 'pycor', 'diffuse',
        'diffuse4', 'patch', 'patch-at', 'patch-ahead', 'patch-here',
        'patch-left-and-ahead', 'patch-right-and-ahead', 'neighbors',
        'neighbors4', 'uphill', 'uphill4', 'downhill', 'downhill4',
        'patches', 'random-pxcor', 'random-pycor', 'import-pcolors'
    ]
    
    agentset_commands = [
        'ask', 'ask-concurrent', 'with', 'of', 'one-of', 'any', 'all',
        'count', 'sort', 'sort-by', 'sort-on', 'max-one-of', 'min-one-of',
        'max-n-of', 'min-n-of', 'with-max', 'with-min', 'other', 'self',
        'myself', 'turtle-set', 'patch-set', 'link-set', 'turtles',
        'patches', 'links', 'nobody', 'no-turtles', 'no-patches', 'no-links'
    ]
    
    creation_commands = [
        'create-turtles', 'crt', 'create-ordered-turtles', 'cro',
        'create-link-with', 'create-link-to', 'create-link-from',
        'create-links-with', 'create-links-to', 'create-links-from'
    ]
    
    control_flow = [
        'if', 'ifelse', 'ifelse-value', 'while', 'repeat', 'loop',
        'foreach', 'let', 'set', 'stop', 'report', 'run', 'runresult',
        'carefully', 'to', 'to-report', 'end', 'startup'
    ]
    
    world_commands = [
        'clear-all', 'ca', 'clear-turtles', 'ct', 'clear-patches', 'cp',
        'clear-drawing', 'cd', 'clear-output', 'reset-ticks', 'tick',
        'tick-advance', 'ticks', 'display', 'no-display', 'resize-world',
        'world-width', 'world-height', 'min-pxcor', 'max-pxcor',
        'min-pycor', 'max-pycor', 'patch-size'
    ]
    
    math_operators = [
        '+', '-', '*', '/', '^', 'mod', 'remainder', 'abs', 'sqrt', 'sin',
        'cos', 'tan', 'asin', 'acos', 'atan', 'ln', 'log', 'exp', 'floor',
        'ceiling', 'round', 'precision', 'random', 'random-float',
        'random-normal', 'random-exponential', 'random-gamma',
        'random-poisson', 'random-seed', 'new-seed'
    ]
    
    list_operations = [
        'list', 'item', 'length', 'empty', 'first', 'last', 'but-first',
        'but-last', 'reverse', 'sort', 'shuffle', 'fput', 'lput',
        'sentence', 'member', 'remove', 'remove-item', 'remove-duplicates',
        'replace-item', 'insert-item', 'sublist', 'position', 'filter',
        'map', 'reduce', 'n-values', 'range'
    ]
    
    string_operations = [
        'word', 'substring', 'read-from-string', 'is-string', 'is-number',
        'is-boolean', 'is-list', 'is-agent', 'is-agentset', 'is-patch',
        'is-turtle', 'is-link'
    ]
    
    io_commands = [
        'print', 'show', 'type', 'write', 'output-print', 'output-show',
        'output-type', 'output-write', 'user-input', 'user-message',
        'user-yes-or-no', 'user-one-of', 'beep', 'timer', 'reset-timer'
    ]
    
    file_operations = [
        'file-open', 'file-close', 'file-close-all', 'file-read',
        'file-read-line', 'file-read-characters', 'file-write', 'file-print',
        'file-type', 'file-show', 'file-exists', 'file-delete', 'file-flush',
        'export-world', 'import-world', 'export-view', 'export-interface'
    ]
    
    plotting_commands = [
        'plot', 'plotxy', 'plot-name', 'set-current-plot', 'clear-plot',
        'clear-all-plots', 'plot-pen-down', 'plot-pen-up', 'set-plot-x-range',
        'set-plot-y-range', 'histogram', 'autoplot', 'setup-plots',
        'update-plots'
    ]
    
    color_commands = [
        'scale-color', 'rgb', 'hsb', 'extract-rgb', 'extract-hsb',
        'approximate-rgb', 'approximate-hsb', 'shade-of', 'wrap-color',
        'red', 'green', 'blue', 'yellow', 'orange', 'violet', 'pink',
        'cyan', 'magenta', 'lime', 'turquoise', 'sky', 'brown', 'gray',
        'black', 'white'
    ]
    
    link_commands = [
        'create-link-with', 'create-link-to', 'create-link-from',
        'link-neighbor', 'link-neighbors', 'in-link-neighbors',
        'out-link-neighbors', 'my-links', 'my-in-links', 'my-out-links',
        'link-with', 'in-link-from', 'out-link-to', 'other-end',
        'both-ends', 'tie', 'untie', 'link-length', 'link-heading',
        'directed-link-breed', 'undirected-link-breed'
    ]
    
    observer_commands = [
        'watch', 'follow', 'ride', 'reset-perspective', 'subject',
        'inspect', 'stop-inspecting'
    ]
    
    boolean_logic = [
        'and', 'or', 'not', 'xor', 'true', 'false'
    ]
    
    # Combine all commands
    all_commands = (
        turtle_commands + patch_commands + agentset_commands + 
        creation_commands + control_flow + world_commands + 
        math_operators + list_operations + string_operations + 
        io_commands + file_operations + plotting_commands + 
        color_commands + link_commands + observer_commands + 
        boolean_logic
    )
    
    # Remove duplicates and return
    return list(set(all_commands))

def create_frequency_dict(commands):
    """
    Create a frequency dictionary with random weights for commands.
    This ensures varied sizes in the wordcloud.
    """
    frequency_dict = {}
    
    # Define different weight categories for visual variety
    core_commands = ['ask', 'set', 'create-turtles', 'forward', 'if', 'repeat', 'to', 'end']
    important_commands = ['with', 'of', 'one-of', 'random', 'count', 'show', 'color']
    
    for command in commands:
        if command in core_commands:
            # Core commands get higher frequency (bigger size)
            frequency_dict[command] = random.randint(80, 100)
        elif command in important_commands:
            # Important commands get medium frequency
            frequency_dict[command] = random.randint(50, 80)
        else:
            # Other commands get random frequency
            frequency_dict[command] = random.randint(10, 60)
    
    return frequency_dict

def generate_wordcloud():
    """
    Generate and save the NetLogo commands wordcloud.
    """
    # Set random seed for reproducible results (optional)
    random.seed(42)
    
    # Get NetLogo commands
    commands = generate_netlogo_commands()
    print(f"Generated {len(commands)} unique NetLogo commands")
    
    # Create frequency dictionary with random weights
    frequencies = create_frequency_dict(commands)
    
    # Define colorful color palette
    colorful_colors = [
        '#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7',
        '#DDA0DD', '#98D8C8', '#F7DC6F', '#BB8FCE', '#85C1E9',
        '#F8C471', '#82E0AA', '#F1948A', '#85C1E9', '#D2B4DE',
        '#AED6F1', '#A3E4D7', '#D5DBDB', '#FADBD8', '#E8DAEF'
    ]
    
    def color_function(*args, **kwargs):
        """Custom color function to return random colors from our palette"""
        return random.choice(colorful_colors)
    
    # Create WordCloud object with custom settings
    wordcloud = WordCloud(
        width=1600,
        height=800,
        background_color='white',
        max_words=200,
        relative_scaling=0.5,
        colormap='Set3',  # Fallback colormap
        color_func=color_function,  # Use our custom color function
        prefer_horizontal=0.7,
        min_font_size=12,
        max_font_size=80,
        font_path=None,  # Use default font
        collocations=False  # Avoid word combinations
    ).generate_from_frequencies(frequencies)
    
    # Create the plot
    plt.figure(figsize=(20, 10))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('NetLogo Programming Language Commands & Primitives', 
              fontsize=24, fontweight='bold', pad=20)
    
    # Save the wordcloud
    output_path = '/Users/ea47/Documents/Teaching/25fa-social-modeling/resources/wordcloud/netlogo_commands_wordcloud.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    
    print(f"Wordcloud saved to: {output_path}")
    
    # Also save just the wordcloud image without matplotlib frame
    wordcloud.to_file(output_path.replace('.png', '_clean.png'))
    print(f"Clean wordcloud saved to: {output_path.replace('.png', '_clean.png')}")
    
    # Show the plot
    plt.show()
    
    return wordcloud

def print_command_stats(commands):
    """Print some statistics about the commands."""
    print(f"\nNetLogo Commands Statistics:")
    print(f"Total unique commands: {len(commands)}")
    print(f"Sample commands: {', '.join(sorted(commands)[:20])}...")

if __name__ == "__main__":
    print("NetLogo Commands Wordcloud Generator")
    print("=" * 40)
    
    try:
        # Generate the wordcloud
        wordcloud = generate_wordcloud()
        
        # Print some stats
        commands = generate_netlogo_commands()
        print_command_stats(commands)
        
        print("\nWordcloud generation completed successfully!")
        print("The wordcloud shows NetLogo programming commands in colorful, randomly-sized text.")
        
    except Exception as e:
        print(f"Error generating wordcloud: {e}")
        print("\nMake sure you have the required packages installed:")
        print("pip install wordcloud matplotlib numpy pillow")
