{% from 'p4/map.jinja' import p4 with context %}

perforce_broker_ssl_d:
  file.directory:
    - name:     {{ p4.broker.certs.p4ssldir.get('path', '/etc/perforce/sslkeys') }}
    - user:     {{ p4.broker.certs.p4ssldir.get('user', 'root') }}
    - group:    {{ p4.broker.certs.p4ssldir.get('group', 'root') }}
    - mode:     {{ p4.broker.certs.p4ssldir.get('mode', '700') }}
    - require:
      - pkg:    {{ p4.broker.package_base.name }}

perforce_broker_sslkeys:
  p4broker.ssldir:
    - name:     {{ p4.broker.certs.p4ssldir.get('path', '/etc/perforce/sslkeys') }}
    {% if 'fingerprint' in p4.broker.certs.p4ssldir %}
    - fingerprint: {{ p4.broker.certs.p4ssldir.fingerprint }}
    {% endif %}
    - require:
      - file:   perforce_broker_ssl_d
