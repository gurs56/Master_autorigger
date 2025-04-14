import maya.cmds as cmds

def main():
    sides = ['l', 'r']
    
    for side in sides:
        # Define the root joint for duplication
        foot_joint = 'JNT_foot_%s' % side
        
        # Check if the foot joint exists
        if not cmds.objExists(foot_joint):
            cmds.warning("Foot joint '%s' does not exist! Skipping." % foot_joint)
            continue
        
        try:
            # Duplicate the foot joint hierarchy
            duplicated_hierarchy = cmds.duplicate(foot_joint, rc=True)  # Duplicate the hierarchy
            duplicated_root = duplicated_hierarchy[0]
            
            # Unparent all duplicated joints
            all_duplicated_joints = [duplicated_root] + (cmds.listRelatives(duplicated_root, ad=True, type='joint') or [])
            for joint in all_duplicated_joints:
                try:
                    cmds.parent(joint, world=True)
                except RuntimeError as e:
                    cmds.warning("Could not unparent joint '%s': %s" % (joint, str(e)))
            
            # Rename all duplicated joints
            renamed_joints = {}
            for joint in all_duplicated_joints:
                # Determine the new name based on the joint type
                if 'ball' in joint.lower():
                    new_name = 'JNT_FOOT_BALL_%s' % side
                elif 'toe' in joint.lower():
                    new_name = 'JNT_FOOT_TOE_%s' % side
                elif 'foot' in joint.lower():
                    new_name = 'JNT_FOOT_%s' % side
                else:
                    continue  # Skip joints not in the naming scheme
                
                # Rename and store the mapping
                new_name = cmds.rename(joint, new_name)
                renamed_joints[joint] = new_name
            
            # Apply orientation constraints
            for original_joint, new_joint in renamed_joints.items():
                original_name = original_joint.replace('JNT_FOOT_', 'JNT_').replace('_BALL', '_ball').replace('_TOE', '_toe')
                if cmds.objExists(original_name):
                    cmds.orientConstraint(original_name, new_joint, mo=False)
                    print("Constrained %s -> %s" % (original_name, new_joint))
                else:
                    cmds.warning("Original joint '%s' does not exist! Skipping constraint." % original_name)

            print("Successfully duplicated and constrained joints for side '%s'." % side)
        
        except RuntimeError as e:
            cmds.warning("Error processing side '%s': %s" % (side, str(e)))
