import maya.cmds as cmds

class MasterControlCreator:
    def __init__(self):
        pass

    def create(self):
        self.ControlUI()

    def ControlUI(self):
        self.window = cmds.window(widthHeight=(500, 200), title="Master Control Utility")

        cmds.frameLayout(label="Control Parameters", collapsable=1)
        cmds.rowLayout(numberOfColumns=3)

        # Control Shape Selector
        cmds.columnLayout()
        cmds.text(label="DO NOT USE YET")
        self.radio1=cmds.radioCollection()
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
        self.colorPalette = cmds.palettePort("myPallete",
                                      dimensions=(columns,rows),
                                      transparent=0,
                                      width=(columns*cellWidth),
                                      height=(rows*cellHeight),
                                      topDown=1,
                                      colorEditable=0)

        for i in range(1,maxOverrideColors):
            colorComponent = cmds.colorIndex(i, query=1)
            cmds.palettePort(self.colorPalette, edit=1, rgbValue=(i, colorComponent[0], colorComponent[1], colorComponent[2]))

        cmds.palettePort(self.colorPalette, edit=1, rgbValue=(0,0.6,0.6,0.6))
        cmds.setParent('..') #columnLayout
        cmds.setParent('..') #rowLayout
        cmds.setParent('..') #frameLayout

        #######################################################################################

        cmds.frameLayout(label="Execute", collapsable=0)
        cmds.rowLayout(numberOfColumns=3)
        cmds.button(label="Create Circle Controls", command=lambda x: self.CreateCircleControls())
        cmds.button(label="Create Square Controls", command=lambda x: self.CreateSquareControls())
        cmds.button(label="Color Controls", command=lambda x: self.Colorizer())
        cmds.setParent('..')
        cmds.setParent('..')

        cmds.showWindow(self.window)

    def CreateCircleControls(self):
        sels = cmds.ls(sl=1)
        colorRGB = cmds.palettePort(self.colorPalette, query=1, setCurCell=1)

        if len(sels) != 0:
            for sel in sels:
                ctrl = cmds.circle(name=(sel + "_Ctrl"))

                grp = cmds.group(name=(sel + "_Ctrl_Grp"))

                self.ColorControl(ctrl, colorRGB)
                cmds.matchTransform(grp, sel)
        else:
            ctrl = cmds.circle()

            grp = cmds.group()

            self.ColorControl(ctrl, colorRGB)

    def CreateSquareControls(self):
        sels = cmds.ls(sl=1)
        colorRGB = cmds.palettePort(self.colorPalette, query=1, setCurCell=1)

        if len(sels) != 0:
            for sel in sels:
                ctrl = cmds.nurbsSquare(name=(sel + "_Ctrl"))

                grp = cmds.group(name=(sel + "_Ctrl_Grp"))

                self.ColorControl(ctrl, colorRGB)
                cmds.matchTransform(grp, sel)
        else:
            ctrl = cmds.nurbsSquare()

            grp = cmds.group()

            self.ColorControl(ctrl, colorRGB)

    def Colorizer(self):
        ctrls = cmds.ls(sl=1)

        colorRGB = cmds.palettePort(self.colorPalette, query=1, setCurCell=1)

        for ctrl in ctrls:
            self.ColorControl(ctrl, colorRGB)

    def ColorControl(self, _ctrl, _color):
        ctrl = _ctrl
        color = _color
        shapes = cmds.listRelatives(ctrl, shapes=1)

        for shape in shapes:
            if cmds.nodeType(shape) == "nurbsCurve":
                # Allow overrides on shape
                cmds.setAttr(shape + ".overrideEnabled", 1)

                # Override color on shape
                cmds.setAttr(shape + ".overrideColor", color)
            else:
                cmds.warning("Selected object is not a curve.")
