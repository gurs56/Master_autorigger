import maya.cmds as cmds

def create_and_parent_res_joints():
    """
    Creates new 'res' joints on top of these source nodes (lowercase),
    then parents them into a foot hierarchy:

    Source Nodes -> New Joints
    ------------------------------------------------
    JNT_foot_l  -> jnt_res_foot_l
    JNT_ball_l  -> jnt_res_ball_l
    JNT_toe_l   -> jnt_res_toe_l

    JNT_foot_r  -> jnt_res_foot_r
    JNT_ball_r  -> jnt_res_ball_r
    JNT_toe_r   -> jnt_res_toe_r

    BallYawIn_R_Loc  -> jnt_res_ballyawin_r
    Heel_R_Loc       -> jnt_res_heel_r
    BallYawOut_R_Loc -> jnt_res_ballyawout_r

    BallYawIn_L_Loc  -> jnt_res_ballyawin_l
    Heel_L_Loc       -> jnt_res_heel_l
    BallYawOut_L_Loc -> jnt_res_ballyawout_l

    Parenting Rules (for each side, l or r):
      - jnt_res_foot_<side> : top-level (no parent)
      - jnt_res_ball_<side> : child of jnt_res_foot_<side>
      - jnt_res_toe_<side>  : child of jnt_res_ball_<side>
      - jnt_res_heel_<side>, jnt_res_ballyawin_<side>, jnt_res_ballyawout_<side> : children of jnt_res_foot_<side>
    """

    # (source_node, new_joint_name)
    pairs = [
        ('JNT_foot_l',   'jnt_res_foot_l'),
        ('JNT_ball_l',   'jnt_res_ball_l'),
        ('JNT_toe_l',    'jnt_res_toe_l'),

        ('JNT_foot_r',   'jnt_res_foot_r'),
        ('JNT_ball_r',   'jnt_res_ball_r'),
        ('JNT_toe_r',    'jnt_res_toe_r'),

        ('BallYawIn_R_Loc',  'jnt_res_ballyawin_r'),
        ('Heel_R_Loc',       'jnt_res_heel_r'),
        ('BallYawOut_R_Loc', 'jnt_res_ballyawout_r'),

        ('BallYawIn_L_Loc',  'jnt_res_ballyawin_l'),
        ('Heel_L_Loc',       'jnt_res_heel_l'),
        ('BallYawOut_L_Loc', 'jnt_res_ballyawout_l'),
    ]

    for source_node, new_jnt_name in pairs:

        # 1. Ensure source node exists
        if not cmds.objExists(source_node):
            cmds.warning("Skipping '%s' - source node doesn't exist." % source_node)
            continue

        # 2. Delete if the target joint already exists
        if cmds.objExists(new_jnt_name):
            cmds.delete(new_jnt_name)

        # 3. Create the new joint
        created_jnt = cmds.createNode("joint", name=new_jnt_name)

        # 4. Match transform (pos/rot/orient)
        pos = cmds.xform(source_node, q=True, ws=True, t=True)
        rot = cmds.xform(source_node, q=True, ws=True, ro=True)
        cmds.xform(created_jnt, ws=True, t=pos)
        cmds.xform(created_jnt, ws=True, ro=rot)

        # Use a parentConstraint trick to ensure local orientation matches
        tmp_cst = cmds.parentConstraint(source_node, created_jnt, mo=False)
        cmds.delete(tmp_cst)

        # 5. Determine side (l or r)
        side_suffix = '_l' if created_jnt.endswith('_l') else '_r'

        # 6. Parent the new joint into the foot hierarchy
        # e.g. jnt_res_ball_l -> child of jnt_res_foot_l
        #      jnt_res_toe_l  -> child of jnt_res_ball_l
        #      jnt_res_heel_l -> child of jnt_res_foot_l
        #      jnt_res_ballyawin_l -> child of jnt_res_foot_l
        # etc.
        foot_jnt  = 'jnt_res_foot' + side_suffix  # e.g. jnt_res_foot_l
        ball_jnt  = 'jnt_res_ball' + side_suffix  # e.g. jnt_res_ball_l

        # If it's foot itself, leave it unparented
        if created_jnt.startswith('jnt_res_foot'):
            pass  # top-level, do nothing
        elif created_jnt.startswith('jnt_res_ball'):
            # parent ball under foot
            if cmds.objExists(foot_jnt):
                cmds.parent(created_jnt, foot_jnt)
        elif created_jnt.startswith('jnt_res_toe'):
            # parent toe under ball
            if cmds.objExists(ball_jnt):
                cmds.parent(created_jnt, ball_jnt)
        elif any(x in created_jnt for x in ['heel', 'ballyawin', 'ballyawout']):
            # parent these under foot
            if cmds.objExists(foot_jnt):
                cmds.parent(created_jnt, foot_jnt)

        print "Created '%s' and parented accordingly." % created_jnt

def main():
    create_and_parent_res_joints()

if __name__ == '__main__':
    main()
