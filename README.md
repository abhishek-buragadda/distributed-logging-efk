# Distributed-logging-efk
This gives the files to create a distributed logging framework using ElasticSearch, Fluentd and Kibana.

# Brief Introduction to Services used:
**Fluentd:**

Fluentd is an open source and multi-platform Log Aggregator and Forwarder which allows you to collect data/logs from different sources, unify and send them to multiple destinations. It's fully compatible with Docker and Kubernetes environments.

**ElasticSearch:**

•	Elasticsearch is a distributed RESTful search engine built for the cloud
•	Elasticsearch is a distributed document store. It can store and retrieve complex data structures—serialized as JSON documents—in real time. In other words, as soon as a document has been stored in Elasticsearch, it can be retrieved from any node in the cluster.

•	Elasticsearch is a search engine which provides a distributed, multitenant-capable full-text search engine with an HTTPweb interface and schema-free JSON documents.

•	In Elasticsearch, all data in every field is indexed by default. That is, every field has a dedicated inverted index for fast retrieval.

•	Elasticsearch is distributed, which means that indices can be divided into shards and each shard can have zero or more replicas. Each node hosts one or more shards, and acts as a coordinator to delegate operations to the correct shard(s). Rebalancing and routing are done automatically".

**Kibana:**

•	Kibana is an open source analytics and visualization platform designed to work with Elasticsearch. We can use Kibana to search, view, and interact with data stored in Elasticsearch indices. We can easily perform advanced data analysis and visualize our data in a variety of charts, tables, and maps.
•	Kibana makes it easy to understand large volumes of data. Its simple, browser-based interface enables you to quickly create and share dynamic dashboards that display changes to Elasticsearch queries in real time.

**Elasticsearch Curator:**

Elasticsearch Curator helps you curate, or manage, your Elasticsearch indices and snapshots by:
1.	Obtaining the full list of indices (or snapshots) from the cluster, as the actionable list
2.	Iterate through a list of user-defined filters to progressively remove indices (or snapshots) from this actionable list as needed.
3.	Perform various actions on the items which remain in the actionable list.

# Comparisons
These are the different products which are considered while investigation. The products are chosen based on the usability, performance need and more specifically how it caters the our requirements.

# Cluster Deployment:

**Fluentd forwarder:**

•	Fluentd is used a forwarder. This is responsible for sending log messages from the container log file to the log forwarder as configured.
 
•	In this role, fluentd is action as a daemonset which collect the logs from the monitored pod log files.

•	The docker engine is configured to log messages. So all the containers will log their messages in the /var/log/container folder with name as
  <container-name>-<random-hash>.log  file.
  
•	Fluentd will read those logs from these  files and forward it to the fluentd-aggregator.

•	Log forwarder is configured with a kubernetes plugin which adds the kubernetes-metadata to the log.

•	Local file buffer is implemented in case the fluentd-aggregator is down or not accepting logs. Meanwhile all the logs will be collected in the local file buffer.

**Fluentd Aggregator:**

•	In this role, fluentd is acting as a log aggregator which collect the logs from fluentd daemonset and forwards it to elasticsearch.

•	Buffer is implemented in case the elasticsearch cluster is down or not accepting logs. Meanwhile all the logs will be collected in the buffer. In case of on-premise setup in-memory buffer is allocated. However in case of production setup AWS EBS volume is attached.

**Elasticsearch**

•	 ElasticSearch cluster installation involves installation of 
1. **Elasticsearch client** 

	Client role is to accept the connection to the elastic search(GET/POST) and perform the operations with the help es-data. 
2. **Elasticsearch master**
	
	master manages the client and data replicas 
3. **Elasticsearch data** 
	
	data is responsible for the storage. Currently this is configured to use an Ontap Volume. It stores all the logs in that ontap volume. The volume is mount based via Persistent Volume and Persistent Volume Claim. (PV and PVC). 

	
	 The installation of elastic is HA in our Helm chart. This means there are multiple replicas of each of the pods(master, client ,data)

	 The default setup has 3 master , 2 client , 2 data pods and this can be configured in any way possible based on the number of nodes we want this setup.We can add/remove nodes   dynamically if we want to .

	 The reason to have 3 master instead of two  → https://blog.trifork.com/2013/10/24/how-to-avoid-the-split-brain-problem-in-elasticsearch/

	 In the HA setup, each of the elastic data, client and master pods are allocated on different nodes .  This means  no two master pods are in the same node.(same is the case with data, client).  So if any of the node is down, the cluster still works as usual .

**Elasticsearch Curator:**

•	Elastic curator helps in index management of elastic search. In this helm chart curator creates initial indices and alias-es for each of indices. So each each alias will point to an index that is created initially. 

Index pattern for the indices.

    "<indexName-{now{yyyy-MM-dd't'HH.mm.ss}}>"
 
For example below:

    api -- api-2018-12-10t10.07.19
    billing – billing-2018-12-10t10.07.19
    lrse -- lrse-2018-12-10t10.07.19
    lrsemetrics -- lrsemetrics-2018-09-000001

•	**max_age, max_size**: The user can configure max-age or max_size for a particular index, after this time the index gets rollover by curator. Please note that the index rollover will happens with whichever condition (either max_age or max_size) occurs first.

•	**schedule**: To configure the schedule for running the curator job.

•	**retentionUnit, retentionCount:** User can also configure the retention time of an index. If a particular index is past the retention time then that index is deleted by the curator. 

•	**closeIndexUnit, closeIndexCount:** Configure this paramter to close the index. A closed index has almost no overhead on the cluster (except for maintaining its metadata), and is blocked for read/write operations.

•	Curator helm chart installation creates a k8s cron job which can be run based on the user configuration . This job is responsible for different action on index like the index rotation, closing, deletion.

•	What happens when an index is rotated  →   Newer indices are created and the alias-es now point to the newer index.

    lrsemetrics -- lrsemetrics-2018-09-000002
    api -- 2018-09-000002
    billing -- 2018-09-000002
    lrse -- lrse-2018-09-000002
    sched -- sched-2018-09-000002
    rabbitmq. -- rabbitmq-2018-09-000002
    mariadb -- mariadb-2018-09-000002
    lrsemetrics -- lrsemetrics-2018-09-000002

# Installation: 
Installations Requirements:

We have 2 different ways of deploying logging .
 
    ElasticSearch HA mode 
        CPU - 5.5
        RAM - 5GB

    ElasticSearch Non-HA mode  
        CPU - 4
        RAM - 3.5GB

**Installing Logging Helm Chart:**

•	Install logging-fluentd-ds  helm chart from the helm repo.

•	The default values.yaml can be modified as per the requirement of cluster setup.is attached above. Further instruction on values is in values.yaml file itself.

•	terminal> helm install <repo-alias>/logging-fluentd-ds -f <customized values.yaml>

**Installing Curator Helm Chart:**

•	Install the elastic-curator helm chart from the helm repo.

•	The default values.yaml can be modified as per the requirement of cluster setup.is attached above. Further instruction on values and its limitations is in values.yaml file itself.

•	terminal> helm install <repo-alias>/elastic-curator -f <customized values.yaml>

**Important Things to Notice**

•	Currently ElasticSearch is by default installed in HA which needs minimum of 3 nodes.(as 3 masters needs to be allocated in 3 different nodes)

•	Minimum RAM requirements for each of client, data, master is 512MB.
 
•	Please take precaution while configuring log retention and rotation as this may lead to disk full scenarios if not configured properly.

•	If the disk is full then all the indices will turn to read-only and you wont be able to insert any new data. This wont happen if care is taken while configuring initial volume size, log retention and rotation
 
•	Make sure that the volume to which es-data is mounted never goes down(HA). If it goes down, elastic will not be able to persist  logs.

# Install
•	Install it with empty volume.

•	Install curator(elastic_curator) only after you install logging is installed as it needs elasticsearch otherwise the curator cronjob errors out. (When logging comes up it will start communicating with it automatically but it is recommended to install it only after logging helm chart )

•	 command → helm install nightly/logging-fluentd-ds -f values.yaml

# Logging  in AWS :

**Changes:**

•	In AWS setup we are using EBS volumes for storing data of elasticsearch and also the fluentd-aggregator buffer.

•	The Elastic Search installation is now using StatefulSet for es-data pods. The type of EBS volume used is ST1 for ElasticSearch whose size limits are  500Gi-16TB . You cannot create a EBS volume with size less than 500Gi .  So the default size in helm is set to 500Gi

•	Fluentd-Aggregator is also using EBS volume for buffering the logs. It is using EBS volume of type gp2 and default size 100Gi.

•	Fluentd Aggregator is also created  as a StatefulSet.
 
•	Node affinity was added to the fluentd-aggregator, es-data and es-client pods. Set the "nodeAffinityEnabled" to "true" for enabling the node affinity. The default value for it  is "m4.2xlarge". Please feel free to change this as per your own requirements.

**Installation:**
    helm install helm-chart -f customized values.yaml
     
# References:

•	{+}https://techstricks.com/fluentd-vs-logstash/+

•	{+}https://logz.io/blog/fluentd-logstash/+

•	{+}https://www.rsyslog.com/+

•	{+}https://www.fluentd.org/guides/recipes/rsyslogd-aggregation+

•	{+}https://www.elastic.co/guide/en/elasticsearch/guide/current/data-in-data-out.html+

•	{+}https://www.elastic.co/blog/found-dive-into-elasticsearch-storage+

