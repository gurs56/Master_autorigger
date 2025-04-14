
def main():
    
    # vars
    
    structureGrp = process.get_option( 'structure Grp' , group = 'Groups' )
    
    # import structure and parent to top grp
    
    cmds.parent( process.import_data('skeletal mesh') , structureGrp )
    
    return