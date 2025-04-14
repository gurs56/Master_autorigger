from vtool.maya_lib import space

def main():
    
    # vars
    sides = ['l', 'r']
    #source_list = [ 'CNT_SUB_GROUND_2', 'CNT_SUB_COG_C', 'CNT_SUB_HIPS_C' ]
    source_list = [ 'CNT_SUB_HIPS_C' , 'CNT_SUB_COG_C', 'CNT_SUB_GROUND_2' ]
    
    # space switches
    
    for side in sides:
        
        cnt = 'CNT_FK_THIGH_1_%s' % side.upper()
        fkDriver = cmds.listRelatives(cnt, p=1)[0]
        
        # space switch setup on cnt drivers
        rig = space.create_multi_follow(
                source_list,
                fkDriver,
                node=cnt,
                constraint_type='orientConstraint',
                attribute_name='followRotate',
                value=0,
                create_title=True
                )
        
    
    return