MLOPS TEST Hernan Gonzalez

1. The solution is based on 3 containers: db, model builder and api exposure.
2. First you'll need to create the docker images in your local image repo
	FOR DB: docker build --pull --rm -f "Dockerfiles\dbtrain.Dockerfile" -t mlopsdb:1.0 "Dockerfiles"
	FOR BUILDER: docker build --pull --rm -f "Dockerfiles\modelbuilder.Dockerfile" -t mlopsbuilder:1.0 "Dockerfiles" 
	FOR API: docker build --pull --rm -f "Dockerfiles\api.Dockerfile" -t mlopsapi:1.0 "Dockerfiles" 
3. The docker compose file is in charge to orchestrate these 3 services. cd into Docker Compose folder and execute docker compose up.
4. The dynamic of the containers is as follows:
	-mlopsdb image is in charge to boot up a mysql instance with a database named data and a table named Iris with the Iris dataset.
	-mlopsbuilder is in charge to read the data from Iris table, and serve as a pythonbox, youll need to execute model.py in order to trigger the mlflow pipeline and save 
	 recent version of the classifier called predmodel.joblib
	-mlopsapi is in charge to expose predmodel.joblib in the post method "/predict"

Regards. 
	
