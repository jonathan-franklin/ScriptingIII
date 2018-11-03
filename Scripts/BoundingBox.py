import maya.cmds as cmds

def CreateLoc(option):
    sels = cmds.ls( sl = True )

    if option is 1:
        dups = cmds.duplicate( sels, rr = True )
        dups = cmds.polyUnite( dups, ch = True, centerPivot = True )
        bbox = cmds.xform( dups, boundingBox = True, q = True )
        pivot = [(bbox[0] + bbox[3]) / 2, (bbox[1] + bbox[4]) / 2, (bbox[2] + bbox[5]) / 2]

        cmds.delete(dups, ch = True)

        loc = cmds.spaceLocator()[0]
        cmds.xform(loc, translation = pivot, worldSpace = True)
    elif option is 2:
        for sel in sels:
            pivot = cmds.xform(sel, q = True, rp = True, ws = True)
            loc = cmds.spaceLocator()
            cmds.xform(loc, translation = pivot, worldSpace = True)

CreateLoc(1)