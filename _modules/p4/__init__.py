from __future__ import absolute_import

import salt.utils
import logging

log = logging.getLogger(__name__)

try:
    from P4 import P4,P4Exception
    HAS_P4PYTHON = True
except ImportError:
    HAS_P4PYTHON = False
    log.error('P4 module could not import p4python.')

__virtualname__ = 'p4'

def __virtual__():
    '''
    Set the module name. Returns an error if p4python is unavailable.
    '''

    if HAS_P4PYTHON:
        return __virtualname__

    return (False, 'p4 execution module not loaded. "p4python" library could not be imported.')


def run(port, user, command, args=[], cmd_input=None):
    '''
    Run p4 client commands against the target server.

    port
        address:port to be connected to.

    user
        Perforce user to execute commands.

    command
        Perforce command and arguments to be executed.

    args
        Arguments to the command specified by <command>.

    cmd_input
        STDIN for the specified command. Usually a completed form, etc.

    CLI Example:

    .. code-block:: bash

        salt '*' p4.run users '-l' localhost:1666 perforce
    '''

    p4 = P4()

    p4.port = port
    p4.user = user

    try:
        p4.connect()
        p4.input = cmd_input

        log.info('Running command: {0} {1}'.format(command, args))
        log.info('Command input: {0}'.format(cmd_input))

        result = p4.run(command, args)
    except P4Exception as p4err:
        log.error('Caught P4 error: {0}'.format(p4err))

        for e in p4.errors:
            log.error(e)

        result = (False, p4.errors)
    finally:
        p4.disconnect()

    return result
