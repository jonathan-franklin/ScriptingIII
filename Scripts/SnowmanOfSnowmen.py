# Importing the Maya command set.
import maya.cmds as cmds

# Creating snowman base
cmds.polySphere( r = True, sx = 20, sy = 20, ax = [0,1,0], cuv = 2, ch = 1)
# Result: pSphere1 polySphere1 # 
cmds.duplicate( rr = True)
# Result: pSphere2 #
cmds.move( 0, 1.831615, 0, r = True, os = True, wd = True )
cmds.scale( 0.687349, 0.687349, 0.687349, r = True )
cmds.move( 0, -0.244511, 0, r = True, os = True, wd = True )
cmds.duplicate( rr = True)
# Result: pSphere3 #
cmds.move( 0, 1.1459, 0, r = True, os = True, wd = True )
cmds.scale( 0.758657, 0.758657, 0.758657, r = True )
cmds.move( 0, -0.127419, 0, r = True, os = True, wd = True )
cmds.select( 'pSphere2', tgl = True )
cmds.move( 0, -0.245208, 0, r = True, os = True, wd = True )
cmds.select( clear = True )
cmds.select( 'pSphere1', r = True )
cmds.scale( 0.91359, 0.91359, 0.91359, r = True )
cmds.move( 0, 0.123063, 0, r = True, os = True, wd = True )
cmds.scale( 0.946528, 0.946528, 0.946528, r = True )
cmds.select( 'pSphere2', r = True )
cmds.scale( 1.03269, 1.03269, 1.03269, r = True )
cmds.select( clear = True )

# Creating the eyes
cmds.select( 'pSphere3', r = True )
cmds.duplicate( rr = True )
# Result: pSphere4 #
cmds.move( 0, 0, 0.399153, r = True, os = True, wd = True )
cmds.scale( 0.100295, 0.100295, 0.100295, r = True )
cmds.move( 0, 0, 0.170178, r = True, os = True, wd = True )
cmds.move( 0.093911, 0, 0, r = True, os = True, wd = True )
cmds.move( 0, 0, -0.073005, r = True, os = True, wd = True)
cmds.move( 0, 0.201061, 0, r = True, os = True, wd = True )
cmds.move( 0.0733562, 0, 0, r = True, os = True, wd = True )
cmds.move( 0, 0, -0.0288609, r = True, os = True, wd = True )
cmds.duplicate( rr = True )
# Result: pSphere5 #
cmds.move( -0.334948, 0, 0, r = True, os = True, wd = True )

cmds.select( 'pSphere5', r = True )
cmds.duplicate( rr = True )
# Result: pSphere6 #
cmds.move( 0, -0.775448, 0, r = True, os = True, wd = True )
cmds.move( 0.16518, 0, 0, r = True, os = True, wd = True )
cmds.move( 0, 0, 0.0958376, r = True, os = True, wd = True )
cmds.duplicate( rr = True )
# Result: pSphere7 #
cmds.move( 0, -0.359811, 0, r = True, os = True, wd = True )
cmds.move( 0, 0, 0.121033, r = True, os = True, wd = True )
cmds.move( 0.0400222, 0, 0, r = True, os = True, wd = True )
cmds.move( 0, 0.0323785, 0, r = True, os = True, wd = True )
cmds.move( 0, -0.117729, 0, r = True, os = True, wd = True )
cmds.duplicate( rr = True )
# Result: pSphere8 #
cmds.move( 0, 0.227476, 0, r = True, os = True, wd = True )
cmds.move( -0.0329691, 0, 0, r = True, os = True, wd = True )
cmds.select( 'pSphere7', r = True )
cmds.move( -0.0444484, 0, 0, r = True, os = True, wd = True )
cmds.select( 'pSphere8', r = True )
cmds.move( 0.0109526, 0, 0, r = True, os = True, wd = True )
cmds.select( cl = True )
cmds.select( 'pSphere7', r = True )
cmds.move( 0, 0, 0.0199912, r = True, os = True, wd = True )
cmds.select( 'pSphere8', r = True )
cmds.move( 0, 0, -0.0118007, r = True, os = True, wd = True )
cmds.select( cl = True )

# Creating the nose
cmds.polyCone( r = 1, h = 2, sx = 20, sy = 1, sz = 0, ax = [0,1,0], rcp = 0, cuv = 3, ch = 1)
# Result: pCone1 polyCone(1 #
cmds.scale( 0.218177, 1, 0.218177, r = True )
cmds.rotate( 82.88842, 0, 0, r = True, os = True, fo = True )
cmds.move( 0, 0, -2.239144, r = True, os = True, wd = True )
cmds.move( 0, 1.121513, 0, r = True, os = True, wd = True )
cmds.move( -0.0287692, 0, 0, r = True, os = True, wd = True )
cmds.scale( 0.354904, 0.354904, 0.354904, r = True )
cmds.move( 0.0219252, 0, 0, r = True, os = True, wd = True )
cmds.rotate( 7.347216, 0, 0, r = True, os = True, fo = True )
cmds.scale( 0.891399, 0.891399, 0.891399, r = True )
cmds.move( 0, -0.0157479, 0, r = True, os = True, wd = True )
cmds.select( 'pSphere2', 'pSphere1', r = True )
cmds.select( cl = True )

# Creating the hat
cmds.polyCylinder( r = 1, h = 2, sx = 20, sy = 1, sz = 1, ax = [0,1,0], rcp = 0, cuv = 3, ch = 1)
# Result: pCylinder1 polyCylinder(1 #
cmds.move( 0, 3.366916, 0, r = True, os = True, wd = True )
cmds.scale( 0.219513, 0.219513, 0.219513, r = True )
cmds.select( 'pCylinder1.e[40:59]', r = True)
cmds.polySplitRing( ch = 1, splitType = 1, weight = 0.0534432, smoothingAngle = 30, fixQuads = 1, insertWithEdgeFlow = 0 )
# Result: polySplitRing(1 #
cmds.select( 'pCylinder1.e[102]', 'pCylinder1.e[104]', 'pCylinder1.e[106]', 'pCylinder1.e[108]', 'pCylinder1.e[110]', 'pCylinder1.e[112]', 'pCylinder1.e[114]', 'pCylinder1.e[116]', 'pCylinder1.e[118]', 'pCylinder1.e[120]', 'pCylinder1.e[122]', 'pCylinder1.e[124]', 'pCylinder1.e[126]', 'pCylinder1.e[128]', 'pCylinder1.e[130]', 'pCylinder1.e[132]', 'pCylinder1.e[134]', 'pCylinder1.e[136]', 'pCylinder1.e[138:139]', d = True )
cmds.select( 'pCylinder1.f[0:19]', r = True )
cmds.polyExtrudeFacet( 'pCylinder1.f[0:19]', constructionHistory = 1, keepFacesTogether = 1, pvx = -2.616802758e-08, pvy = 3.159133989, pvz = -3.925204138e-08, divisions = 1, twist = 0, taper = 1, off = 0, thickness = 0, smoothingAngle = 30 )
# Result: polyExtrudeFace1 #
cmds.setAttr( "polyExtrudeFace1.localTranslate", 0,0,0.131562, type = 'double3' )
cmds.select( 'pCylinder1', r = True )
cmds.move( 0, -0.342669, 0, r = True, os = True, wd = True )
cmds.rotate( 0, 0, -10.710335, r = True, os = True, fo = True )
cmds.move( 0.124312, 0, 0, r = True, os = True, wd = True )
cmds.move( 0, 0.0149343, 0, r = True, os = True, wd = True )
cmds.move( 0, 0.00669382, 0, r = True, os = True, wd = True )
cmds.select( cl = True )

cmds.polyCube( w = 1, h = 1, d = 1, sx = 1, sy = 1, sz = 1, ax = [0,1,0], cuv = 4, ch = 1)
# Result: pCube1 polyCube1 #
cmds.move( 1.249354, 2.168872, 0, r = True, os = True, wd = True )
cmds.scale( 1, 0.0419897, 1, r = True )
cmds.scale( 1, 1, 0.0345664, r = True )
cmds.duplicate( rr = True )
# Result: pCube2 #
cmds.rotate( 0, 0, 31.20481, r = True, os = True, fo = True )
cmds.move( 0.353212, 0, 0, r = True, os = True, wd = True )
cmds.scale( 0.458048, 0.458048, 0.458048, r = True )
cmds.move( -0.12073, 0, 0, r = True, os = True, wd = True )
cmds.select( 'pCube1', r = True )
cmds.select( 'pCube2', 'pCube1', r = True )
cmds.polyUnite( 'pCube2', 'pCube1', ch = 1, mergeUVSets = 1, centerPivot = True, name = 'pCube2')
# Result: pCube3 cmds.polyUnite(1 #
cmds.rotate( 0, 0, 21.969225, r = True, os = True, fo = True )
cmds.move( -0.359507, 0, 0, r = True, os = True, wd = True )
cmds.move( 0, -0.286094, 0, r = True, os = True, wd = True )
cmds.duplicate( rr = True )
# Result: pCube4 #
cmds.move( -1.958762, 0.946035, 0, r = True, os = True, wd = True )
cmds.rotate( 0, -102.255783, 0, r = True, os = True, fo = True )
cmds.rotate( 0, -55.460015, 0, r = True, os = True, fo = True )
cmds.rotate( 0, 0, 42.946565, r = True, os = True, fo = True )
cmds.move( -0.157962, 0, 0, r = True, os = True, wd = True )
cmds.move( 0, -0.092327, 0, r = True, os = True, wd = True )
cmds.move( 0, 0, -0.169901, r = True, os = True, wd = True )
cmds.select( 'pCube3', r = True )
cmds.rotate( 0, -10.700004, 0, r = True, os = True, fo = True )
cmds.move( 0, 0, 0.0737085, r = True, os = True, wd = True )
cmds.select( 'pCube4', r = True )
cmds.rotate( -52.892484, 0, 0, r = True, os = True, fo = True )
cmds.select( cl = True )

# Combine into finished snowman
cmds.select('pSphere3', 'pSphere2', 'pCube3', 'pCube4', 'pSphere7', 'pSphere1', 'pSphere5', 'pSphere4', 'pSphere6', 'pSphere8', 'pCylinder1', 'pCone1', r = True)
cmds.polyUnite('pSphere3', 'pSphere2', 'pCube3', 'pCube4', 'pSphere7', 'pSphere1', 'pSphere5', 'pSphere4', 'pSphere6', 'pSphere8', 'pCylinder1', 'pCone1', ch = 1, mergeUVSets = 1, centerPivot = True, name = 'Snowman' )
cmds.delete( ch = 1, all = 1)

cmds.polySphere( r = 10, sx = 20, sy = 20, ax = [0,1,0], cuv = 2, ch = 1)
# Result: pSphere1 polySphere1
cmds.select( 'pSphere1.vtx[0:381]', r = True )
selection = cmds.ls( sl = True )
for each in selection:
    print(each)