Docker image for [FDDB (Face Detection Data Set and Benchmark)](http://vis-www.cs.umass.edu/fddb/results.html) evaluation.

## Usage

Download [originalPics](http://vis-www.cs.umass.edu/fddb/originalPics.tar.gz) and [FDDB-folds](http://vis-www.cs.umass.edu/fddb/FDDB-folds.tgz).

Make sure you have the following directory structure in `FDDB_HOME`:
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

Install docker by running:
```bash
sudo apt-get install docker.io
sudo service docker start
```

Run the command below mapping `FDDB_HOME` to `/FDDB`:
```bash
docker run --rm -it \
   -v ${FDDB_HOME}:/FDDB \
   housebw/fddb-evaluator
```
where `FDDB_HOME` should be set to the folder of this repository.

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
