import maya.cmds as cmds

def connect_switch_to_constraints_and_visibility(joint_list, switch_control, attribute_name, ik_items, fk_items):
    """
    Connect IK/FK switch control to the parent constraint weights and toggle visibility of IK/FK items.

    Args:
        joint_list (list): List of joints with existing parent constraints.
        switch_control (str): Name of the switch control (e.g., 'l_Arm_SWITCH' or 'r_Arm_SWITCH').
        attribute_name (str): The IK/FK switch attribute name on the control.
        ik_items (list): List of IK controls and joints to toggle visibility.
        fk_items (list): List of FK controls and joints to toggle visibility.
    """
    # Set up reverse node for visibility
    reverse_node = "{}_reverse".format(switch_control)
    if not cmds.objExists(reverse_node):
        reverse_node = cmds.createNode('reverse', name=switch_control + "_reverse")
        cmds.connectAttr('{}.{}'.format(switch_control, attribute_name), reverse_node + ".inputX", force=True)
    else:
        reverse_node = "{}_reverse".format(switch_control)

    # Toggle IK/FK items visibility
    for ik_item in ik_items:
        if cmds.objExists(ik_item):
            cmds.connectAttr('{}.{}'.format(switch_control, attribute_name), '{}.visibility'.format(ik_item), force=True)

    for fk_item in fk_items:
        if cmds.objExists(fk_item):
            cmds.connectAttr(reverse_node + ".outputX", '{}.visibility'.format(fk_item), force=True)

    # Connect the switch to constraints
    for joint in joint_list:
        constraints = cmds.listRelatives(joint, type='parentConstraint')
        if not constraints:
            cmds.warning("No parent constraint found on joint '{}'.".format(joint))
            continue

        constraint = constraints[0]
        targets = cmds.parentConstraint(constraint, query=True, targetList=True)
        if len(targets) < 2:
            cmds.warning("Constraint '{}' on joint '{}' does not have two targets.".format(constraint, joint))
            continue

        ik_weight = '{}.{}W0'.format(constraint, targets[0])
        fk_weight = '{}.{}W1'.format(constraint, targets[1])

        cmds.connectAttr('{}.{}'.format(switch_control, attribute_name), ik_weight, force=True)
        cmds.connectAttr(reverse_node + ".outputX", fk_weight, force=True)

        print("Connected '{}' to '{}' and '{}' weights on '{}'.".format(
            '{}.{}'.format(switch_control, attribute_name), ik_weight, fk_weight, constraint))

def main():
    # Retrieve joint lists from process options for arms
    arm_list_l = process.get_option("Arm_L", group="Joint")
    arm_list_r = process.get_option("Arm_R", group="Joint")

    # Define IK/FK switch controls and associated controls and joints for visibility
    switches = {
        "l_Arm_SWITCH": {
            "joint_list": arm_list_l,
            "ik_items": ["controls_IK_Arm_1_L", "JNT_IK_upperarm_l"],
            "fk_items": ["controls_FK_Arm_1_L", "JNT_FK_upperarm_l"]
        },
        "r_Arm_SWITCH": {
            "joint_list": arm_list_r,
            "ik_items": ["controls_IK_Arm_1_R", "JNT_IK_upperarm_r"],
            "fk_items": ["controls_FK_Arm_1_R", "JNT_FK_upperarm_r"]
        }
    }
    switch_attribute = "IKFK_SWITCH"

    # Process each switch
    for switch_control, data in switches.items():
        connect_switch_to_constraints_and_visibility(
            joint_list=data["joint_list"],
            switch_control=switch_control,
            attribute_name=switch_attribute,
            ik_items=data["ik_items"],
            fk_items=data["fk_items"]
        )

    print("IK/FK switch connections and visibility toggles completed for arms.")
