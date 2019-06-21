# logging

## Installing the chart
In bash,
```
$ helm install /logging-fluentds-aws  --set elasticsearch.nfs.mountpath="<mountpath>" --set elasticsearch.nfs.server="<IP>"
```

## Introduction
This chart includes fluentd, fluentd daemonset, elasticsearch and kibana installations.

## Configuration

The following table lists the configurable parameters of the chart and their default values.
| Parameter                                 | Description                      | Default                                   |
|-------------------------------------------+----------------------------------+-------------------------------------------|
| `elasticsearch.repository`                | elastic image repository         | `` |
| `elasticsearch.image`                     | elastic  image name              | `nightly/elasticsearch`               |
| `elasticsearch.tag`                       | elastic  tag                     | `latest`                                  |
| `fluentd.repository`                      | fluentd image repository         | `` |
| `fluentd.daemonset.image`                 | fluentd daemonset image name     | `nightly/fluentd_ds`                  |
| `fluentd.daemonset.tag`                   | fluentd daemonset  tag           | `latest`                                  |
| `fluentd.aggr.image`                      | fluentd aggregator image name    | `nightly/fluentd_aggr`                |
| `fluentd.aggr.tag`                        | fluentd aggregator tag           | `latest`                                  |
|  `elasticsearch.noOfMasters`              | No of masters in elasticsearch   |  `2`
|  `elasticsearch.masterReplicas`           | No of replicas for es-master     |  `3`
|  `elasticsearch.clientReplicas`           | No of replicas for es-client     |  `2`
|  `elasticsearch.dataReplicas`             | No of replicas for es-data       |  `2`
|  `elasticserch.resources.dataCPU`         | CPU resource for es-data         |  `1`
|  `elasticserch.resources.clientCPU`       | CPU resource for es-client       |  `1`
|  `elasticserch.resources.masterCPU`       | CPU resource for es-master       |  `1`
|  `elasticserch.resources.masterMemory`    | Memory for es-master             |  `1Gi`  
|  `elasticserch.resources.clientMemory`    | Memory for es-client             |  `1Gi`
|  `elasticserch.resources.dataMemory`      | Memory for es-data               |  `1Gi`
|  `fluentd.host`                           | FLuentd hostname                 |  `fluentd`
|  `fluentd.port`                           | Fluentd port                     |  `24224`
|  `fluentd.resources.cpu`                  | CPU resource for fluentd         |  `1`
| `fluentd.resources.memory`                | Memory resource for fluentd      |  `1Gi`
| `elasticsearch.volumes.pv`                | Persistent volume                |   `ontap-nfs-elastic`
| `elasticsearch.volumes.pvc`               | Persistent volume claim          |   `ontap-nfs-elastic-claim`
| `elasticsearch.volumes.capacity`          | Volume capacity                  |   `50Gi`
| `elasticsearch.nfs.mountPath`             | Nfs mount path                   |   `/ab_elastic`
| `elasticsearch.volumes.server`            | Ontap vserver IP                 |   `10.193.78.90` 
   
  
                      
