Docker image for [FDDB (Face Detection Data Set and Benchmark)](http://vis-www.cs.umass.edu/fddb/results.html) evaluation.

## Usage

Clone this repository:
```bash
git clone https://github.com/jan3zk/fddb_evaluation_docker.git
cd fddb_evaluation_docker/
```

Download originalPics:
```bash
wget http://vis-www.cs.umass.edu/fddb/originalPics.tar.gz
tar -xvf originalPics.tar.gz
mkdir originalPics
mv 2002 originalPics/
mv 2003 originalPics/
```

Download FDDB-folds:
```bash
wget http://vis-www.cs.umass.edu/fddb/FDDB-folds.tgz
tar -xvf FDDB-folds.tgz
```

After executing above commands, make sure you have the following directory structure in `FDDB_HOME`:
```
originalPics/
   2002/
   (...)
FDDB-folds/
   FDDB-fold-01-ellipseList.txt
   FDDB-fold-01.txt
   (...)
detections/
   fold-01-out.txt
   fold-02-out.txt
   (...)
```

Install docker:
```bash
sudo apt-get install docker.io
sudo service docker start
```

Run the command below mapping `FDDB_HOME` to `/FDDB`:
```bash
docker run --rm -it -v ${FDDB_HOME}:/FDDB housebw/fddb-evaluator
```
where `FDDB_HOME` should be set to the folder where this repository was cloned to, e.g. `FDDB_HOME=/home/my_name/fddb_evaluation_docker/`.

If everything goes fine you should see:
```bash
Processing 2845 images
0 images done
(...)
2844 images done
```
And 4 new files in `FDDB_HOME`:
* detectionsContROC.png
* detectionsContROC.txt
* detectionsDiscROC.png
* detectionsDiscROC.txt

Sample files in `detections\` and ROC curves are obrained by the MTCNN detector. Replace these files to perform the evaluation with your own detector.
