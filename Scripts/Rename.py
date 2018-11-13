import maya.cmds as cmds

def Renamer(rename, numPad):
    sel = cmds.ls(selection = True)
    holding = rename.split('#')
    i = 1

    for obj in sel:
        if numPad == 1:
            newSel = holding[0] + str(i) + holding[1]
            cmds.rename(obj, newSel)
            i += 1
        elif numPad == 2 and i < 10:
            newSel = holding[0] + "0" + str(i) + holding[1]
            cmds.rename(obj, newSel)
            i += 1
        elif numPad == 3 and i < 10:
            newSel = holding[0] + "00" + str(i) + holding[1]
            cmds.rename(obj, newSel)
            i += 1
        elif numPad == 3 and i < 100:
            newSel = holding[0] + "0" + str(i) + holding[1]
            cmds.rename(obj, newSel)
            i += 1
        elif numPad == 4 and i < 10:
            newSel = holding[0] + "000" + str(i) + holding[1]
            cmds.rename(obj, newSel)
            i += 1
        elif numPad == 4 and i < 100:
            newSel = holding[0] + "00" + str(i) + holding[1]
            cmds.rename(obj, newSel)
            i += 1
        elif numPad == 4 and i < 1000:
            newSel = holding[0] + "0" + str(i) + holding[1]
            cmds.rename(obj, newSel)
            i += 1
        else:
            newSel = holding[0] + "0" + str(i) + holding[1]
            cmds.rename(obj, newSel)
            i += 1

Renamer('Left_#_Jnt', 2)