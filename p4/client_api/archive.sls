{% from 'p4/map.jinja' import p4 with context %}

{% set capi = p4.client_api %}

p4_client_api_archive:
  archive.extracted:
    - name:         {{ capi.archive.path }}
    - user:         {{ capi.install.user }}
    - group:        {{ capi.install.group }}
    - source:       {{ capi.archive.host ~ capi.archive.version ~ '/' ~ 'bin.linux26x86_64' ~ '/p4api.tgz' }}
    - source_hash:  {{ capi.archive.source_hash }}
    - if_missing:   {{ capi.install.path ~ '/p4api' }}
    - require_in:
      - file:       p4_client_api_archive_symlink

p4_client_api_archive_symlink:
  file.symlink:
    - name:         {{ capi.install.path ~ '/p4api' }}
    - target:       {{ capi.archive.path ~ '/' ~ capi.archive.build }}
