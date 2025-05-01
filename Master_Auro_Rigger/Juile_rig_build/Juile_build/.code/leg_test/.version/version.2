# IK/FK LEG + FOOT RIG (PYTHON 2) FOR YOUR AUTO RIGGER
# Based on joint names and structure in https://github.com/gurs56/Master_autorigger.git

import maya.cmds as cmds

#-------------------------#
# UTILS
#-------------------------#
def duplicate_chain(joint_list, suffix):
    new_chain = []
    for jnt in joint_list:
        new_name = jnt.replace('JNT_', 'JNT_' + suffix + '_')
        new_jnt = cmds.duplicate(jnt, po=True, n=new_name)[0]
        new_chain.append(new_jnt)
    for i in range(1, len(new_chain)):
        cmds.parent(new_chain[i], new_chain[i-1])
    return new_chain

#-------------------------#
# BUILD JOINT CHAINS
#-------------------------#
def build_leg_chains():
    base_joints = ['JNT_thigh_l', 'JNT_calf_l', 'JNT_foot_l']
    fk_chain = duplicate_chain(base_joints, 'FK')
    ik_chain = duplicate_chain(base_joints, 'IK')
    return base_joints, fk_chain, ik_chain

#-------------------------#
# FK CONTROLS
#-------------------------#
def create_fk_controls(fk_chain):
    controls = []
    for jnt in fk_chain:
        ctrl_name = jnt.replace('JNT_', 'CNT_')
        ctrl = cmds.circle(nr=(1,0,0), r=2, n=ctrl_name)[0]
        grp = cmds.group(ctrl, n=ctrl + '_GRP')
        pos = cmds.xform(jnt, q=True, ws=True, t=True)
        cmds.xform(grp, ws=True, t=pos)
        cmds.orientConstraint(ctrl, jnt)
        controls.append(ctrl)
    for i in range(1, len(controls)):
        cmds.parent(controls[i] + '_GRP', controls[i-1])
    return controls

#-------------------------#
# IK RIG
#-------------------------#
def create_ik_controls(ik_chain):
    ik_ctrl = cmds.circle(nr=(0,1,0), r=3, n='CNT_IK_FOOT_l')[0]
    grp = cmds.group(ik_ctrl, n='CNT_IK_FOOT_l_GRP')
    foot_pos = cmds.xform(ik_chain[2], q=True, ws=True, t=True)
    cmds.xform(grp, ws=True, t=foot_pos)
    
    pole_vector = cmds.spaceLocator(n='CNT_LEG_POLE_VECTOR_l')[0]
    thigh_pos = cmds.xform(ik_chain[0], q=True, ws=True, t=True)
    calf_pos = cmds.xform(ik_chain[1], q=True, ws=True, t=True)
    pv_pos = [(thigh_pos[0]+calf_pos[0])/2, (thigh_pos[1]+calf_pos[1])/2, (thigh_pos[2]+calf_pos[2])/2 - 10]
    cmds.xform(pole_vector, ws=True, t=pv_pos)
    
    ik_handle = cmds.ikHandle(n='IKHANDLE_leg_l', sj=ik_chain[0], ee=ik_chain[2], sol='ikRPsolver')[0]
    cmds.parent(ik_handle, ik_ctrl)
    cmds.poleVectorConstraint(pole_vector, ik_handle)
    return ik_ctrl, pole_vector

#-------------------------#
# IK/FK SWITCH SETUP
#-------------------------#
def create_ik_fk_switch(base_joints, fk_chain, ik_chain):
    for i in range(len(base_joints)):
        cmds.parentConstraint(fk_chain[i], base_joints[i], mo=False, w=1)
        cmds.parentConstraint(ik_chain[i], base_joints[i], mo=False, w=0)

#-------------------------#
# FOOT PIVOT (BAREBONES)
#-------------------------#
def build_foot_roll():
    # Simplified version, replace this with actual pivot setup if needed
    print('Build custom foot roll here using grouped pivot hierarchy')

#-------------------------#
# MAIN
#-------------------------#
def rig_leg_system():
    base_joints, fk_chain, ik_chain = build_leg_chains()
    create_fk_controls(fk_chain)
    create_ik_controls(ik_chain)
    create_ik_fk_switch(base_joints, fk_chain, ik_chain)
    build_foot_roll()

rig_leg_system()

