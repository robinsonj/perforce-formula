{% from 'p4/map.jinja' import p4 with context %}

include:
  - p4.pkgrepo

p4_broker_base_pkg:
  pkg.installed:
    - name:       {{ p4.broker.package_base.name }}
    - version:    {{ p4.broker.package_base.version }}
    - require:
      - pkgrepo:  p4_package_server
