import sys
import maya.cmds as cmds
sys.path.append(r'C:\Users\jonat\Documents\maya\2018\scripts\MyScripts')
from Rename import Renamer
from CreateControls import MasterControlCreator
from BoundingBox import LocatorTool
from JointBuilder import JointCreator
from RandomPlacement import RandomPlacement

MCC = MasterControlCreator()
LocTool = LocatorTool()
JointCreator = JointCreator()
RandomPlacement = RandomPlacement()


class Layout:
    def __init__(self):
        pass

    def create(self):
        self.BuildLayout()

    def BuildLayout(self):

        self.window = cmds.window(widthHeight=(400,300), title="Master Control Program", resizeToFitChildren=1)

        # RENAMER SECTION
        cmds.frameLayout(label="Renamer", collapsable=0)
        cmds.columnLayout(rowSpacing=5)
        self.renameField=cmds.textField(placeholderText="Prefix_#_Suffix",width=200)
        cmds.text(label="Num-Padding:")
        self.numPadding=cmds.intField()
        cmds.button(label="Execute",command=lambda x: self.CheckRenameField())
        cmds.setParent('..')
        cmds.setParent('..')

        # ---------------------------------------------------------------------------------------------- #

        # PLACEMENT RANDOMIZER SECTION
        cmds.frameLayout(label="Random Placer",collapsable=0,height=100)
        cmds.columnLayout(rowSpacing=5)
        cmds.rowLayout(numberOfColumns=4,columnWidth4=(100,2,100,100))
        cmds.text(label="# of Duplicates")
        cmds.separator(style="single")
        cmds.text(label="Min Range")
        cmds.text(label="Max Range")
        cmds.setParent('..')

        cmds.rowLayout(numberOfColumns=4,columnWidth4=(100,2,100,100))
        self.duplicatesField=cmds.intField()
        cmds.separator(style="single")
        self.minRangeField=cmds.floatField()
        self.maxRangeField=cmds.floatField()
        cmds.setParent('..')

        cmds.rowLayout(numberOfColumns=1)
        cmds.button(label="Execute",command=lambda x: self.CheckRandomizerFields())
        cmds.setParent('..')
        cmds.setParent('..')
        cmds.setParent('..')

        # ---------------------------------------------------------------------------------------------- #

        # CONTROL UTILITY SECTION
        cmds.frameLayout(label="Control Parameters", collapsable=1)
        cmds.rowLayout(numberOfColumns=3)

        # Control Shape Selector
        cmds.columnLayout()
        cmds.text(label="DO NOT USE YET")
        self.radio1 = cmds.radioCollection()
        cmds.radioButton(label="Circle")
        cmds.radioButton(label="Star")
        cmds.radioButton(label="Box")
        cmds.setParent('..')

        cmds.separator(style="single", width=50, horizontal=0)

        # Control Color Selector
        cmds.columnLayout()
        # Parameters for making custom color palettes.
        maxOverrideColors = 32
        formOffset = 2
        columns = maxOverrideColors / 2
        rows = 2
        cellWidth = 17
        cellHeight = 17

        cmds.text(label="Select Color")

        # Create a color palette with all of the available override colors.
        MCC.colorPalette = cmds.palettePort("myPallete",
                                             dimensions=(columns, rows),
                                             transparent=0,
                                             width=(columns * cellWidth),
                                             height=(rows * cellHeight),
                                             topDown=1,
                                             colorEditable=0)

        for i in range(1, maxOverrideColors):
            colorComponent = cmds.colorIndex(i, query=1)
            cmds.palettePort(MCC.colorPalette, edit=1,
                             rgbValue=(i, colorComponent[0], colorComponent[1], colorComponent[2]))

        cmds.palettePort(MCC.colorPalette, edit=1, rgbValue=(0, 0.6, 0.6, 0.6))
        cmds.setParent('..')  # columnLayout
        cmds.setParent('..')  # rowLayout
        cmds.setParent('..')  # frameLayout

        ##########################################################################

        cmds.frameLayout(label="Execute", collapsable=0)
        cmds.rowLayout(numberOfColumns=3)
        cmds.button(label="Create Circle Controls", command=lambda x: MCC.CreateCircleControls())
        cmds.button(label="Create Square Controls", command=lambda x: MCC.CreateSquareControls())
        cmds.button(label="Color Controls", command=lambda x: MCC.Colorizer())
        cmds.setParent('..')
        cmds.setParent('..')

        # ---------------------------------------------------------------------------------------------- #

        # CENTER LOCATOR SECTION
        cmds.frameLayout(label="Center Locator")
        cmds.columnLayout(adjustableColumn=True)
        cmds.button(label='Create Locator (Bounding Box)',
                    c=lambda x: LocTool.CreateLoc(1))
        cmds.button(label='Create Locator (Pivot)',
                    c=lambda x: LocTool.CreateLoc(2))
        cmds.setParent('..')
        cmds.setParent('..')

        # ---------------------------------------------------------------------------------------------- #

        # FK JOINT CREATOR SECTION
        cmds.frameLayout(label="Joint Creator")
        cmds.columnLayout(adjustableColumn=True)
        cmds.button(label='Create FK Joint Chain',
                    c=lambda x: JointCreator.ChainBuilder())
        cmds.setParent('..')
        cmds.setParent('..')

        cmds.showWindow(self.window)

    def CheckRenameField(self):
        renameInput = cmds.textField(self.renameField, query=1, text=1)
        numPadding = cmds.intField(self.numPadding, query=1, value=1)
        Renamer(renameInput, numPadding)

    def CheckRandomizerFields(self):
        duplicates = cmds.intField(self.duplicatesField, query=1, value=1)
        minRange = cmds.floatField(self.minRangeField, query=1, value=1)
        maxRange = cmds.floatField(self.maxRangeField, query=1, value=1)
        RandomPlacement.Distributor(duplicates, minRange, maxRange)


test = Layout()
test.create()