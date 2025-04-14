
def main():
    
    # vars
    
    modelGrp = process.get_option( 'model Grp' , group = 'Groups' )
    
    # import model and parent to top grp
    
    cmds.parent( process.import_data( 'model' ) , modelGrp )
    
    
    return