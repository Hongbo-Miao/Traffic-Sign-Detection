import numpy as np
import os

#own stuff
from sign_checker import SignChecker

###########################################
"""
author: Kim-Louis Simmoteit

This script trains a SVM with the
output of preprocess_*.py.
"""
###########################################

output_path = "./SVMs/" #path to folders with SVM
if not os.path.exists(output_path):
	os.makedirs(output_path)

svm_prefix = "11_"	#SVM prefix

#load all calculated HOG-Descriptors
load_path = "./Train_data/"
max_run = 60  #only take runs with have the first 600 images of GTSDB as origin
data = np.load(load_path+"gtsdb.npy")
for i in range(1,max_run+1):
	if i==58: #58 has no sign and no negative samples -> neglect
		continue
	data = np.concatenate((data, np.load(load_path+"hog_run_"+str(i)+".npy")), axis=0)

for i in range(43):
	data = np.concatenate((data, np.load(load_path+"hog_train_c"+str(i)+".npy")), axis=0)

print("Data loaded! Training SVM ...")
sc = SignChecker()
sc.train(data[:,1:],data[:,0])
sc.save(output_path+svm_prefix)

#parameters:
#1 - C=10 gamma=5 #start (forgot transform_sqrt at full image!)			->RIP
#2 - C=1.0 gamma="auto" - standard settings								-> Best so far	
#3 - C=1.0 gamma=0.1
#4 - same settings as 3 just more data									->RIP
#5 - same settings as 2 just more data									->RIP
#6 - C=2.0 gamma="auto"													
#7 - C=10 gamma="auto"													-> slightly better
#8 - C=10 gamma=1.0  - with 32x32 color images							->RIP
#9 - Linear C=50
#10 - C=50 gamma=10
#11 - Random background data - standard settings
