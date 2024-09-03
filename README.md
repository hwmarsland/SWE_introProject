# SWE_introProject

### HOW TO RUN
- This program is run from the command line using the command `python3 guiBoxTool.py` while navigated to the location of the python file in the command line.
  - NOTE: Please place the `Programming-Assignment-Data` folder in the same location as the `guiBoxTool.py` file. If you forget, the program will prompt you with an error.
- The result of the program will be a newly created folder named `Edited-Images` located in the current directory that contains all of the associated updated png files.

### REQUIRED LIBRARIES
- lxml (Used to parse xml files)
  - Can be installed with `pip install lxml`
- Pillow (Used to edit png files)
  - Can be installed with `pip install pillow`
 
### SOLUTION DESCRIPTION
- My solution is fairly straightforward. It operates using a single nested loop to iterate through the files in the `Programming-Assignment-Data` folder to grab the xml files one at a time. When it finds an xml, it locates the associated png for later editing. Then, it parses and searches the xml using the xpath function of lxml to find all the leaf nodes. With a complete list of leaf nodes, the program then maps the bounds attribute of each node to usable coordinates. These coordinates are then used to draw a rectangle for each node on the png file. When all of the leaf nodes have been drawn in, the program saves the file to the `Edited-Images` folder. When everything has been completed, the program prints `Completed` to the command line.
