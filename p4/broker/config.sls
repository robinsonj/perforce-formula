{% from 'p4/map.jinja' import p4 with context %}

{% for broker_name, broker in p4.broker.get('config', {}).items() %}

perforce_broker_{{ broker_name }}_config:
  file.managed:
    - name:     {{ broker.path }}
    - user:     {{ p4.broker.config_file.user }}
    - group:    {{ p4.broker.config_file.group }}
    - mode:     {{ p4.broker.config_file.mode }}
    - source:   {{ broker.source }}
    - template: jinja
    - require:
      - pkg:    {{ p4.broker.package_base.name }}
      - user:   {{ p4.broker.config_file.user }}

{% endfor %}
