from vtool.maya_lib import space

def main():
    
    # vars
    sides = ['l', 'r']
    source_list = [ 'CNT_SUB_GROUND_2', 'CNT_SUB_COG_C', 'CNT_SUB_SPINE_3_C' ]
    
    # space switches
    
    for side in sides:
        
        cnt = 'CNT_IK_ARM_BTM_1_%s' % side.upper()
        ikDriver = cmds.listRelatives(cnt, p=1)[0]
        
        source_list.append(
                'CNT_CLAVICLE_1_%s' % side.upper() 
                )
                
        # space switch setup on cnt drivers
        rig = space.create_multi_follow(
                source_list,
                ikDriver,
                node=cnt,
                constraint_type='parentConstraint',
                attribute_name='follow',
                value=0,
                create_title=True
                )
        
    
    return