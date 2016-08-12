{% from 'p4/map.jinja' import p4 with context %}

include:
  - p4.broker.package_base

p4_broker_pkg:
  pkg.installed:
    - name:       {{ p4.broker.package.name }}
    - version:    {{ p4.broker.package.version }}
    - require:
      - pkgrepo:  p4_package_server
      - pkg:      p4_broker_base_pkg
