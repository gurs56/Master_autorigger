
def main():
    
    # vars
    
    assetGrp =  process.get_option( 'asset Grp' , group = 'Groups' )
    
    # create model top grp
    
    modelGrp = cmds.group( em = 1, n = process.get_option( 'model Grp' , group = 'Groups' ) , p = assetGrp )
    
    return