import os
import re

# Obtain predict.txt from https://github.com/hualitlc/MTCNN-on-FDDB-Dataset/blob/master/FDDB-folds/predict.txt

with open('predict.txt', 'r') as predfile:
  pred = predfile.readlines()

for fold in range(10):
  with open('./FDDB-folds/FDDB-fold-%02d.txt'%(fold+1)) as f:
    foldfiles = [line.rstrip('\n') for line in f]
  with open('./detections/fold-%02d-out.txt'%(fold+1), 'w') as outfile:
    for ff in foldfiles:
      idx = pred.index([s for s in pred if ff+'\n' in s][0])
      numdet = int(pred[idx+1][:-1])
      det = pred[idx:idx+numdet+2]
      outfile.write(''.join(det))
