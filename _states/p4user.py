'''
Manage perforce user configuration
==================================

TODO: Add documentation.
'''

from __future__ import absolute_import

import logging

log = logging.getLogger(__name__)

def present(name,
            type='standard',
            server='localhost:1666',
            super_user='super',
            super_pass='perforce'
            ):
    '''
    Ensure that the named user is present in the target server with the
    specified properties.

    name
        Name of the user to manage.

    server
        Perforce server to connect to.

    super_user
        User to perform actions as ('-u' from the p4 client). Must have super
        priveledges.

    super_pass
        Password for super_user.
    '''

    ret = { 'name':     name,
            'changes':  {},
            'result':   True,
            'comment':  ''}

    info = __salt__['p4.run']('users {0}'.format(name), server, super_user)

    log.info('User info in server {0}: {1}'.format(server, info))

    if '- no such user(s)' in info:
        # User needs to be created.
        form_spec   = __salt__['p4.run']('user -o {0}'.format(name), server, super_user)
        create_ret  = __salt__['p4.run']('user -fi', server, super_user, stdin=form_spec)
        log.info('User create output: {0}'.format(create_ret))

        ret['changes'][name] = 'Created'
        ret['changes']['output'] = create_ret
        ret['comment'] = 'Perforce user "{0}" created.'.format(name)
    else:
        # User already exists.
        log.info('Perforce user {0} already exists.'.format(name))
        ret['comment'] = 'Perforce user "{0}" is present and up to date.'.format(name)

    return ret
