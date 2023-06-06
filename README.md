# grafana login
- user, password: admin

# set grafana influxdb data resource
- URL: http://influxdb:8086
- Database: sample
- user: root
- passwod: root
sample.py実行後、save&test

# dependencies:
- pip install influxdb
- pip install Flask==2.1.0
- pip install Flask-Cors
- sudo apt install python3-flask


# telegraf
- edit /etc/telegraf/telegraf.conf,
- systemctl start telegraf
