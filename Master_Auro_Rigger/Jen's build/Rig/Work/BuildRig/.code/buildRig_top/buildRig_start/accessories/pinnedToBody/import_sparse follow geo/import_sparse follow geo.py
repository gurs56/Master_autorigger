
def main():
    
    setupGrp = process.get_option( 'setup Grp' , group = 'Groups' )
    
    process.import_data('sparse follow geo')
    cmds.parent('sparse_setup', setupGrp)