import maya.cmds as cmds

def parent_constrain_to_bind(joint_pairs):
    """
    Apply parent constraints to bind joints based on corresponding IK and FK joints.

    Args:
    joint_pairs (list of tuples): Each tuple contains three joints in the order (IK joint, FK joint, Bind joint).
    """
    for pair in joint_pairs:
        ik_joint, fk_joint, bind_joint = pair
        # Check if all joints in the pair exist
        if cmds.objExists(ik_joint) and cmds.objExists(fk_joint) and cmds.objExists(bind_joint):
            cmds.parentConstraint(ik_joint, fk_joint, bind_joint, mo=True)
        else:
            # Warn if any joint in the pair does not exist
            cmds.warning("One or more joints do not exist: {}, {}, {}".format(ik_joint, fk_joint, bind_joint))

# Example usage
joint_pairs = [
    # Left arm
    ("JNT_IK_upperarm_l", "JNT_FK_upperarm_l", "JNT_upperarm_l"),
    ("JNT_IK_lowerarm_l", "JNT_FK_lowerarm_l", "JNT_lowerarm_l"),
    ("JNT_IK_hand_l", "JNT_FK_hand_l", "JNT_hand_l"),
    # Right arm
    ("JNT_IK_upperarm_r", "JNT_FK_upperarm_r", "JNT_upperarm_r"),
    ("JNT_IK_lowerarm_r", "JNT_FK_lowerarm_r", "JNT_lowerarm_r"),
    ("JNT_IK_hand_r", "JNT_FK_hand_r", "JNT_hand_r")
]
parent_constrain_to_bind(joint_pairs)


