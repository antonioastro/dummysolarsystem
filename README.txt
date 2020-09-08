Thanks for downloading Antonio's N-body simulator. For the greatest enjoyment please follow these instructions, and any further instructions given in the py files carefully.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
the code is simple to run. should you want a solar system simulation you should follow these steps:

open both Simulation.py and Solar System.py (Particle.py contains only the particle class and Bodies.py contains all the solar system bodies start conditions, but are required for the simulation to work- ignore analyis.py for now)
change the saving and loading directories in the files keeping the last elements the same as this is the title of the file being saved/loaded - there are more details on this in the docstrings at the start of the files.
decide on the timestep, simulation runtime, method, datatosave by following the relevant instructions in the docstrings
run the file - it will do the rest for you.
once it has saved, (it will say so in the terminal) switch to Solar System.py
decide which graph you want to plot by following the instructions in the docstrings
run the code - it will automatically both save a plot to a directory and open up the plot in a new window

NOTE THAT IF YOU DO NOT CHANGE THE DIRECTORY FROM THE DEFAULTS, THE CODE WILL THROW AN ERROR AT YOU THAT LOOKS LIKE:
----FileNotFoundError: [Errno 2] No such file or directory: '[DIRECTORY HERE]'
if this is the case then you have not changed the directory as instructed.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

if you want to analyse the data:
run all the above as instructed.
now open analysis.py
change the directories as instructed in the docstrings at the top of the code. 
decide on what graph type to plot by choosing kinetic energy change, total energy, virial theorem, momentum, angular momentum, by following the relevant instructions in the docstring
run the code - it will do the rest for you
once complete it will both save a copy of the graph under the relevant name and display the graph on the screen.

NOTE THAT IF YOU DO NOT CHANGE THE DIRECTORY FROM THE DEFAULTS, THE CODE WILL THROW AN ERROR AT YOU THAT LOOKS LIKE:
----FileNotFoundError: [Errno 2] No such file or directory: '[DIRECTORY HERE]'
if this is the case then you have not changed the directory as instructed.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

if you want to simulate another solar system or change the starting conditions of the current one:
move Bodies.py out of the directory. 
create a copy of the SAME NAME and put it back in the original directory. this is so you still have the original available
open Bodies.py (the new one you just copied in)
you can now create a new system by editing the names, masses, starting conditions, ensuring that nothing else is changed. you can have as many bodies as you wish - only your computer's processing power is the limit
they should be formatted as such (don't add units in curly brackets (m) they are just for your reference):

Body name=Particle([position x, position y, position z](m),[velocity x, velocity y, velocity z](m/s),[0,0,0],'Body Name', Mass (kg))
Body name2=Particle([position x2, position y2, position z2](m),[velocity x2, velocity y2, velocity z2](m/s),[0,0,0],'Body Name2', Mass2 (kg))

ensure that the EXACT BRACKETS AND CODE REMAIN. ONLY CHANGE position x, position y, etc. the docstrings in bodies.py give more instructions.
once done carry out instructions from the first section of this text file.