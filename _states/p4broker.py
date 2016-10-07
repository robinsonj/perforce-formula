'''
Manage perforce broker SSL certificates
=======================================

TODO: Add documentation.
'''

from __future__ import absolute_import

def ssldir(name,
           fingerprint=None,
           user='root'):
    '''
    Ensure that the named directory is appropriately configured to have an SSl
    certificate and key for a Perforce broker.

    name
        Name of the directory containing the certificate.txt and privatekey.txt
        files.

    fingerprint
        Fingerprint used to verify the certificate.

    user
        User that will own the directory.
    '''

    ret = { 'name':     name,
            'changes':  {},
            'result':   True,
            'comment':  ''}

    current_fingerprint = __salt__['p4broker.ssldir_fingerprint'](name, fingerprint)

    if current_fingerprint[0]:
        ret['comment'] = '{0} is in the correct state'.format(name)
    else:
        new_fingerprint = __salt__['p4broker.ssldir_create'](name, user)
        ret['changes']['output'] = new_fingerprint[1]
        ret['comment'] = 'P4SSLDIR {0} created'.format(name)

    return ret
