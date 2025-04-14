from vtool.maya_lib import rigs
from vtool.maya_lib import rigs_util

def main():
    
    joints = process.get_option("Hip", group="Joint")
    Ctrlgrp = process.get_option("Ctrl_grp", group = "Groups")
    
    hips = rigs.SparseRig('Hips', 'C')
    hips.set_joints(joints)
    hips.set_attach_joints(True)
    hips.set_control_to_pivot(True)
    hips.set_create_sub_control(False)
    hips.set_control_shape('circle')
    hips.set_control_offset_axis('z')
    hips.set_control_size(25)
    hips.set_number_in_control_name(False)
    #hips.set_control_shape("pelvis")
    
    
    hips.delete_setup()
    hips.create()
    
    hips.set_control_parent("CNT_SUB_COG_1_C")
    
    return