{% from 'p4/map.jinja' import p4 with context %}

include:
{% if p4.client.base_install %}
  - p4.client.package_base
{% else %}
  - p4.client.package
{% endif %}
