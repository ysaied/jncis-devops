Provision interface configs:
  junos.install_config:
   - name: salt:///configs/interfaces.conf
   - diffs_file: /home/lab/interfaces-{{grains.id}}.diff

