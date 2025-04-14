from vtool.maya_lib import rigs

def main():
    
    # set vars
    joints = ['JNT_gasTank_c', 'JNT_backpackZipper_l', 'JNT_calfJet_l', 'JNT_calfJet_r']
    sparseJnt_parentCnt_dict =  process.get_option( 'sparseJnt_parentCnt_dict' , group = 'Groups' ) 
    
    
    for jnt in joints:
        
        # set vars
        control_parent = sparseJnt_parentCnt_dict[jnt]
        side = jnt[-1]
        name = jnt.split('_')[1]
        setupGrp = process.get_option( 'setup Grp' , group = 'Groups' )    
        
        # create rig 
        rig = rigs.SparseRig(name, side)
            
        rig.set_joints(jnt)
        rig.set_control_size(10)
        rig.set_control_shape('cube')
        rig.set_create_sub_control(True)
        rig.set_sub_visibility(False)
    
        rig.delete_setup()
        rig.create()
        rig.set_control_parent(control_parent)
        
    return