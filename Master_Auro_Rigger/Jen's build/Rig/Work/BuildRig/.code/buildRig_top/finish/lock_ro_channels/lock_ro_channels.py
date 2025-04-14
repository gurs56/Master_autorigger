
def main():
    
    ro_attributes = cmds.ls('CNT_*.rotateOrder')
    for attr in ro_attributes:
        cmds.setAttr( attr , k=0, cb=1, l=1)
        if attr.find('_GEAR_') != -1:
            cmds.setAttr( attr, cb=0)
    return