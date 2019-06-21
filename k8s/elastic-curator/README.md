# elastic-curator

## Installing the chart
```bash
$ helm install elastic-curator --set elasticsearch.host="hostname" --set elasticsearch.port="port"
```

## Introduction
This chart creates elastic-curator for index management in elastic search. 
This will make the index rollover after specified time (default- 60days ). 
It runs a cron job once in a month to check the the index update the index rollovers. 
0 23 28 1-12 *  --> cron expression currently used. 

## Configuration

The following table lists the configurable parameters of the  chart and their default values.
| Parameter                                 | Description                      | Default                                   |
|-------------------------------------------+----------------------------------+-------------------------------------------|
| `curator.repository`                | curator image repository         | `` |
| `curator.image`                     | curator  image name              | ``                        |
| `curator.tag`                       | curator  tag                     | `latest`                                  |
| `elasticsearch.host`                | elastic host name                | `elasticsearch` |
| `elasticsearch.port`                | elastic port                     | `9200`                         |
| `curator.max_age`                   | maximum age for an index         | `30d`                                  |
| `curator.max_size`                  | maximum size for an index        | `25gb`                                  |
