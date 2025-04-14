
import maya.cmds as cmds

# Cleanup previous work (optional)
cmds.select(all=True)
cmds.delete()

# Create joints for the foot
ankleJoint = cmds.joint(name="ankle_JNT")
ballJoint = cmds.joint(name="ball_JNT", position=(0, 0, 5))
toeJoint = cmds.joint(name="toe_JNT", position=(0, 0, 10))

# Add IK handles for ankle and ball
ikHandleAnkle = cmds.ikHandle(
    name="ankle_IK",
    startJoint=ankleJoint,
    endEffector=ballJoint,
    solver="ikSCsolver"
)[0]

ikHandleBall = cmds.ikHandle(
    name="ball_IK",
    startJoint=ballJoint,
    endEffector=toeJoint,
    solver="ikSCsolver"
)[0]

# Create control curves
mainCtrl = cmds.circle(name="foot_CTRL", radius=3)[0]
heelCtrl = cmds.circle(name="heel_CTRL", radius=1.5)[0]
toeCtrl = cmds.circle(name="toe_CTRL", radius=1.5)[0]

# Position controls
cmds.xform(heelCtrl, t=(0, 0, -2))  # Place behind ankle
cmds.xform(toeCtrl, t=(0, 0, 12))   # Place at toe

# Group controls under main control
cmds.parent(heelCtrl, toeCtrl, mainCtrl)

# Create reverse foot setup (critical for rig behavior)
revHeel = cmds.group(empty=True, name="reverseHeel_GRP")
revBall = cmds.group(empty=True, name="reverseBall_GRP")
revToe = cmds.group(empty=True, name="reverseToe_GRP")

# Position reverse groups
cmds.xform(revHeel, t=cmds.xform(ankleJoint, q=True, t=True, ws=True))
cmds.xform(revBall, t=cmds.xform(ballJoint, q=True, t=True, ws=True))
cmds.xform(revToe, t=cmds.xform(toeJoint, q=True, t=True, ws=True))

# Parent reverse groups under main control
cmds.parent(revHeel, revBall, revToe, mainCtrl)

# Constrain IK handles to reverse foot groups
cmds.pointConstraint(revHeel, ikHandleAnkle)
cmds.pointConstraint(revBall, ikHandleBall)

# Add custom attributes to main control
cmds.addAttr(mainCtrl, ln="HeelLift", min=0, max=10, dv=0, k=True)
cmds.addAttr(mainCtrl, ln="ToeLift", min=0, max=10, dv=0, k=True)
cmds.addAttr(mainCtrl, ln="FootRoll", min=-10, max=10, dv=0, k=True)

# Connect attributes to drive rotations (set driven keys)
# Heel lift
cmds.setDrivenKeyframe(
    revHeel + ".rotateX",
    cd=mainCtrl + ".HeelLift",
    driverValue=0,
    value=0
)
cmds.setDrivenKeyframe(
    revHeel + ".rotateX",
    cd=mainCtrl + ".HeelLift",
    driverValue=10,
    value=30
)

# Toe lift
cmds.setDrivenKeyframe(
    revToe + ".rotateX",
    cd=mainCtrl + ".ToeLift",
    driverValue=0,
    value=0
)
cmds.setDrivenKeyframe(
    revToe + ".rotateX",
    cd=mainCtrl + ".ToeLift",
    driverValue=10,
    value=-30
)

# Foot roll (side-to-side)
cmds.connectAttr(
    mainCtrl + ".FootRoll",
    revBall + ".rotateZ"
)

# Cleanup: Lock unused attributes
for ctrl in [mainCtrl, heelCtrl, toeCtrl]:
    for attr in ["tx", "ty", "tz", "rx", "ry", "rz", "sx", "sy", "sz", "v"]:
        cmds.setAttr(ctrl + "." + attr, lock=True, keyable=False)

cmds.select(clear=True)
print("Foot rig created!")