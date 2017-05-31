# HDL - Deep Learning on Hadoop
Support Deep Learning on Hadoop platform, leveraging existing popular Deep Learning engines such as TensorFlow, MXNet, Caffe and Intel Caffe. Ref. [HADOOP-13944](https://issues.apache.org/jira/browse/HADOOP-13944)

This project will focuses on the whole architecture, common facilities and high level considerations. It has respective sub project for each engine, as follows.

* [TensorFlow on YARN](https://github.com/Intel-bigdata/TensorFlowOnYARN)
* [MXNet on YARN](https://github.com/Intel-bigdata/mxnetOnYARN)
* [Caffe on YARN](https://github.com/Intel-bigdata/CaffeOnYARN)

# High level considerations
* A new layer in Hadoop for launching, distributing and executing Deep Learning workloads like for MapReduce;
* A framework in the new layer to leverage and support existing Deep Learning engines such as TensorFlow, Caffe/Intel-Caffe, MXNet, Nevana and etc.;
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

# How TO Run

### 1. TensorFlow
   
1. Prepare the build environment following the instructions from [TensorFlow tutorial](https://www.tensorflow.org/install/install_sources)

2. Run the [between-graph mnist example](TensorflowOnYARN/examples/between-graph/mnist_feed.py).

Assume you are in `TensorflowOnYARN` dir.
**Method One:**

Apply resources (ClusterSpec) and run.

```bash
bin/ydl-tf launch --num_worker 2 --num_ps 2
```

This will launch a YARN application, which creates a `tf.train.Server` instance for each task. A `ClusterSpec` is printed on the console such that you can submit the training script to. e.g.

```bash
ClusterSpec: {"ps":["node1:22257","node2:22222"],"worker":["node3:22253","node2:22255"]}
```

```bash
python examples/between-graph/mnist_feed.py \
	--ps_hosts="ps0.hostname:ps0.port,ps1.hostname:ps1.port" \
	--worker_hosts="worker0.hostname:worker0.port,worker1.hostname:worker1.port" \
	--task_index=0

python examples/between-graph/mnist_feed.py \
	--ps_hosts="ps0.hostname:ps0.port,ps1.hostname:ps1.port" \
	--worker_hosts="worker0.hostname:worker0.port,worker1.hostname:worker1.port" \
	--task_index=1
```
**Method Two:**
  
Directly submit TensorFlow training jobs and parameters to YARN.

```bash
python bin/demo.py "bin/ydl-tf" "launch" "examples/between-graph/mnist_feed.py"
```

3. To get ClusterSpec of an existing TensorFlow cluster launched by a previous YARN application.

```bash
bin/ydl-tf cluster --app_id <Application ID>
```

4. You can also use YARN commands through `ydl-tf`. 

For example, get running application list,

```bash
bin/ydl-tf application --list
```

or kill an existing YARN application(TensorFlow cluster),

```bash
bin/ydl-tf kill --application <Application ID>
```

### 2. Caffe
Assume you are in `CaffeOnYARN` dir.

1. Train mnist with the jar package, prototxt and parameters. The number means the number of service we launch.
   
```bash
bin/ydl-caffe -jar ydl-caffe.jar -conf /path/lenet_memory_solver.prototxt -model hdfs:///mnist.model -num 3
```

2. Check the log using the applicationId we get from the screen 
   
```bash
yarn logs -applicationId xxxxxxxxxx | less
```
or kill an existing YARN application,

```bash
yarn application -kill <Application ID>
```


### 3. MXNet
Assume you are in `MXNetOnYARN` dir. 
1. Train mnist in distributed model.

```bash
bin/ydl-mx 2 train_mnist.py --kv-store sync
```
   
2. Check the log using the applicationId we get from the screen 

```bash
yarn logs -applicationId xxxxxxxxxxxx | less
```
or kill an existing YARN application,

```bash
yarn application -kill <Application ID>
```
