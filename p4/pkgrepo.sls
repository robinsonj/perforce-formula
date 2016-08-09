{% from 'p4/map.jinja' import p4 with context %}

p4_package_server:
  pkgrepo:
    - managed
    - humanname:  {{ p4.pkgrepo.humanname }}
    - name:       {{ p4.pkgrepo.name }}
{% if grains.os_family == 'Debian' %}
    - dist:       {{ p4.pkgrepo.dist }}
    - file:       {{ p4.pkgrepo.file }}
    - key_url:    {{ p4.pkgrepo.key_url }}
{% elif grains.os_family == 'RedHat' %}
    - baseurl:    {{ p4.pkgrepo.baseurl }}
    - gpgkey:     {{ p4.pkgrepo.gpgkey }}
    - gpgcheck:   {{ p4.pkgrepo.gpgcheck }}
{% endif %}
