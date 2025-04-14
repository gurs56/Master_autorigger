from vtool.maya_lib import rigs
from vtool.maya_lib import rigs_util

def main():
    
    joint_name = "JNT_head"
    if cmds.objExists(joint_name) and cmds.nodeType(joint_name) == "joint":
        print("Joint '{}' found.".format(joint_name))
    else:
        print("Joint '{}' not found.".format(joint_name))
        
    head = rigs.SparseRig("head", "C")
    head.set_joints(joint_name)
    head.set_control_offset_axis("z")
    head.set_control_size(15)
    head.set_create_sub_control(False)
    
    head.delete_setup()
    head.create()
    head.set_control_parent("CNT_NECK_2_C")

    
    return