{% from 'p4/map.jinja' import p4 with context %}

p4python_package:
  pip.installed:
    - name:       p4python
    - upgrade:    True
    - require:
      - pkg:      python-pip
{% for type, name in p4.p4python.require.items() %}
      - {{ type }}: {{ name }}
{% endfor %}

python_dep_packages:
  pkg.installed:
    - names:
      - python-pip
      - {{ p4.p4python.require.pkg }}
