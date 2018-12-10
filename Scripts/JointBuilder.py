import maya.cmds as cmds


class JointCreator:
    def __init__(self):
        pass

    def ChainBuilder(self):
        sels = cmds.ls(selection=True)
        print(sels)
        i = 0
        joints = []

        for obj in sels:
            bbox = cmds.xform(obj, boundingBox=True, q=True)
            pivot = [(bbox[0] + bbox[3]) / 2, (bbox[1] + bbox[4]) / 2, (bbox[2] + bbox[5]) / 2]
            jnt = cmds.joint(obj)
            joints.append(jnt)
            deparenter = obj + '|' + jnt
            cmds.parent(deparenter, world=True)
            cmds.xform(jnt, translation=pivot, worldSpace=True)
            o = i - 1
            if i >= 1:
                print(joints)
                cmds.parent(jnt, joints[o])
            i += 1
