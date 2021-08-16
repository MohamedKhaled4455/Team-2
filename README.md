# Team-2
 

	Project details:
	The used programming language
	The purpose of the document
	The description of the project




(The used programming language: Python)

	Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. 
	Its high-level built-in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together.
	Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. 
	Python supports modules and packages, which encourages program modularity and code reuse. 

	The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms and can be freely distributed.



 







(The purpose of the document)

	The purpose of this document is to describe the code of the project with the help of code snippets to make it easily read and understood.


 



(The description of the project)

	The description of the game:
	The mouse tries to:
•	Escape: this occurs if the mouse reaches the bridge (touches the green tile)
•	Not to starve to death: this occurs if it makes less than 20 moves without escaping.
•	Not to be eaten, this occurs if the mouse doesn’t meet the cat (touches the cat tile)
•	Not to be drown, this occurs if the mouse doesn’t hit the water (touches a blue tile)
 
	The code description:
 

	First, you should import some important libraries to start the program:
o	PyGame
o	Random
o	Time 
 

	Defining some colors with the help of (RGB) range of color:
o	Black
o	White
o	Green
o	Grey
o	Blue
 

	To draw the grids of the boardgame, we set two variables (WIDTH, HEIGHT) and set each of them to (66).
	We made the variable (margin = 1) between each cell.

 

	To make the mouse move in all directions, we set the two variables (x, y) to (0).
	Z = [x, y]
 
	To randomize the movement of the rat, we need to make 3 lists (Rx, Ry, R_mouse) and adjust the position of the rat perfectly.
 
	Here, we display the screen mode to a certain size which is [500, 500] and setting a caption (‘Window’).
 
	We upload 2 photos for the cat and the rat to make the game more realistic with transform scale (60, 60).
      

 
	To adjust the movement by arrows, we made every step change by (66) and (0) in different directions in the two coordinates (x, y). 
 
	To make 2D empty list (grid), we made 2 loops as shown in the figure consists of 7 empty elements in each loop to make a (49 blocks) in the boardgame. 

 

	This is initialization of the (PyGame) library to make games on python.
 
	The code lines that describe the window editing and clock setting.
 
	The function (font_setting) that adjusts the font color.
 
	The function (message) that adjusts the font type and size and how its place on the boardgame.
 
	To apply the 4 scenarios that we mentioned them earlier, we need to write 4 functions that express them which are:
o	Starve
o	Escape
o	Water
o	Dead 
 
	These two functions (RAT_MOVEMENT, keys) describe the rat movement.
 
	The event coding lines.
 
 

	The scenarios that may happen. 
 
 
	To draw the grid, we made loops as shown in the figures.

 

	To quit the game, you need to write the line code (pygame. quit ()).














Samsung Innovation Campus
PYTHON
FINAL PROJECT
MOUSE ESCAPING GAME

 
