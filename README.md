# Operationalizing_Machine_Learning
Udacity Nano Degree Project 2

This is the second project in the Udacity Machine Learning Engineer with Microsoft Azure Nanodegree Program. In this project, Azure was used to configure a cloud-based machine learning production model, deploy it, and consume it. A pipeline was also created, published, and consumed.

## Project Overview

This project had 2 primary components:

- The first part required the creation of a machine learning model using AutoML in Azure Machine Learning Studio. The best AutoML model (based on accuracy) was deployed using Azure Container Instance (ACI) and consumed through a REST API endpoint. Swagger UI was used to help understand the REST API requirements. 
- The second part of the project used the Azure Python SDK to create, train, and publish the full pipeline instead of the alternative GUI-based Azure Machine Learning Studio approach used in Part 1. A Jupyter Notebook was used to create the pipeline code. I used my personal Azure account to create and deploy the model.

The Bank Marketing dataset from UCI ( [link](https://automlsamplenotebookdata.blob.core.windows.net/automl-sample-notebook-data/bankmarketing_train.csv) ) was used for this classification project. The goal of the classification experiment was to predict whether the client would accept an offer to open a bank term deposit. The result of the prediction appears in column *`y`* and can be either *`yes`* or *`no`*.



## **Architectural Diagram**

TBD

The project consisted of the following main steps:

- **Authentication:** The Azure Machine Learning Extension is installed in the Workspace. A Security Principal account was then created to securely interact with Azure Machine Learning Studio over the internet. 
- **Automated ML Experiment:** In this step, the chosen dataset (e.g. Bank Marketing) was uploaded into the Azure Machine Learning Studio. Next, a new experiment was created using AutoML, a compute cluster was created, the type of machine learning task was chosen (e.g. classification for this experiment), the exit criteria were defined (e.g. 1 hour max duration for the training time) and then the model was trained on the dataset using the defined compute cluster.
- **Deploy the Best Model:** After the AutoML experiment was completed, a summary of the generated models and their metrics was shown. The *Best Model* , along with its explanation, was available in the *Details* tab ( it also appears at the top of the *Models* tab). The best model was deployed with Authentication using an Azure Container Instance (ACI). Once deployed, the HTTP API allowed the model to be interacted with by sending data through POST requests.
- **Enable Logging:** After deploying the Best Model, Application Insights were enabled using the Python SDK and the logs.py script. Logs were retrieved and reviewed.
- **Swagger Documentation:** In this step, the deployed model was consumed via the Swagger UI, Docker Desktop and the provided Swagger JSON file from Azure. The deployed model was visible in the *Endpoints* section of Azure ML Studio. The Swagger UI makes it easy to understand how to send requests to the API and what type of data should be included in the request. 
- **Consume Model Endpoints:** The enpoint.py script was used to interact with the deployed model by sending it test data and receiving back a classification prediction (e.g. Yes or No). The endpoint.py script had to be modified to include the specific *scoring_uri* for the deployed model and the authentication *key* for the model. The URI was located in the *Details* tab of the deployed model (above the Swagger URI) and the key was located on the Consume tab. Additionally, the model response time was also benchmarked using Apache Benchmark and the benchmark.sh file. Based on the results of the benchmarking using first 10 and then 100 sample requests, the model can accommodate approximately 3 requests per second and there were no failed requests.
- **Create, Publish and Consume a Pipeline:** For the second part of the project, a Jupyter Notebook-based pipeline  was created with the same key, URI, dataset, compute cluster, and model name created in Part 1 to create, publish and consume the AutoML experiment. This step required the `config.json` file (downloaded from the Azure workspace > Settings) to be located in the same working directory as the Notebook. The Notebook allows for the entire process of training and deploying the model to be automated.
- **Documentation:** The final step in the project was the creation of documentation. The required documentation includes:
  - 1) [My Screencast Demo](URL) showing a working deployed model, a deployed pipeline, an available AutoML model and successful API requests to the deployed Endpoint with a JSON payload 
    2) this README file describing the project's main steps.

## Future Improvements

1. Class imbalance issue
2. Use a parallel run step in the pipeline



## Required Screenshots

##### Deploy model in Azure ML Studio

###### Create Security Principal Account

This screenshot shows the successful creation of a Security Principal account in my Azure workspace. No errors were returned after running the az ml workspace share command.

<<<<<<< HEAD
![Successfully create Service Principal Role](C:\Users\Courtlin\Documents\GitHub\Operationalizing_Machine_Learning\Required Screenshots\Successfully create Service Principal Role.jpg)



###### Create a new AutoML run

This screenshot shows that the "Bankmarketing" dataset is registered and available in Azure ML Studio ![2 Registered dataset bankmarketing](C:\Users\Courtlin\Documents\GitHub\Operationalizing_Machine_Learning\Required Screenshots\2 Registered dataset bankmarketing.jpg)



This screenshot shows that the bankmarketing-automl experiment was completed in 29 minutes and 22 seconds with a final AUC of 0.946.

![3 Automl experiment completed](C:\Users\Courtlin\Documents\GitHub\Operationalizing_Machine_Learning\Required Screenshots\3 Automl experiment completed.jpg)



###### Deploy a model and consume a model endpoint via an HTTP API

Endpoints section in Azure ML Studio, showing that “Application Insights enabled” says “true”.



Logging is enabled by running the provided `logs.py` script



Swagger runs on localhost showing the HTTP API methods and responses for the model



`endpoint.py` script runs against the API producing JSON output from the model.



Apache Benchmark (ab) runs against the HTTP API using authentication keys to retrieve performance results. (optional)





## Link to project walk-through screencast
=======
![Successfully create Service Principal Role](https://github.com/icenine81/Operationalizing_Machine_Learning/blob/b78f13c899ac72ea4f68834c11f8e0401f96898f/Required%20Screenshots/Successfully%20create%20Service%20Principal%20Role.jpg)
>>>>>>> b3be02abae9485d255aefd1735640aa024c5ae14
