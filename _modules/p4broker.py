from __future__ import absolute_import

import re
import os

# Import salt libs.
import salt.utils

def _p4broker(opts, env=None):
    '''
    '''

    p4broker = salt.utils.which('p4broker')

    if p4broker == None and "/opt/perforce/sbin" not in os.environ["PATH"]:
        os.environ["PATH"] += os.pathsep + "/opt/perforce/sbin"
        p4broker = salt.utils.which('p4broker')

    cmd = '{0} {1}'.format(p4broker, opts)

    return __salt__['cmd.run'](cmd, python_shell=False, env=env)


def run(opts, ssldir):
    '''
    '''

    env = [ { 'P4SSLDIR': ssldir } ]

    return _p4broker(opts, env)


def ssldir_fingerprint(ssldir, fingerprint=None):
    '''
    '''

    exists = False

    out = run('-Gf', ssldir)
    reg = re.compile('^Fingerprint:.*')

    if reg.match(out):
        exists = True

    return (exists, out)

def ssldir_create(ssldir):
    '''
    '''

    run('-Gc', ssldir)

    return ssldir_fingerprint(ssldir)
