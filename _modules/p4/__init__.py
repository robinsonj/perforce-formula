
def run(command, port, user):
    '''
    Run p4 client commands against the target server.
    '''

    p4_path = 'p4'
    options = '-p {0} -u {1}'.format(port, user)
    cmd     = '{0} {1} {2}'.format(p4_path, options, command)

    return __salt__['cmd.run'](cmd, python_shell=False)
