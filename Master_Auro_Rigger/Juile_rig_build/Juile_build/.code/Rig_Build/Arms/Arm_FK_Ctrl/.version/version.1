from vtool.maya_lib import rigs
import maya.cmds as cmds

def main():
    # List of sides
    sides = ['l', 'r']
    
    # Loop for Arms
    for arm in sides:
        # Find FK Arm joints for the current side
        FKArm = [
            i for i in process.get_option("FK_Arm", group="IKFK")
            if i.endswith('_%s' % arm)  # Ensure the name ends with the correct side
        ]
        
        # Debugging: Print the joints for the current side
        print("Found FK Arm Joints for side '%s': %s" % (arm, FKArm))
        
        # Skip if no joints are found for the current side
        if not FKArm:
            cmds.warning("No FK Arm joints found for side '%s'!" % arm)
            continue

        # Create FK rig for the arm
        ArmRig = rigs.FkRig("FK_Arm", arm)  # Pass the correct side (arm) here
        ArmRig.set_joints(FKArm)
        ArmRig.set_control_size(8)
        ArmRig.set_control_offset_axis("z")
        #ArmRig.set_buffer(True)
        ArmRig.delete_setup()
        ArmRig.create()
        
    cmds.parent("controls_FK_Arm_1_L", "CNT_CLAVICLE_1_L")
    cmds.parent("controls_FK_Arm_1_R", "CNT_CLAVICLE_1_R")
