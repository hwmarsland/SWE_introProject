PROCESS:
- Use library "lxml" to parse the xml file and find leaf nodes, grabbing coordinate dimensions for drawing boxes
  - Finding leaf nodes are the most important part as those are the sections that need to be highlighted in yellow boxes.
- Use python imaging library (PIL) to edit the image and add in the yellow boxes.
- Program should take arguments of the set of xml files and the png files and use the xml file to draw yellow boxes in the png file, generating a new png file in the process.

NOTES:
- Simple tool, just make a set of instructions.
  - DRY principles still apply. Make sure processes are part of functions and file isn't just a jumble of instructions.
