{% from 'p4/map.jinja' import p4 with context %}

include:
{% if p4.server.base_install %}
  - p4.server.package_base
{% else %}
  - p4.server.package
{% endif %}
  - p4.server.license
