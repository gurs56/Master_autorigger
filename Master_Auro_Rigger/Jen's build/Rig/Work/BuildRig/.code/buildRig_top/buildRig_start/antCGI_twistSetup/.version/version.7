from vtool.maya_lib import attr


def main():
    
    body_parts = ['upperarm', 'lowerarm', 'thigh', 'calf']
    sides = ['l', 'r']
    setup = process.get_option( 'setup Grp' , group = 'Groups' )    
    twistSetup = cmds.group( em=1, n='twist_setup', p = setup )

    for side in sides:
        for body in body_parts:
            bodyBnd_top = 'JNT_%s_%s' % (body , side)
            twistBnd_top = 'JNT_%s_twist_01_%s' % ( body , side )
            twistBnd_btm = 'JNT_%s_twist_02_%s' % ( body , side )
            twistBnd_aim = cmds.listRelatives( # like calf to thigh or foot to calf
                        'JNT_%s_%s' % ( body , side ), 
                        ad=0 , 
                        type = 'joint'
                        )[1]
            fol_top = 'FOLLOW_%s_twist_01_%s' % ( body , side )
            fol_btm = 'FOLLOW_%s_twist_02_%s' % ( body , side )
            
            
            # create twist follow system
            
            twistFollows = cmds.duplicate( twistBnd_top , renameChildren = 1 )
            cmds.rename( twistFollows[0], fol_top )
            cmds.rename( twistFollows[1], fol_btm )
            aim_loc = '%s_aim_%s' % (body , side)
            cmds.spaceLocator(
                        n = aim_loc
                        )[0]
                        
            pc_temp = cmds.parentConstraint( fol_top , aim_loc, mo = 0 )
            cmds.delete(pc_temp)
            
            cmds.parent( aim_loc , fol_top )
            cmds.parent( fol_top , twistSetup )
            cmds.refresh()
            cmds.select(cl=1)
            
            # constraints
            # do if side ..?
            aim_loc_path = cmds.ls(aim_loc, l=1)[0]
            cmds.aimConstraint( 
                    twistBnd_aim , twistBnd_top ,
                    aim = [1, 0, 0],
                    u = [0, 0, 1],
                    wut = 'object',
                    wuo = aim_loc_path
                    )
                  
            fol_ikHandle = cmds.ikHandle( n = '%s_follow_ik_%s' % ( body ,  side ), startJoint = fol_top , endEffector = fol_btm , sol = 'ikRPsolver' )
            pc_temp = cmds.parentConstraint( twistBnd_aim , fol_ikHandle[0], mo = 0 )
            cmds.delete(pc_temp)
            cmds.parent( fol_ikHandle , twistBnd_aim )
            
            for a in 'xyz':
                cmds.setAttr('%s.poleVector%s' % ( fol_ikHandle[0] , a.upper() ) , 0)
            
            for index, i in enumerate([bodyBnd_top, twistBnd_top, twistBnd_btm, twistBnd_aim, fol_top, fol_btm, twistFollows, aim_loc, fol_ikHandle]):
                print index, i
            
            # connect to second twist jnt
            
            attr.connect_multiply( source_attribute = '%s.rotateX' % bodyBnd_top , target_attribute = '%s.rotateX' % twistBnd_btm , value=0.5)
            '''
            multi = attr.MultiplyDivideNode('%s_%s' % ( body ,  side ))
            multi.set_operation(1)
            multi.input1X_in('%s.rotateX' % bodyBnd_top)
            multi.set_input2(valueX = .5)
            multi.outputX_out('%s.rotateX' % twistBnd_btm)
            '''
            
            if body.find('arm') != -1:
                cmds.parentConstraint( 'JNT_spine_05', fol_top , mo=1)
            else:
                cmds.parentConstraint( 'JNT_pelvis', fol_top , mo=1)
    
    return