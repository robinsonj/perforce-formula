from __future__ import absolute_import

import re
import os

# Import salt libs.
import salt.utils

def _p4broker(opts, runas='root', env=None):
    '''
    '''

    p4broker = salt.utils.which('p4broker')

    if p4broker == None and "/opt/perforce/sbin" not in os.environ["PATH"]:
        os.environ["PATH"] += os.pathsep + "/opt/perforce/sbin"
        p4broker = salt.utils.which('p4broker')

    cmd = '{0} {1}'.format(p4broker, opts)

    return __salt__['cmd.run'](cmd, python_shell=False, env=env, runas=runas)


def run(opts, ssldir, user='root'):
    '''
    '''

    env = [ { 'P4SSLDIR': ssldir } ]

    return _p4broker(opts, user, env)


def ssldir_fingerprint(ssldir, user, fingerprint=None):
    '''
    '''

    exists = False

    out = run('-Gf', ssldir, user)
    reg = re.compile('^Fingerprint:.*')

    if reg.match(out):
        exists = True

    return (exists, out)

def ssldir_create(ssldir, user):
    '''
    '''

    run('-Gc', ssldir, user)

    return ssldir_fingerprint(ssldir, user)
