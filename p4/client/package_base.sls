{% from 'p4/map.jinja' import p4 with context %}

include:
  - p4.pkgrepo

p4_cli_base_pkg:
  pkg.installed:
    - name:       {{ p4.client.package.name }}
    - version:    {{ p4.client.package.version }}
    - require:
      - pkgrepo:  p4_package_server
