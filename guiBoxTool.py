'''
GUI BOX TOOL

This tool collects all of the xml files located in the Programming-Assignment-Data folder, finds the
associated png file and highlights all of the leaf nodes denoted in the xml file visually on the png
file with a yellow box.

It uses the os library to interact with the file system, the lxml library to read the xml files and
the PIL library to edit them and add the boxes.

HARRIS MARSLAND
'''

# Imports
import os
from PIL import Image, ImageDraw
from lxml import etree

# Create new folder to house updated images and get file folder path
cwd = os.getcwd()
if not os.path.exists(cwd + '\\Edited-Images'):
    os.mkdir(cwd + '\\Edited-Images')
padFolder = cwd + '\\Programming-Assignment-Data'
if not os.path.exists(padFolder):
    raise FileExistsError ('The Programming-Assignment-Data folder could not be found. Please place it in the current directory.')

# Iterate through files in folder, grabbing all xml files
for file in os.listdir(padFolder):
    splitFilename = os.path.splitext(file)
    
    # Find corresponding png file
    if splitFilename[1] == '.xml':
        if os.path.exists(padFolder + '\\' + splitFilename[0] + '.png'):
            xmlFile = file
            pngFile = Image.open(padFolder + '\\' + splitFilename[0] + '.png')
        else:
            raise FileNotFoundError (file + ' does not have a matching png file.')
    else:
        continue
    
    # Parse the xml tree for the leaf nodes
    tree = etree.parse(padFolder + '\\' + file)
    root = tree.getroot()
    leafNodes = root.xpath('//*[not(*)]') # //* searches all nodes, not(*) grabs nodes without children

    # Open the image to be edited
    draw = ImageDraw.Draw(pngFile)

    # For each leaf, create a yellow box connecting the corner coordinates in the image file
    for leaf in leafNodes:
        bounds = leaf.get('bounds')
        
        # Map the bounds values into usable coordinates
        coords = bounds[:-1].replace('[', '').replace(']',',').split(',')
        x1, y1, x2, y2 = map(int, coords)

        # Use coords to draw a box in the image
        draw.rectangle([x1, y1, x2, y2], outline='yellow', width=3)

    # Save image to new folder
    newImageName = 'Updated_' + splitFilename[0] + '.png'
    pngFile.save(cwd + '\\Edited-Images\\' + newImageName)

print('Completed')