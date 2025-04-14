from vtool.maya_lib import rigs
from vtool.maya_lib import rigs_util
from vtool.maya_lib import attr


def main():

    for side in ['L','R']:
        rig_fk_leg(side)

def rig_fk_leg(side):
    
    joints = process.get_option("Leg_%s" % side, group="Joint")
    rigparts = process.get_option("RigParts", group="Groups")
    '''
    if stretch:
        rig = rigs.FkScaleRig('leg', side)
    if not stretch:
        rig = rigs.FkRig('leg', side)
    '''
    rig = rigs.FkRig('fk_leg', side)
    rig.set_joints(joints)
    rig.set_buffer(True) 
    rig.set_control_offset_axis('z')
    rig.set_control_size(5)
    #rig.set_control_shape("")
       
    rig.create()

    #control = rigs_util.Control('CNT_LEG_3_%s' % side)
    #control.rotate_shape(0,0,90)

    rig.set_control_parent('CNT_SUB_COG_1_C')
    rig.set_setup_parent(rigparts)
    

