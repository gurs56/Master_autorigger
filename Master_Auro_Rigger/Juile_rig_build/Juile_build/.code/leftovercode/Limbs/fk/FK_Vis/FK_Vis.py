import maya.cmds as cmds

# Lists for switches and FK groups
switch = ["L_Leg_SWITCH", "R_Leg_SWITCH", "L_Arm_SWITCH", "R_Arm_SWITCH"]
FKparentGrp = ["controls_FK_Leg_1_L", "controls_FK_Leg_1_R", "controls_FK_Arm_1_L", "controls_FK_Arm_1_R"]

def connect_fk_visibility():
    if len(switch) != len(FKparentGrp):
        cmds.error("The number of switches and FK parent groups must match!")
        return

    for i, ctrl_switch in enumerate(switch):
        fk_group = FKparentGrp[i]

        if not cmds.objExists(ctrl_switch):
            cmds.warning("Switch '%s' does not exist!" % ctrl_switch)
            continue
        
        if not cmds.objExists(fk_group):
            cmds.warning("FK parent group '%s' does not exist!" % fk_group)
            continue

        # Ensure the IKFK_SWITCH attribute exists
        if not cmds.objExists('%s.IKFK_SWITCH' % ctrl_switch):
            cmds.warning("Switch '%s' does not have an 'IKFK_SWITCH' attribute!" % ctrl_switch)
            continue

        # Connect IKFK_SWITCH to FK visibility
        visibility_attr = '%s.visibility' % fk_group
        ikfk_attr = '%s.IKFK_SWITCH' % ctrl_switch

        # Create a reverse node for the visibility
        reverse_node = cmds.createNode('reverse', name='%s_visibilityReverse' % fk_group)
        
        cmds.connectAttr(ikfk_attr, '%s.inputX' % reverse_node, force=True)
        cmds.connectAttr('%s.outputX' % reverse_node, visibility_attr, force=True)

        print("Connected visibility of '%s' to '%s'" % (fk_group, ctrl_switch))

# Run the function
connect_fk_visibility()
