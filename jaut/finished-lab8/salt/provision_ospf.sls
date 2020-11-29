Provision OSPF:
  junos.install_config:
   - name: salt:///configs/ospf.conf
   - diffs_file: /home/lab/ospf-{{grains.id}}.diff
