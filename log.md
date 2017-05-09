Worker information
hostname: i-02c1ea8-precise-production-2-worker-org-docker.travisci.net:44642919-dd42-4e13-ab43-44e41469cb39
version: v2.5.0 https://github.com/travis-ci/worker/tree/da3a43228dffc0fcca5a46569ca786b22991979f
instance: d85a46c:travis:python
startup: 546.932742ms
Build system information
Build language: python
Build group: stable
Build dist: precise
Build id: 230537702
Job id: 230537703
travis-build version: 6b1476380
Build image provisioning date and time
Thu Feb  5 15:09:33 UTC 2015
Operating System Details
Distributor ID:	Ubuntu
Description:	Ubuntu 12.04.5 LTS
Release:	12.04
Codename:	precise
Linux Version
3.13.0-29-generic
Cookbooks Version
a68419e https://github.com/travis-ci/travis-cookbooks/tree/a68419e
GCC version
gcc (Ubuntu/Linaro 4.6.3-1ubuntu5) 4.6.3
Copyright (C) 2011 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

LLVM version
clang version 3.4 (tags/RELEASE_34/final)
Target: x86_64-unknown-linux-gnu
Thread model: posix
Pre-installed Ruby versions
ruby-1.9.3-p551
Pre-installed Node.js versions
v0.10.36
Pre-installed Go versions
1.4.1
Redis version
redis-server 2.8.19
riak version
2.0.2
MongoDB version
MongoDB 2.4.12
CouchDB version
couchdb 1.6.1
Neo4j version
1.9.4
RabbitMQ Version
3.4.3
ElasticSearch version
1.4.0
Installed Sphinx versions
2.0.10
2.1.9
2.2.6
Default Sphinx version
2.2.6
Installed Firefox version
firefox 31.0esr
PhantomJS version
1.9.8
ant -version
Apache Ant(TM) version 1.8.2 compiled on December 3 2011
mvn -version
Apache Maven 3.2.5 (12a6b3acb947671f09b81f49094c53f426d8cea1; 2014-12-14T17:29:23+00:00)
Maven home: /usr/local/maven
Java version: 1.7.0_76, vendor: Oracle Corporation
Java home: /usr/lib/jvm/java-7-oracle/jre
Default locale: en_US, platform encoding: ANSI_X3.4-1968
OS name: "linux", version: "3.13.0-29-generic", arch: "amd64", family: "unix"

$ export DEBIAN_FRONTEND=noninteractive
Reading package lists...
Building dependency tree...
Reading state information...
The following extra packages will be installed:
  libc-bin libc-dev-bin libc6-dev
Suggested packages:
  glibc-doc
The following packages will be upgraded:
  libc-bin libc-dev-bin libc6 libc6-dev
4 upgraded, 0 newly installed, 0 to remove and 264 not upgraded.
Need to get 8,856 kB of archives.
After this operation, 13.3 kB of additional disk space will be used.
Get:1 http://us.archive.ubuntu.com/ubuntu/ precise-updates/main libc6-dev amd64 2.15-0ubuntu10.18 [2,948 kB]
Get:2 http://us.archive.ubuntu.com/ubuntu/ precise-updates/main libc-dev-bin amd64 2.15-0ubuntu10.18 [84.5 kB]
Get:3 http://us.archive.ubuntu.com/ubuntu/ precise-updates/main libc-bin amd64 2.15-0ubuntu10.18 [1,178 kB]
Get:4 http://us.archive.ubuntu.com/ubuntu/ precise-updates/main libc6 amd64 2.15-0ubuntu10.18 [4,646 kB]
Fetched 8,856 kB in 0s (14.6 MB/s)
Preconfiguring packages ...
(Reading database ... 72431 files and directories currently installed.)
Preparing to replace libc6-dev 2.15-0ubuntu10.10 (using .../libc6-dev_2.15-0ubuntu10.18_amd64.deb) ...
Unpacking replacement libc6-dev ...
Preparing to replace libc-dev-bin 2.15-0ubuntu10.10 (using .../libc-dev-bin_2.15-0ubuntu10.18_amd64.deb) ...
Unpacking replacement libc-dev-bin ...
Preparing to replace libc-bin 2.15-0ubuntu10.10 (using .../libc-bin_2.15-0ubuntu10.18_amd64.deb) ...
Unpacking replacement libc-bin ...
Processing triggers for man-db ...
Setting up libc-bin (2.15-0ubuntu10.18) ...
(Reading database ... 72430 files and directories currently installed.)
Preparing to replace libc6 2.15-0ubuntu10.10 (using .../libc6_2.15-0ubuntu10.18_amd64.deb) ...
Unpacking replacement libc6 ...
Setting up libc6 (2.15-0ubuntu10.18) ...
Setting up libc-dev-bin (2.15-0ubuntu10.18) ...
Setting up libc6-dev (2.15-0ubuntu10.18) ...
Processing triggers for libc-bin ...
ldconfig deferred processing now taking place
$ sudo apt-get install libssl1.0.0
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following extra packages will be installed:
  libssl-dev
The following packages will be upgraded:
  libssl-dev libssl1.0.0
2 upgraded, 0 newly installed, 0 to remove and 262 not upgraded.
Need to get 2,634 kB of archives.
After this operation, 29.7 kB of additional disk space will be used.
Get:1 http://us.archive.ubuntu.com/ubuntu/ precise-updates/main libssl-dev amd64 1.0.1-4ubuntu5.39 [1,580 kB]
Get:2 http://us.archive.ubuntu.com/ubuntu/ precise-updates/main libssl1.0.0 amd64 1.0.1-4ubuntu5.39 [1,054 kB]
Fetched 2,634 kB in 0s (17.8 MB/s)
Preconfiguring packages ...
(Reading database ... 72430 files and directories currently installed.)
Preparing to replace libssl-dev 1.0.1-4ubuntu5.21 (using .../libssl-dev_1.0.1-4ubuntu5.39_amd64.deb) ...
Unpacking replacement libssl-dev ...
Preparing to replace libssl1.0.0 1.0.1-4ubuntu5.21 (using .../libssl1.0.0_1.0.1-4ubuntu5.39_amd64.deb) ...
Unpacking replacement libssl1.0.0 ...
Setting up libssl1.0.0 (1.0.1-4ubuntu5.39) ...
Setting up libssl-dev (1.0.1-4ubuntu5.39) ...
Processing triggers for libc-bin ...
ldconfig deferred processing now taking place
$ git clone --depth=50 --branch=master https://github.com/omnific-h/CSCI4830-Repository.git omnific-h/CSCI4830-Repository
Cloning into 'omnific-h/CSCI4830-Repository'...
remote: Counting objects: 43, done.
remote: Compressing objects: 100% (42/42), done.
remote: Total 43 (delta 18), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (43/43), done.
Checking connectivity... done.

$ cd omnific-h/CSCI4830-Repository
$ git checkout -qf 3b0be856f5fe1a5de198822026c0f8c08875a27f
$ source ~/virtualenv/python2.7/bin/activate

$ python --version
Python 2.7.9
$ pip --version
pip 6.0.7 from /home/travis/virtualenv/python2.7.9/lib/python2.7/site-packages (python 2.7)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
$ python pytest.py
Hello world from Travis CI
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK


The command "python pytest.py" exited with 0.

Done. Your build exited with 0.
