from vtool.maya_lib import rigs
from vtool.maya_lib import rigs_util
import maya.cmds as cmds

def main():
    # List of sides
    sides = ['l', 'r']
    
    # Loop through sides and create the rig for each side
    for side in sides:
        # Find clavicle joints for the current side
        ClavJoint = [
            i for i in process.get_option("Arms", group="Joint")
            if i.find('JNT_clavicle_%s' % side) != -1
        ]
        
        # Debugging: Print joints found for the side
        print("Found Clavicle Joints for side '%s': %s" % (side, ClavJoint))
        
        # Skip if no joints found for the side
        if not ClavJoint:
            cmds.warning("No clavicle joints found for side '%s'!" % side)
            continue
        
        # Create the clavicle rig for the current side
        clav = rigs.SparseRig("clavicle", side)
        clav.set_joints(ClavJoint)
        clav.set_attach_joints(True)
        clav.set_control_to_pivot(True)
        clav.set_create_sub_control(False)
        clav.set_control_shape('yaw')
        #clav.set_control_offset_axis('x')
        clav.set_control_size(4)
        clav.delete_setup()
        clav.create()
        clav.set_control_parent("CNT_SPINE_2_C")

    return
