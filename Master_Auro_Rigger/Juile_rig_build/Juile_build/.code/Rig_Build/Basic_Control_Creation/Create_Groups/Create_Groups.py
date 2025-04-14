import maya.cmds as cmds
from vtool.maya_lib import core

def main():
    # Create the master group as empty
    Juile_Rig = cmds.group(empty=True, name="Juile_Rig")
    print("Created master group: {}".format(Juile_Rig))  # Debugging print

    # List of asset group names
    Asset_Grps = ["Joints_Group", "Geo_Group", "RigParts"]

    # Loop through the list and create/parent each group
    for group_name in Asset_Grps:
        # Create the empty group
        NewGrp = cmds.group(empty=True, name=group_name)
        print("Created group: {}".format(NewGrp))  # Debugging print
        
        # Parent the new group to the Juile_Rig group
        cmds.parent(NewGrp, Juile_Rig)
        print("Parented {} to {}".format(NewGrp, Juile_Rig))  # Debugging print
        
    # Create the Control Group and parent it to "RigParts"
    Control_grp = cmds.group(empty=True, name="Control_Group")
    cmds.parent("Control_Group", "RigParts")  
    print("Created control group: {}".format(Control_grp))  # Debugging print

    # Force Maya to refresh the scene
    cmds.refresh(force=True)

    # Check if the groups exist in the scene
    for group_name in Asset_Grps:
        if cmds.objExists(group_name):
            print("{} exists in the scene.".format(group_name))
        else:
            print("{} does not exist in the scene.".format(group_name))

    return

