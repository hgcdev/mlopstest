import mysql.connector
import pandas as pd
import mlflow
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from joblib import dump


#Connect with mysql server db container
db_connection = mysql.connector.connect(
    host='db',
    user='user',
    passwd='user123')

#select database data
db_cursor = db_connection.cursor()
db_cursor.execute("use data") 

#select table Iris
db_cursor.execute("select SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm,Species from Iris")

#get column names
columns = db_cursor.column_names
#get rows
table_rows = db_cursor.fetchall()
#create dataframe from mysql connection
iris = pd.DataFrame(table_rows,columns=columns)

#prepare dataset

X = iris.iloc[:, :-1].values
y = iris.iloc[:, -1].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

mlflow.set_experiment("iris") # creates an experiment if it doesn't exist


with mlflow.start_run(run_name="Iris RF Experiment") as run:
    
    # train the model
    LRclassifier = LogisticRegression(solver='liblinear')
    LRclassifier.fit(X_train, y_train)
    y_pred = LRclassifier.predict(X_test)
    print(classification_report(y_test, y_pred))
    print(confusion_matrix(y_test, y_pred))


    # save the model artifact for deployment
    mlflow.sklearn.log_model(LRclassifier, "Logistic-Regression-model")

    # log model performance 
    LRAcc = accuracy_score(y_pred,y_test)
    print('accuracy is', LRAcc)
    mlflow.log_metric("acc", LRAcc)
   
    run_id = run.info.run_uuid
    experiment_id = run.info.experiment_id
    mlflow.end_run()
    print(mlflow.get_artifact_uri())
    print("runID: %s" % run_id)
    dump(LRclassifier, './predmodel.joblib')