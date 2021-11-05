#################################################################################################################################
# AutoTile
# Version 1.0
# Author: ASARG
# Description: Implements the tile automata model as designed by Chalk et al.
#################################################################################################################################
# AutoTile Manual

Table of Contents
Sections
1 - Application
2 - Models Overview
3 - File I/O
4 - Feature Map
5 - Change Log


#############################
Section 1 - Application

## 1.1 Requirements
  Required:
    -Python 3+
    -PyQt5 (install using pip)
	-networkx (install using pip)
  Optional:


## 1.2 Usage
  Running:
    >python3 AutoTile.py

## 1.3 Menu Overview
Main Menu
 + File
    - New 
    - Load
    - Save As
    - Save History
    - Load History
 + Tools
    - Edit
    - Rotate
    - Combine
    - X-Reflect
    - Y-Reflect
    - Slow Mode
    - Time Elapsed
 + Available Moves
    - List of available moves
    - Next
    - Previous
 + Examples
    - Shape
	- Model
	- Input
    
## 1.4 Menu Functions
1.4.1 File Menu
1.4.1.1 New
  This menu option opens the editor so you may begin making a new system.
  
1.4.1.2 Load
  This menu option will prompt the user for a file and then attempt to open it. 

  The application will only load XML files.
  
1.4.1.3 Save As . . .
  This menu option will prompt the user for a file name and location to log the information to. It will overwrite a file if it already exists.

1.4.1.4 Save History
  This menu option saves where the assembly is currently at to a JSON file.
  This menu option saves the current assembly to a JSON file.
  Since some assemblies can get quite large, you have the ability to save multiple versions of the assembly at different points in time.
  When prompted, enter the name of the JSON file, then enter how many steps inbetween each version of the assembly you want. If you would like only
  the current assembly and no multiple versions, enter 0.

1.4.1.5 Load History
  This menu option takes a JSON file and loads a system, assembly, and all steps to a certain point.

1.4.2 Tools Menu
1.4.2.1 Edit
  When clicked, opens the editor with the current system loaded.
  
1.4.2.2 Rotate
  Rotates the current system 90 degrees clockwise. Ex. a assembly where the final shape is " |" will now be "__"
  
1.4.2.3 Combine
  Prompts the user to select a valid file and attempts to combine the system in the file with the current loaded system.

1.4.2.4 X-Reflect
  "Reflects" the system across the x-axis.

1.4.2.5 Y-Reflect
  "Reflects" the system across the y-axis.

1.4.2.4 Slow Mode
  This is a radio button that, when selected, adds a brief delay in between steps while the play option is selected.

1.4.2.5 Time Elapsed
  This is just text that shows the user how many "time steps" have occured at the current step.

1.4.3 Available Moves
  This section allows a particular attachment or transition to be selected rather than a move being picked at random.
1.4.3.1 Next
  When there are more moves than can be shown, you can page through the moves with 'Next'.
1.4.3.2 Prev
  Similar to 'Next', you can page through the moves with 'Prev'.

1.4.4 Example
1.4.4.1 Shape
	Here you will see a combo box with three options "strings," "Thin Rectangle," and "Square." Select your desired shape to begin loading an example system

1.4.4.2 Model
	Here you will see a combo box with three options "Deterministic," "Non-Deterministic," and "One-Sided." Select your desired model of computation for the example to follow.

1.4.4.3 Input
	Above the input box is text saying valid input types for the chosen options. Type your input in here then press the button below to load an example system. 

## 1.5 Simulator Screen
Windows users, we are aware of a bug that does not let you interact with the simulator when you press play on some systems and are looking into it.

1.5.1 Simulator Area
  This is where the simulation occurs. When a system with a seed is loaded, the chosen seed tile will appear here. 
  Tiles are displayed here with their respective label and color. It should be noted that only up to 4 characters of the label will be displayed, so it is recommended to color code should you have labels with similar beginnings.


1.5.2 Toolbar
  The toolbar has five buttons which include:
  -First: returns you to the first step of the assembly
  -Previous: shows you the previous step of the assembly
  -Play/Pause: pressing play simulates what a system would do step by step. Pause will appear when a user presses play so you may stop the simulation on a certain step. If you would like the play sequence to be slower, be sure to press the "slow mode" radio button.
  -Next: shows you the next step of the assembly
  -Last: takes you to the last step of the function
  It should be noted that these only work if a system is loaded

1.5.3 Simulator Controls
  Once a system is loaded: 
  -WASD will move the assembly. Holding shift with any of the WASD keys will move the assembly faster, this functions speed relates to the size of the assembly 
  -The mouse scroll wheel can zoom in and out, additionally + and - keys also zoom in and out
  -C will "recenter" the seed of the assembly.

  These hotkeys correspond to the tool bar at the top of the screen and are mapped to follow the layout respectively.
  -H -First 
  -J -Previous
  -K -Play/Pause
  -L -Next 
  -; -Last

## 1.6 Editor Menu
1.6.1 General Settings
1.6.1.1 System Temperature
Set the system temperature here.
1.6.1.2 Freezing Check
click this button to check if your current system is a freezing system. Output is on the GUI and a .svg file called freezingcheck shows a graph with the states.

1.6.2 Add State
1.6.2.1 Color
Input a colors hexadecimal value here to set the states color
1.6.2.2 Label
Input a string here to be your states label. Note: on screen only the first 4 letters will appear from the states label
1.6.2.3 Seed
Check this box if this state can be a seed
1.6.2.4 Initial
Check this box if this state is an inital state or a state that can be used freely.

1.6.3 Add Affinity Rule
1.6.3.1 State1
The left state if its h or the top state if its v
1.6.3.2 State2
The right state if its h or the bottom state if its v
1.6.3.3 Direction
Input the direction of the affinity rule here, use h for a horizontal rule and v for a vertical rule
1.6.3.4 Glue Strength
Set the glue strength of this bond

1.6.4 Add Transition Rule
1.6.4.1 State 1
The left state if its h or the top state if its v
1.6.4.2 State 2
The right state if its h or the bottom state if its v
1.6.4.3 State 1 Final
What the left/top state transitions to if State1 and State2 are next to each other
1.6.4.4 State 2 Final
What the right/bottom state transitions to if State1 and State2 are next to each other
1.6.4.5 Direction
Input the direction of the transition rule here, use h for a horizontal rule and v for a vertical rule
#############################
Section 2 - Models Overview

2.1 Tile Automata 
A Tile Automata system is a marriage between cellular automata and 2-handed self-assembly.
Systems consist of a set of monomer tile states, along with local affinities between states
denoting the strength of attraction between adjacent monomer tiles in those states. A set  
of local state-change rules are included for pairs of adjacent states. Assemblies (collections
of edge-connected tiles) in the model are created from an initial set of starting assemblies
by combining previously built assemblies given sufficient binding strength from the affinity
function. Further, existing assemblies may change states of internal monomer tiles according
to any applicable state change rules.

2.1.1 Freezing
Consider a tile automata system and a directed graph G constructed as follows:
Each state type is a vertex
for any two state types, a and b, an edge from a to b exists if and only if there exists a
transition rule between them i.e. a transitions to b
The system is said to be freezing if G is acyclic and non-freezing otherwise. Intuitively, a tile
automata system is freezing if any one tile in the system can never return to a state which
it held previously. This implies that any given tile in the system can only undergo a finite
number of state transitions.

#############################
Section 3 - File I/O

3.1 XML format
  The editor can create an XML file for you, but should you desire to check or build your own XML file an example simple system XML file is shown below. 

EXAMPLE:
    <?xml version='1.0' encoding='utf-8'?>
<System Temp="1">
	<AllStates>
		<State Label="A" Color="f03a47" />
		<State Label="B" Color="3f88c5" />
		<State Label="C" Color="323031" />
	</AllStates>
	<InitialStates>
		<State Label="A" Color="f03a47" />
		<State Label="B" Color="3f88c5" />
	</InitialStates>
	<SeedStates>
		<State Label="A" Color="f03a47" />
	</SeedStates>
	<VerticalTransitions>
		<Rule Label1="A'" Label2="B" Label1Final="A'" Label2Final="A" />
	</VerticalTransitions>
	<HorizontalTransitions>
		<Rule Label1="B" Label2="B" Label1Final="B" Label2Final="C" />
	</HorizontalTransitions>
	<VerticalAffinities>
		<Rule Label1="A" Label2="B" Strength="1" />
	</VerticalAffinities>
	<HorizontalAffinities>
		<Rule Label1="B" Label2="B" Strength="1" />
	</HorizontalAffinities>
</System>
    
#############################
Section 4 - Feature Map



#############################
Section 5 - Changelog

## 5.1 Version 1.0
    - Initial version distributed to others
    
