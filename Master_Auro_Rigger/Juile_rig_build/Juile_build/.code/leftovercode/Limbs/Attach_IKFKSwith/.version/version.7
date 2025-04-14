import maya.cmds as cmds

def connect_ikfk_switch():
    print("Starting IK/FK switch connections...")
    
    limbs = {
        'L_Arm': {
            'switch_control': 'L_Arm_SWITCH',
            'constraints': [
                'JNT_upperarm_l_parentConstraint1',
                'JNT_lowerarm_l_parentConstraint1',
                'JNT_hand_l_parentConstraint1'
            ]
        },
        'R_Arm': {
            'switch_control': 'R_Arm_SWITCH',
            'constraints': [
                'JNT_upperarm_r_parentConstraint1',
                'JNT_lowerarm_r_parentConstraint1',
                'JNT_hand_r_parentConstraint1'
            ]
        },
        'L_Leg': {
            'switch_control': 'L_Leg_SWITCH',
            'constraints': [
                'JNT_calf_l_parentConstraint1',
                'JNT_thigh_l_parentConstraint1',
                'JNT_foot_l_parentConstraint1',
                'JNT_ball_l_parentConstraint1',
                'JNT_toe_l_parentConstraint1'
            ]
        },
        'R_Leg': {
            'switch_control': 'R_Leg_SWITCH',
            'constraints': [
                'JNT_calf_r_parentConstraint1',
                'JNT_thigh_r_parentConstraint1',
                'JNT_foot_r_parentConstraint1',
                'JNT_ball_r_parentConstraint1',
                'JNT_toe_r_parentConstraint1'
            ]
        }
    }

    for limb, data in limbs.items():
        print("Processing limb: %s" % limb)
        switch_control = data['switch_control']
        constraints = data['constraints']

        if not cmds.objExists('%s.IKFK_SWITCH' % switch_control):
            cmds.warning("Switch control '%s' does not have an 'IKFK_SWITCH' attribute!" % switch_control)
            continue

        for constraint in constraints:
            if cmds.objExists(constraint):
                print("Connecting constraint: %s" % constraint)
                cmds.connectAttr('%s.IKFK_SWITCH' % switch_control, '%s.w0' % constraint, force=True)
                
                reverse_node = cmds.createNode('reverse', name='%s_reverse' % constraint)
                cmds.connectAttr('%s.IKFK_SWITCH' % switch_control, '%s.inputX' % reverse_node, force=True)
                cmds.connectAttr('%s.outputX' % reverse_node, '%s.w1' % constraint, force=True)
            else:
                cmds.warning("Constraint '%s' does not exist!" % constraint)

connect_ikfk_switch()