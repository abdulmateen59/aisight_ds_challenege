# AiSight Data Science Challenge!
**Docker**
To Run the tasks in dockers container use following command :
```sh
$ docker build -t aisight . && docker run -it --rm aisight /bin/bash
```
Once the container is up run the driver code :
```sh
$ python3 main.py
```  
#  Toolset
    - Python 3.7.5
    - Sklearn 0.21.3
    - Panadas 0.24.2
    
# Dataset
The dataset reside in **DataSet** directory and proficient with both provided datasets. To change the dataset use -F argument while executing the script e.g.
```sh
$ python3 main.py -F /DataSet/project/project_pump.csv
```
# Project Details
The project is divided into 3 tasks and each task has its own class which is placed in the libs directory.
 1) preprosses
 2) clustering
 3) machine learning
- **main.py** is the driver code used to run the project. 
 
# Preprocess
 - It reads the CSV file and transform it for further processing.
 - PreProcess implements sensor data aggregation functions as well such as **mean**, **sum**, **max**, **min**
 
# Clustering
 - This class is used to find the best cluster size based upon ***silhouette score***
 - It check from cluter size 2 to 20 and returns the best size of cluster.

# Machine learing
- The Machine learning module splits the data into 25% for test and 75% for training.
- Four different machine learning algorithms are implemented from which ***K Neighbors*** is the most optimized for the given problems whereas **Navie Bayes** also performs closely. 
- Dump and load model functionality is also added to this module.

---
For any further questions please contact me at:                             
[Email : abdul.mateen59@yahoo.com](abdul.mateen59@yahoo.com)