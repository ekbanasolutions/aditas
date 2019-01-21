# Aditas

- [Introduction](#introduction)
- [Features](#features)
    - [Bigdata Services](#bigdata-services)
    - [Linux System](#linux-system)
- [How is Aditas different from Cloudera/Ambari](#comparision)
- [User](#user)
- [Built with](#built-with)
- [License](#license)

## Introduction

Aditas is a python based application which displays information such as service-specific (Hadoop, HBase, Elasticsearch) summaries, graphs, and alerts. You can create and manage your cluster using kento to perform basic operational tasks, such as starting and stopping services, adding hosts to your cluster, and updating service configurations. You also can use kento to monitor cpu-usage, memory-usage, network-bandwidth, disk-usage, disk I/O and top processes of your linux system.

## Features
We have many features for both Bigdata services and linux server.

- #### Bigdata Services
```
* Restart all services
* Stop all services
* Restart/Stop specific service such as Namenode, Datanode, Regionserver etc.
* Monitor their usages (cpu, memory, i/o...)
* Changing configuration of services
* Copy from/to HDFS
```

- #### Linux system
```
* Make new directories
* Archive/Extract-Archive
* Copy multiple files
* Move multiple files
* Rename files
* Delete files/folders
* Head/Tail files
```

## How is Aditas different from Cloudera/Ambari
Aditas is not a replacement of Cloudera/Ambari. Cloudera and Ambari both are tools to manage and monitor Bigdata Services, but both of them requires you to install, configure and manage hadoop ecosystem through their application. 
So, if you have your own cluster and want to monitor or manage it then these tools doesn't provide you a platform for that. Where as Aditas lets you to manage and monitor your existing services.

## User
Aditas can be used by different type of users. It is mainly focused for those who are familier with bigdata services and works on Hadoop eco-system, but it can also be used by users who works on linux system, there are some useful features available for them.

## License

This project is licensed under MIT LICENSE

