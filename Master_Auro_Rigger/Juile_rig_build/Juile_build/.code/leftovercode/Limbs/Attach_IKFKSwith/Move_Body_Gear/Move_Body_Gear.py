import maya.cmds as cmds

def match_position_quick(source, target):
    """
    Quickly matches the position of the target to the source.
    :param source: The name of the source object.
    :param target: The name of the target object.
    """
    if not cmds.objExists(source) or not cmds.objExists(target):
        cmds.warning("One or both objects do not exist!")
        return

    # Create a pointConstraint to snap position
    temp_constraint = cmds.pointConstraint(source, target, maintainOffset=False)
    
    # Delete the constraint immediately after snapping
    #cmds.delete(temp_constraint)
    print("Position of %s matched to %s." % (target, source))


match_position_quick('JNT_hand_l', 'xform_L_Arm_SWITCH')
match_position_quick('JNT_hand_r', 'xform_R_Arm_SWITCH')
match_position_quick('JNT_foot_l', 'xform_L_Leg_SWITCH')
match_position_quick('JNT_foot_r', 'xform_R_Leg_SWITCH')
