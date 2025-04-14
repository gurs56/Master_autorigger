from vtool.maya_lib import rigs
from vtool.maya_lib import rigs_util
from vtool.maya_lib import attr


def main():
    
    # vars
    sides = ['l', 'r']
    rigGrp = process.get_option( 'rig Grp' , group = 'Groups' )
    controlsGrp = process.get_option( 'controls Grp' , group = 'Groups' )    
    setupGrp = process.get_option( 'setup Grp' , group = 'Groups' )    
    subGround2 = process.get_option('sub ground 2', group = 'Groups')
    subCog = 'CNT_SUB_COG_C'
    hips = 'CNT_SUB_HIPS_C'
    
    setup_grp = process.get_option( 'setup Grp' , group = 'Groups' )   
    
    for side in sides:
        
        joints = ['IK_foot_%s'%side, 'IK_ball_%s'%side, 'IK_toe_%s'%side]
        
        # ik foot roll setup
        foot_roll = rigs.FootRig('FootRoll',side=side)
        foot_roll.set_joints(joints)
        foot_roll.set_attach_joints(True)
        foot_roll.set_pivot_locators('Heel_%s_Loc' %side.upper(), 'BallYawIn_%s_Loc' %side.upper(), 'BallYawOut_%s_Loc' %side.upper())
        foot_roll.set_sub_visibility(True)
        foot_roll.set_ik_parent('xform_ikHandle_ik_Leg_1_%s' % side.upper() )
        foot_roll.set_control_size(5)
        foot_roll.set_control_offset_axis('Z')
        foot_roll.set_attribute_control( 'CNT_IK_LEG_BTM_1_%s' % side.upper() )
        
        foot_roll.set_toe_control_as_sub_control(True)
        
        
        
        foot_roll.set_forward_roll_axis('Y')
        foot_roll.set_side_roll_axis('X')
        
        '''
        foot_roll.set_toe_rotate_axis(axis='Z')
        foot_roll.set_top_roll_axis('X')
        '''
        foot_roll.set_create_foot_roll(True)
        
        
        foot_roll.create()
        foot_roll.set_control_parent('CNT_SUB_IK_LEG_BTM_1_%s' % side.upper() )
        
        cmds.parentConstraint( 'CNT_FOOTROLL_BALL_1_%s' % side.upper(), 'xform_ikHandle_ik_Leg_1_%s' % side.upper(), mo=1 )
            
        
        foot_roll.set_control_parent('CNT_SUB_IK_LEG_BTM_1_%s' % side.upper() )
        foot_roll.set_setup_parent(setup_grp)
        
        
    
    
    
    
    
    return