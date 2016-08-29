def p4dctl(name, action, show_output=False):
    p4dctl_path = '/sbin/p4dctl'
    cmd         = '{0} {1} {2}'.format(p4dctl_path, action, name)

    if show_output:
        return __salt__['cmd.run'](cmd, python_shell=False)
    else:
        return not __salt__['cmd.retcode'](cmd, python_shell=False)


def run(name, action):
    '''
    Run p4dctl with the specified service name and action.

    name
        Service name as configured by p4dctl.conf

    action
        Action name. Can be: start, stop, restart, status.

    CLI Example:

    .. code-block:: bash

        salt '*' p4dctl.run p4d restart
        salt '*' p4dctl.run p4broker status
    '''

    return p4dctl(name, action)


def status(name):
    '''
    Return the status of a perforce service managed by p4dctl.

    name
        Service name as configured by p4dctl.conf.

    CLI Example:

    .. code-block:: bash

        salt '*' p4dctl.status <service name>
    '''

    return __salt__['p4dctl.run'](name, 'status')


def start(name):
    '''
    Return the start result of a perforce service managed by p4dctl.

    name
        Service name as configured by p4dctl.conf.

    CLI Example:

    .. code-block:: bash

        salt '*' p4dctl.start <service name>
    '''

    return __salt__['p4dctl.run'](name, 'start')


def stop(name):
    '''
    Return the stop result of a perforce service managed by p4dctl.

    name
        Service name as configured by p4dctl.conf.

    CLI Example:

    .. code-block:: bash

        salt '*' p4dctl.stop <service name>
    '''

    return __salt__['p4dctl.run'](name, 'stop')


def restart(name):
    '''
    Return the restart result of a perforce service managed by p4dctl.

    name
        Service name as configured by p4dctl.conf.

    CLI Example:

    .. code-block:: bash

        salt '*' p4dctl.restart <service name>
    '''

    return __salt__['p4dctl.run'](name, 'restart')

def list(name=None):
    '''
    List the perforce services managed by p4dctl.

    If no name is passed, list all managed services.

    name
        Service name as configured by p4dctl.conf.

    CLI Example:

    .. code-block:: bash

        salt '*' p4dctl.list
        salt '*' p4dctl.list p4d-server
    '''

    return p4dctl(name, 'list', True)
