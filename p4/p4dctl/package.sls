{% from 'p4/map.jinja' import p4 with context %}

include:
  - p4.pkgrepo

p4_p4dctl_pkg:
  pkg.installed:
    - name:       {{ p4.p4dctl.package.name }}
    - version:    {{ p4.p4dctl.package.version }}
    - require:
      - pkgrepo:  p4_package_server
