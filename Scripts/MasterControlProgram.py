import MyScripts/Rename.mel
import MyScripts/RandomPlacement.mel
import MyScripts/CreateControls.mel

import maya.cmds as cmds

class Layout():
    def __init__(self):
        pass
    def create(self):
        self.BuildLayout()
    def BuildLayout(self):
        self.window = cmds.window(widthHeight=(500,300), title="Master Control Program", resizeToFitChildren=1)
        cmds.frameLayout(label="Renamer", collapsable=0)
        cmds.columnLayout()
