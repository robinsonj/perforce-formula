import salt.utils

def _p4_path():
    '''
    Return the filesystem path to the p4 client binary.

    Perforce packages may install the binary to /opt/perforce/[s]bin/ and create
    a symlink from different parts of the system (/bin/, /sbin/, /usr/bin/,
    etc.).
    '''

    return salt.utils.which('p4')


def _run_p4(cmd, stdin):
    '''
    '''

    cmdstr = ' '.join([_p4_path()] + [i for i in cmd])

    return __salt__['cmd.run'](cmdstr, stdin=stdin, python_shell=False)


def run(command, port, user, stdin=None):
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

    options = []

    if port:
        options += ['--port', port]
    if user:
        options += ['--user', user]

    cmd = options + [command]

    return _run_p4(cmd, stdin)
