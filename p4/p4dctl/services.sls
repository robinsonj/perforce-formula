{% from 'p4/map.jinja' import p4 with context %}

{% for service in p4.p4dctl.get('services', {}).get('running', []) %}

perforce_p4dctl_{{ service }}_service:
  p4dctl.running:
    - name:     {{ service }}
    - require:
      {% for conf_name, _ in p4.p4dctl.get('config', {}).items() %}
      - file: perforce_p4dctl_{{ conf_name }}_config
      {% endfor %}

{% endfor %}
