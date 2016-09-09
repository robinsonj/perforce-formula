{% from 'p4/map.jinja' import p4 with context %}

{% for user_name, user in p4.get('users', {}).items() %}

perforce_server_{{ user.server }}_user_{{ user_name }}:
  p4user.present:
    - name:     {{ user_name }}
    - server:   {{ user.server }}

{% endfor %}
