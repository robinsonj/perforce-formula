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


def running(name, sig=None, init_delay=None, **kwargs):
    '''
    Ensure the named perforce service is running.

    name
        Service name as configured by p4dctl.conf

    sig
        TODO

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

    # If in test mode, don't do any work.
    if __opts__['test']:
        ret['result']   = None
        ret['comment']  = 'Service {0} is set to start'.format(name)
        return ret

    return ret
