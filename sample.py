#!/usr/bin/env python
import time
import datetime
from influxdb import InfluxDBClient

client = InfluxDBClient('127.0.0.1', 8086, 'root', 'root', 'sample')

# databaseの存在を判定し、作成前であれば新規作成
dbs = client.get_list_database()
sample_db = {'name': 'sample'}
if sample_db not in dbs:
    client.create_database('sample')

t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')

data_array = []
while True:
    with open('/sys/class/thermal/thermal_zone0/temp') as t:
        cpu_temperature = int(t.read()) / 1000

    print(f'temp {cpu_temperature}')
    # now = datetime.datetime.now(JST)
    now = datetime.datetime.now(datetime.timezone.utc)
    timestamp = now.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    print(f'{timestamp}')
    # "time": "2009-11-10T23:00:00Z",
    # インポートするjsonデータを作成
    data_array.append({
        "fields": {
            "cpu": cpu_temperature,
            "mem": 20.0,
        },
        "tags": {
            "category": "fuga",
            "machine": "web02"
        },
        "measurement": "metrics",
        "time": timestamp
    })
    # import_array = [
    # {
    #   "fields" : {
    #     "cpu" : cpu_temperature,
    #     "mem" : 20.0,
    #   },
    #   "tags" : {
    #     "category" : "fuga",
    #     "machine" : "web02"
    #   },
    #   "measurement" : "metrics"
    #   #"time" : timestamp
    # }
    # ]
    # client.write_points(import_array)
    # データ投入
    if len(data_array) > 5:
        client.write_points(data_array)
        data_array.clear()


    time.sleep(1)
