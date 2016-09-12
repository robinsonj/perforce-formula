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

    p4 = P4()

    p4.port = port
    p4.user = user

    try:
        p4.connect()
        result = p4.run(command)
    except P4Exception as p4err:
        log.error(p4err)
        result = False
    finally:
        p4.disconnect()

    return result
