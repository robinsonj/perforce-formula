{% from 'p4/map.jinja' import p4 with context %}

include:
{% if p4.broker.base_install %}
  - p4.broker.package_base
{% else %}
  - p4.broker.package
{% endif %}
  - p4.broker.config
