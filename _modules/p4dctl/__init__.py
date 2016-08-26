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

    cmd = ('/sbin/p4dctl {0} {1}').format(action, name)

    return not __salt__['cmd.run'](cmd, python_shell=False)


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
