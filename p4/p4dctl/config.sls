{% from 'p4/map.jinja' import p4 with context %}

perforce_p4dctl_config:
  file.managed:
    - name:     {{ p4.p4dctl.config_file.path }}
    - user:     {{ p4.p4dctl.config_file.user }}
    - group:    {{ p4.p4dctl.config_file.group }}
    - mode:     {{ p4.p4dctl.config_file.mode }}
    - source:   {{ p4.p4dctl.config_file.source }}
    - template: jinja
    - require:
      - pkg:    {{ p4.p4dctl.package.name }}
      - user:   {{ p4.p4dctl.config_file.user }}

perforce_p4dctl_config_d:
  file.directory:
    - name:     {{ p4.p4dctl.config_file_d.path }}
    - user:     {{ p4.p4dctl.config_file_d.user }}
    - group:    {{ p4.p4dctl.config_file_d.group }}
    - mode:     {{ p4.p4dctl.config_file_d.mode }}
    - require:
      - file:   perforce_p4dctl_config

{% for conf_name, config in p4.p4dctl.get('config', {}).items() %}

perforce_p4dctl_{{ conf_name }}_config:
  file.managed:
    - name:     {{ p4.p4dctl.config_file_d.path }}/{{ conf_name }}.conf
    - user:     {{ p4.p4dctl.config_file.user }}
    - group:    {{ p4.p4dctl.config_file.group }}
    - mode:     {{ p4.p4dctl.config_file.mode }}
    - source:   {{ config.source }}
    - template: jinja
    - require:
      - file:   perforce_p4dctl_config_d

{% endfor %}
