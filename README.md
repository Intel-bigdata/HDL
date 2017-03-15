# HDL - Deep Learning on Hadoop
Support Deep Learning on Hadoop platform, leveraging existing popular Deep Learning engines such as Tensorflow, mxNet, Caffe and Intel Caffe. Ref. [HADOOP-13944](https://issues.apache.org/jira/browse/HADOOP-13944)

This project will focuses on the whole architecture, common facilities and high level considerations. It has respective sub project for each engine, as follows.

* [Tensorflow on YARN](https://github.com/Intel-bigdata/TensorFlowOnYARN)
* [mxNet on YARN](https://github.com/Intel-bigdata/mxnetOnYARN)
* [Caffe on YARN](https://github.com/Intel-bigdata/CaffeOnYARN)

# High level considerations
* A new layer in Hadoop for launching, distributing and executing Deep Learning workloads like for MapReduce;
* A framework in the new layer to leverage and support existing Deep Learning engines such as Tensorflow, Caffe/Intel-Caffe, mxnet, Nevana and etc.;
* Extend and enhance YARN to support the desired scheduling capabilities, like already raised in the community, for FPGA, GPU and etc.;
* Optimize HDFS storage and provide desired data formats for Deep Learning;
* Tools and libraries to submit and manage DL jobs, necessary web UIs for the monitoring and troubleshooting;
* Optionally, for the long term, a common Deep Learning domain representation for users to define DL jobs independent of concrete DL engines.
* Out of scope: new Deep Learning engine. We leverage and support existing DL engines, also allowing users to hook their owns.

# Architecture
![](https://github.com/intel-bigdata/hdl/blob/master/hdl.png)

# Why on Hadoop - the rational
* Deep Learning is data and IO heavy, related advantages in HDFS and Hadoop: of vast data to learn from, already existing or easy loading into; data locality, still desired in DL; tiered storage support, to use faster devices like NVMe SSD, 3D XPoint and persistent memory; cache support, to use large memory for hot or repeatedly accessed data; even Ozone, the KV store for amounts of small objects and the desired API; and the cloud support.
* Deep Learning is computing heavy, related advantages in YARN: flexible, to support complex computing frameworks and applications; hardware capability aware, accordingly scheduling and distributing, thinking about FPGA, GPU and RDMA; large scale, proven scalability supporting thousands of nodes; nice facilities such as timeline service and richful interfaces (cmds, restful and web).
* As a common and low level facility layer, easier to optimize in bottom, yet powerful to support above frameworks, such as Spark, Flink, Hive and Streams. Don’t need to hack everywhere, but in a central place and common layer.
* Security, enterprise and distribution. A mature ecosystem for Deep Learning to build upon.

