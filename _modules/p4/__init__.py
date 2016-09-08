
def run(command, port, user):
    '''
    Run p4 client commands against the target server.

    command
        Perforce command and arguments to be executed.

    port
        address:port to be connected to.

    user
        Perforce user to execute commands.

    CLI Example:

    .. code-block:: bash

        salt '*' p4.run 'users -l' localhost:1666 perforce
    '''

    p4_path = 'p4'
    options = '-p {0} -u {1}'.format(port, user)
    cmd     = '{0} {1} {2}'.format(p4_path, options, command)

    return __salt__['cmd.run'](cmd, python_shell=False)
