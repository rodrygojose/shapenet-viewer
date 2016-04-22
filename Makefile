SBT=bin/sbt

# check if on jenkins and setup some env variables
#ifdef WORKSPACE

#def WORKSPACE
#WORKSPACE = "/user/rortizca/home/workspace/useful_code/shapenet-viewer"

export DATA_DIR=/user/rortizca/home/workspace/useful_code/shapenet-viewer/data/test
export WORK_DIR=/user/rortizca/home/workspace/useful_code/shapenet-viewer/data/out
#export DATA_DIR=$(WORKSPACE)/test/data
#export WORK_DIR=$(WORKSPACE)/work
$(info Setting DATA_DIR to $(DATA_DIR))  
$(info Setting WORK_DIR to $(WORK_DIR))

#endif

.PHONY: default all sbt compile test clean package assembly deps

default: package assembly

all: package assembly deps

sbt: bin/sbt-launch.jar

bin/sbt-launch.jar:
	wget "http://repo.typesafe.com/typesafe/ivy-releases/org.scala-sbt/sbt-launch/0.13.7/sbt-launch.jar" -P bin

compile: sbt
	$(SBT) compile

test: sbt
	$(SBT) test

clean: sbt
	$(SBT) clean

package: sbt
	$(SBT) package

assembly: sbt
	$(SBT) assembly

deps: sbt
	$(SBT) assemblyPackageDependency
