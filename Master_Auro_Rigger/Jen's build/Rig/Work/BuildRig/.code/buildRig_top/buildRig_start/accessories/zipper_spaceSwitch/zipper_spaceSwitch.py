from vtool.maya_lib import space

def main():
    
    # vars
    source_list = [ 'CNT_GROUND_1', 'CNT_BACKPACK_1_C', 'CNT_SUB_BACKPACK_1_C' ]
    
    # space orient switch
    
    cnt = 'CNT_BACKPACKZIPPER_1_L'
    ikDriver = cmds.listRelatives(cnt, p=1)[0]
    
    # space switch setup on cnt drivers
    rig = space.create_multi_follow(
            source_list,
            ikDriver,
            node=cnt,
            constraint_type='orientConstraint',
            attribute_name='followRotate',
            value=1,
            create_title=True
            )
        
    
    return