import maya.cmds as cmds
import random

# This function takes a selection, and duplicates it a given number of times
# and randomly places it in a cube of a given size.

def RandomPlacement(duplicates, rangeMin, rangeMax):
    selection = cmds.ls(sl=True)
    cmds.group(selection, name='selection')

    # Copy selection group $duplicates number of times and randomly place
    # within $rangeMin and $rangeMax on each axis.
    for num in range(0,duplicates):
        duplications = cmds.duplicate('selection')
        x = random.uniform(rangeMin, rangeMax)
        y = random.uniform(rangeMin, rangeMax)
        z = random.uniform(rangeMin, rangeMax)

        cmds.select(duplications[0], r=True)
        cmds.move(x, y, z)

    geometry = cmds.ls(geometry=True)
    transforms = cmds.listRelatives(geometry, p=True, path=True)
    cmds.select(transforms, r=True)
    cmds.parent(world=True)
    cmds.select(selection, r=True)
    cmds.delete(selection)


RandomPlacement(5, -10, 10)