{% from 'p4/map.jinja' import p4 with context %}

include:
  - p4.server.package_base

p4_server_pkg:
  pkg.installed:
    - name:       {{ p4.server.package.name }}
    - version:    {{ p4.server.package.version }}
    - require:
      - pkgrepo:  p4_package_server
      - pkg:      p4_server_base_pkg
