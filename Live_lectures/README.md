# monikit_assignment
monikit assignment


# General Information 
>>>>>Pandas
 #reading data 
	raw_training = pd.read_csv("File.csv")
 #How many rows in data ?
  	raw_trainging.shape[0]
 #which column have null values 
  	raw_trainging.isnull.sum()
 # ignorig missing values
 Ages = raw_trainging[pd.notnull(raw_trainging["Age"])]["Age"]
 #how many mean and women
 (raw_trainging["Sex"].value_counts()[0],raw_trainging["Sex"].value_counts()[1]))
 
 
 
 
 
# Important packages 
 #to profile data in HTML 
 pip install pandas_profiling
 
 
 
 #To save the packages used 
 pip freeze >> requirements.txt
 pip intall -r requirements.txt
 
 # To specify a new enviroment
 condal install -n python= 3.7  testing_1 
 source activate testing_1
 
 
 
#Courses 
https://www.coursera.org/learn/intro-to-deep-learning
