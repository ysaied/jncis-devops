Provision DNS:
  junos.install_config:
   - name: salt:///configs/dns.conf
   - diffs_file: /home/lab/dns-{{grains.id}}.diff
