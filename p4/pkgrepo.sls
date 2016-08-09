{% from 'p4/map.jinja' import p4 with context %}

p4_package_server:
  pkgrepo.managed:
    - humanname:  {{ p4.pkgrepo.humanname }}
    - name:       {{ p4.pkgrepo.name }}
    - dist:       {{ p4.pkgrepo.dist }}
    - file:       {{ p4.pkgrepo.file }}
    - key_url:    {{ p4.pkgrepo.key_url }}
