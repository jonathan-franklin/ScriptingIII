import maya.cmds as cmds

class LocatorTool():
    def __init__(self):
        self.mWin = 'LocWindow'

    def create(self):
        self.delete()

        self.mWin = cmds.window(self.mWin, title='Create Locator')
        self.mCol = cmds.columnLayout(parent=self.mWin, adjustableColumn=True)
        self.dropCtrl = cmds.optionMenuGrp(parent=self.mCol, label='Type')
        cmds.menuItem(parent=self.dropCtrl, label='Bounding Box')
        cmds.menuItem(parent=self.dropCtrl, label='Pivot Point')
        cmds.button(parent=self.mCol, label='Create Locator',
                    c=lambda x: self.CreateLoc(cmds.optionMenu(self.dropCtrl, q=True, select=True)))


        cmds.showWindow(self.mWin)

    def delete(self):
        if cmds.window(self.mWin, exists=True):
            cmds.deleteUI(self.mWin)

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

#CreateLoc(1)