'''
Start and stop perforce services
================================

TODO: Add documentation
'''

from salt.exceptions import CommandExecutionError

def _available(name, ret):
    '''
    Check if the named perforce service is available

    name
        Service name as configured by p4dctl.conf
    '''

    available = __salt__['p4dctl.status'](name)

    if not available:
        ret['result'] = False
        ret['comment'] = 'The perforce service named {0} is not available.'.format(name)

    return available


def running(name, init_delay=None, **kwargs):
    '''
    Ensure the named perforce service is running.

    name
        Service name as configured by p4dctl.conf

    init_delay
        TODO
    '''

    ret = { 'name':     name,
            'changes':  {},
            'result':   True,
            'comment':  ''}

    # Check if the named service is available (configured in p4dctl.conf).
    try:
        if not _available(name, ret):
            return ret
    except CommandExecutionError as exc:
        ret['result']   = False
        ret['comment']  = exc.strerror
        return ret

    before_status = __salt__['p4dctl.status'](name)

    # Check if the service is already running.
    if before_status:
        ret['comment'] = 'Service {0} is already running.'.format(name)
        return ret

    # If in test mode, don't do any work.
    if __opts__['test']:
        ret['result']   = None
        ret['comment']  = 'Service {0} is set to start'.format(name)
        return ret

    # Start the service.
    service_start = __salt__['p4dctl.start'](name)

    if not service_start:
        ret['result'] = False
        ret['comment'] = 'Service {0} failed to start.'.format(name)
    else:
        ret['comment'] = 'Service {0} started.'.format(name)

    if init_delay:
        time.sleep(init_delay)
        ret['comment'] = (
                '{0}\nDelayed return for {1} seconds.'
                .format(ret['comment'], init_delay)
        )

    return ret
