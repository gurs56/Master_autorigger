from vtool.maya_lib import rigs
from vtool.maya_lib import rigs_util

def main():
    
    # vars
    
    subGround2 = process.get_option( 'sub ground 2' , group = 'Groups' )
    controlsGrp = process.get_option( 'controls Grp' , group = 'Groups' )
    controlsAttr = 'controlsVis'
    structureGrp = process.get_option( 'structure Grp' , group = 'Groups' )
    structureAttr = 'structureVis'
    modelGrp = process.get_option( 'model Grp' , group = 'Groups' )
    modelAttr = 'modelVis'
    geoLockAttr = 'geoLock'
    setupGrp = process.get_option( 'setup Grp' , group = 'Groups' )
    setupAttr = 'setupVis'
    sizex, sizey, sizez =  cmds.getAttr('%s.boundingBoxMax'%modelGrp)[0]
        
    # create gear cnt
    
    gear = rigs_util.Control( 'CNT_GEAR_1' )
    gear.set_curve_type( 'gear' )
    gear.color(22)
    xform = gear.create_xform( prefix = 'xform' )
    cmds.parent( xform, subGround2 )
    gear.hide_attributes( attributes = None )
    g_name = gear.get()
    # create attrs on gear cnt
    
    cmds.addAttr(g_name, ln = modelAttr, at = 'bool', dv = 1, k = 1)
    cmds.connectAttr(
                '%s.%s' % ( g_name, modelAttr ) , 
                '%s.v' % modelGrp
                    )
                
    cmds.setAttr('%s.%s' % ( g_name, modelAttr ) , k=0, cb=1)
    
    cmds.addAttr(g_name, ln = geoLockAttr, at = 'bool', dv = 1, k = 1)
    geoLock_multiplyNode = cmds.createNode('multiplyDivide', n= 'geoLock_multiplyDivide')
    cmds.connectAttr(
                '%s.%s' % ( g_name, geoLockAttr ) , 
                '%s.input1X'%geoLock_multiplyNode
                    )
    cmds.setAttr('%s.input2X'%geoLock_multiplyNode , 2)
    cmds.connectAttr(
                '%s.outputX'%geoLock_multiplyNode ,
                '%s.overrideDisplayType' % modelGrp
                    )
    cmds.setAttr('%s.overrideEnabled' % modelGrp, 1)
                
    
    cmds.setAttr('%s.%s' % ( g_name, geoLockAttr ) , k=0, cb=1)
    
    cmds.addAttr(g_name, ln = controlsAttr, at = 'bool', dv = 1, k = 1 )
    cmds.connectAttr(
                '%s.%s' % ( g_name, controlsAttr ) , 
                '%s.v' % controlsGrp
                    )
    cmds.setAttr('%s.%s' % ( g_name, controlsAttr ) , k=0, cb=1)
                
    cmds.addAttr(g_name, ln = structureAttr, at = 'bool', dv = 0, k = 1 )
    cmds.connectAttr(
                '%s.%s' % ( g_name, structureAttr ) , 
                '%s.v' % structureGrp
                    )
    cmds.setAttr('%s.%s' % ( g_name, structureAttr ) , k=0, cb=1)
                
    cmds.addAttr(g_name, ln = setupAttr, at = 'bool', dv = 0, k = 1 )
    cmds.connectAttr(
                '%s.%s' % ( g_name, setupAttr ) , 
                '%s.v' % setupGrp
                    )
    cmds.setAttr('%s.%s' % ( g_name, setupAttr ) , k=0, cb=1)
    
    return