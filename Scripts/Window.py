import maya.cmds as cmds

def WindowMaker ():
    mWin = "LocWindow"

    if cmds.window(mWin, exists=True):
        cmds.deleteUI(mWin)

    mWin = cmds.window(mWin, title='Create Locator')
    mCol = cmds.columnLayout(parent=mWin, adjustableColumn=True)
    #dropCtrl = cmds.optionMenuGrp(parent=mCol, label='Type')
    #cmds.menuItem(parent=dropCtrl, label='Bounding Box')
    #cmds.menuItem(parent=dropCtrl, label='Pivot Point')
    #cmds.button(parent=mCol, label='Create Locator')

    cmds.text(parent=mCol, label='Locator Type:')
    cmds.button(parent=mCol, label='Bounding Box')
    cmds.button(parent=mCol, label='Pivot Point')

    cmds.showWindow(mWin)

WindowMaker ()