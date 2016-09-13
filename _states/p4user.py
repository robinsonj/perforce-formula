'''
Manage perforce user configuration
==================================

TODO: Add documentation.
'''

from __future__ import absolute_import

import logging

log = logging.getLogger(__name__)

def present(name,
            user_type='standard',
            server='localhost:1666',
            super_user='super',
            super_pass='perforce'
            ):
    '''
    Ensure that the named user is present in the target server with the
    specified properties.

    name
        Name of the user to manage.

    user_type
        Perforce spec type of the user. Can be 'standard,' 'service,' or
        'operator.' Value is not checked for validity. Defaults to 'standard.'

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

    info = __salt__['p4.run'](server, super_user, 'users', name)

    log.info('User info in server {0}: {1}'.format(server, info))

    if info[0]:
        # User already exists.
        log.info('Perforce user {0} already exists.'.format(name))
        log.debug('Perforce user {0} info: {1}'.format(name, info))

        ret['comment'] = 'Perforce user "{0}" is present and up to date.'.format(name)
    else:
        # User needs to be created.
        form_spec   = __salt__['p4.run'](server, super_user, 'user', '-o').pop(0)
        log.debug('User form: {0}'.format(form_spec))
        form_spec['User'] = name
        form_spec['Type'] = user_type
        form_spec['FullName'] = name
        log.debug('User form input: {0}'.format(form_spec))
        create_ret  = __salt__['p4.run'](server, super_user, 'user', '-fi', cmd_input=form_spec)
        log.info('User create output: {0}'.format(create_ret))

        ret['changes'][name] = 'Created'
        ret['changes']['output'] = create_ret
        ret['comment'] = 'Perforce user "{0}" created.'.format(name)

    return ret
