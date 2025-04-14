
def main():
    
    # create top grps for asset
    
    allGrp = cmds.group( em = 1 , n = process.get_option( 'all Grp' , group = 'Groups' ))
    assetGrp = cmds.group( em = 1 , n = process.get_option( 'asset Grp' , group = 'Groups' ), p = allGrp )
    
    return