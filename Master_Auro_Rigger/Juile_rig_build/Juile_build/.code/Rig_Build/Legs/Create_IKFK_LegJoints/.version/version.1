import maya.cmds as cmds

def get_joint_suffix(name, suffix):
    """
    Replace the joint prefix (e.g., 'JNT') with the provided suffix (IK/FK).
    """
    return name.replace("JNT", "JNT" + suffix)

def duplicate_joints(joint_list, suffix):
    """
    Duplicate joints with a specific suffix and return the new joint list.
    """
    duplicated_joints = []  # Initialize the list to store duplicated joints
    for joint in joint_list:
        if cmds.objExists(joint):
            # Duplicate the joint, keeping its position and orientation
            dup_joint = cmds.duplicate(joint, name=get_joint_suffix(joint, suffix), po=True)[0]
            duplicated_joints.append(dup_joint)
        else:
            cmds.warning("Joint '{}' does not exist!".format(joint))
    return duplicated_joints

def sort_joints(joint_list, target_names):
    """
    Sorts the joints based on the hierarchy defined in target_names.
    """
    sorted_joints = []
    for target in target_names:
        for joint in joint_list:
            if target in joint:
                sorted_joints.append(joint)
    return sorted_joints

def parent_joints_debug(joint_list):
    """
    Parent joints in the correct order with debugging information.
    """
    print "Joint List Received:", joint_list
    for i in range(len(joint_list) - 1):
        if cmds.objExists(joint_list[i]) and cmds.objExists(joint_list[i + 1]):
            print "Parenting {} to {}".format(joint_list[i + 1], joint_list[i])
            cmds.parent(joint_list[i + 1], joint_list[i])
        else:
            print "Error: One or both joints do not exist - {} or {}".format(joint_list[i], joint_list[i + 1])

def main():
    """
    Main function to create and parent IK and FK joint chains.
    """
    # Look at all joints 
    ArmJoints = cmds.ls(type='joint')
      
    # Target joint names to look for
    target_names = ["JNT_upperarm", "JNT_lowerarm", "JNT_hand"]
    
    # Lists to store original joints for left and right arms
    LArmJoints = []
    RArmJoints = []
    
    # Loop through all joints and check for matches
    for joint in ArmJoints:
        if "twist" not in joint:  # Exclude twist joints
            for target in target_names:
                if target in joint:
                    if joint.endswith("_l"):
                        LArmJoints.append(joint)
                    elif joint.endswith("_r"):
                        RArmJoints.append(joint)

    # Print results for debugging
    print "Left Arm Joints: {}".format(LArmJoints)
    print "Right Arm Joints: {}".format(RArmJoints)
    
    # Sort the joints based on the target hierarchy
    LArmJoints = sort_joints(LArmJoints, target_names)
    RArmJoints = sort_joints(RArmJoints, target_names)

    # Duplicate IK and FK joints for left and right arms
    ik_joints_left = duplicate_joints(LArmJoints, "_IK")
    fk_joints_left = duplicate_joints(LArmJoints, "_FK")
    ik_joints_right = duplicate_joints(RArmJoints, "_IK")
    fk_joints_right = duplicate_joints(RArmJoints, "_FK")
    
    # Parent the IK and FK joints in the correct order
    parent_joints_debug(ik_joints_left)  # Parent left IK joints
    parent_joints_debug(fk_joints_left)  # Parent left FK joints
    parent_joints_debug(ik_joints_right)  # Parent right IK joints
    parent_joints_debug(fk_joints_right)  # Parent right FK joints
    
    # Print final results
    print "Left Arm IK Joints: {}".format(ik_joints_left)
    print "Left Arm FK Joints: {}".format(fk_joints_left)
    print "Right Arm IK Joints: {}".format(ik_joints_right)
    print "Right Arm FK Joints: {}".format(fk_joints_right)

    return
