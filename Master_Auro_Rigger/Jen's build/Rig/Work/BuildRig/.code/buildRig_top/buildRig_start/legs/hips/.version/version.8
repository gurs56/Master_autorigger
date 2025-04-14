from vtool.maya_lib import rigs
from vtool.maya_lib import rigs_util

def main():
    
    # vars
    
    rigGrp = process.get_option( 'rig Grp' , group = 'Groups' )
    controlsGrp = process.get_option( 'controls Grp' , group = 'Groups' )    
    joints = process.get_option('pelvis', group = 'Rig Bone Groups')
    subGround2 = process.get_option('sub ground 2', group = 'Groups')
    cogSub = 'CNT_SUB_COG_C'
    # cog controller
    
    hips = rigs.SparseRig('Hips', 'C')
    hips.set_joints(joints)
    hips.set_attach_joints(True)
    hips.set_control_to_pivot(True)
    hips.set_create_sub_control(True)
    #rig.set_sub_visibility(False)
    hips.set_control_shape('circle')
    hips.set_control_offset_axis('z')
    hips.set_control_size(4)
    #rig.set_control_color(22)
    #cog.set_scalable(True)
    #rig.set_sub_control_color(17)
    #rig.set_attach_type('hi')
    hips.set_number_in_control_name(False)
    
    
    #rig.set_scalable(True, keep_negative_scale_on_joint=False)
    
    hips.delete_setup()
    hips.create()
    
    hips.set_control_parent( cogSub )
    subHips = hips.get_all_controls()[0]
    subHips_noNumber = subHips.replace('_1', '')
    
    cmds.rename(subHips, subHips_noNumber)
    
    
    return