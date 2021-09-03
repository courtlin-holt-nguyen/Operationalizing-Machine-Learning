# Operationalizing_Machine_Learning
#### Udacity Machine Learning Engineer with Microsoft Azure Nanodegree Project 2

This is the second project in the Udacity Machine Learning Engineer with Microsoft Azure Nanodegree Program. In this project, Azure was used to configure a cloud-based machine learning production model, deploy it, and consume it. A pipeline was also created, published, and consumed.

## Project Overview

This project had 2 primary components:

- The first part required the creation of a machine learning model using AutoML in Azure Machine Learning Studio. The best AutoML model (based on accuracy) was deployed using Azure Container Instance (ACI) and consumed through a REST API endpoint. Swagger UI was used to help understand the REST API requirements.
- The second part of the project used the Azure Python SDK to create, train, and publish the full pipeline instead of the alternative GUI-based Azure Machine Learning Studio approach used in Part 1. A Jupyter Notebook was used to create the pipeline code. I used my personal Azure account to create and deploy the model.

The Bank Marketing dataset from UCI ( [link](https://automlsamplenotebookdata.blob.core.windows.net/automl-sample-notebook-data/bankmarketing_train.csv) ) was used for this classification project. The goal of the classification experiment was to predict whether the client would accept an offer to open a bank term deposit. The result of the prediction appears in column *`y`* and can be either *`yes`* or *`no`*.



## **Architectural Diagram**

![Architectural Design Project Overview](https://github.com/icenine81/Operationalizing_Machine_Learning/blob/52064b639b373ce3d08244761d5e844b8c808c73/Required%20Screenshots/Architectural%20Design%20Project%20Overview.jpg)

This project consisted of the following main steps:

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

1. Class imbalance issue - this project could be improved by addressing the issue of class imbalance that exists in the dataset. As shown in the screenshot, the number of "Yes" outcomes only represent 11% of the total responses in the dataset. This is a problem because a simple model could be trained to always predict a "No" response and it would be correct nearly 90% of the time.  

![20 Areas for improvement Class imbalance](https://github.com/icenine81/Operationalizing_Machine_Learning/blob/47798a1d29f4cecf821d426726bb41302d2dcef5/Required%20Screenshots/20%20Areas%20for%20improvement%20Class%20imbalance%202.jpg)



![20 Areas for improvement Class imbalance 2](C:\Users\Courtlin\Documents\GitHub\Operationalizing_Machine_Learning\Required Screenshots\20 Areas for improvement Class imbalance 2.jpg)





1. Use a Parallel Run Step in the pipeline - An additional improvement would be to use a parallel run step in the pipeline to speed up model training by breaking the dataset into smaller batches and processing them at the same time.

   https://docs.microsoft.com/en-us/python/api/azureml-pipeline-steps/azureml.pipeline.steps.parallel_run_step.parallelrunstep?view=azure-ml-py

![ParallelRunStep Class](https://github.com/icenine81/Operationalizing_Machine_Learning/blob/47798a1d29f4cecf821d426726bb41302d2dcef5/Required%20Screenshots/ParallelRunStep%20Class.jpg)

## Required Screenshots

##### Deploy model in Azure ML Studio

###### Create Security Principal Account

This screenshot shows the successful creation of a Security Principal account in my Azure workspace. No errors were returned after running the az ml workspace share command.

![1 Successfully create Service Principal Role](https://github.com/icenine81/Operationalizing_Machine_Learning/blob/47798a1d29f4cecf821d426726bb41302d2dcef5/Required%20Screenshots/1%20Successfully%20create%20Service%20Principal%20Role.jpg)

###### Create a new AutoML run

This screenshot shows that the "Bankmarketing" dataset is registered and available in Azure ML Studio ![2 Registered dataset bankmarketing](https://github.com/icenine81/Operationalizing_Machine_Learning/blob/47798a1d29f4cecf821d426726bb41302d2dcef5/Required%20Screenshots/2%20Registered%20dataset%20bankmarketing.jpg)

This screenshot shows that the bankmarketing-automl experiment was completed in 29 minutes and 22 seconds.

![3 Automl experiment completed](https://github.com/icenine81/Operationalizing_Machine_Learning/blob/47798a1d29f4cecf821d426726bb41302d2dcef5/Required%20Screenshots/3%20Automl%20experiment%20completed.jpg)



This screenshot shows the summary statistics about the best model (a Voting Ensemble model)

![4 Best Model Summary](https://github.com/icenine81/Operationalizing_Machine_Learning/blob/47798a1d29f4cecf821d426726bb41302d2dcef5/Required%20Screenshots/4%20Best%20Model%20Summary.jpg)

This screenshot shows the best model had an Accuracy of 0.91927

![5 Best Model Summary 2](https://github.com/icenine81/Operationalizing_Machine_Learning/blob/47798a1d29f4cecf821d426726bb41302d2dcef5/Required%20Screenshots/5%20Best%20Model%20Summary%202.jpg)

This screenshot shows the Explanation about the most important features of the model

![6 Best Model Summary 3](https://github.com/icenine81/Operationalizing_Machine_Learning/blob/47798a1d29f4cecf821d426726bb41302d2dcef5/Required%20Screenshots/6%20Best%20Model%20Summary%203.jpg)



This screenshot shows the precision and recall curves

![7 Best Model Summary 4](https://github.com/icenine81/Operationalizing_Machine_Learning/blob/47798a1d29f4cecf821d426726bb41302d2dcef5/Required%20Screenshots/7%20Best%20Model%20Summary%204.jpg)



###### Deploy a model and consume a model endpoint via an HTTP API

The Endpoints section in Azure ML Studio, shows that the model was deployed with Application Insights disabled. 

![8 Best model deployed without App Insights](https://github.com/icenine81/Operationalizing_Machine_Learning/blob/47798a1d29f4cecf821d426726bb41302d2dcef5/Required%20Screenshots/8%20Best%20model%20deployed%20without%20App%20Insights.jpg)



This screenshot now shows that “Application Insights enabled” says “true” after being modified with the Python SDK.

![9 Application insights enabled after Python SDK](https://github.com/icenine81/Operationalizing_Machine_Learning/blob/47798a1d29f4cecf821d426726bb41302d2dcef5/Required%20Screenshots/9%20Application%20insights%20enabled%20after%20Python%20SDK.jpg)

These 2 screenshots show that Logging was enabled by running the provided `logs.py` script

![10 Application insights enabled - logs generated](https://github.com/icenine81/Operationalizing_Machine_Learning/blob/47798a1d29f4cecf821d426726bb41302d2dcef5/Required%20Screenshots/10%20Application%20insights%20enabled%20-%20logs%20generated.jpg)

![11 Application insights enabled - logs generated GUI](https://github.com/icenine81/Operationalizing_Machine_Learning/blob/47798a1d29f4cecf821d426726bb41302d2dcef5/Required%20Screenshots/11%20Application%20insights%20enabled%20-%20logs%20generated%20GUI.jpg)



This screenshot shows that Swagger UI was running on localhost and showing the HTTP API methods and responses for the model.

![12 Swagger API interaction](https://github.com/icenine81/Operationalizing_Machine_Learning/blob/47798a1d29f4cecf821d426726bb41302d2dcef5/Required%20Screenshots/12%20Swagger%20API%20interaction.jpg)



This screenshot shows that `endpoint.py` script ran against the API producing JSON output from the model. The result was "no" for the sample data provided in the JSON payload.

![13 Using endpoint-py to interact with the API](https://github.com/icenine81/Operationalizing_Machine_Learning/blob/47798a1d29f4cecf821d426726bb41302d2dcef5/Required%20Screenshots/13%20Using%20endpoint-py%20to%20interact%20with%20the%20API.jpg)



This screenshot shows that Apache Benchmark (ab) runs against the HTTP API using authentication keys to retrieve performance results. In this case, 100 sample requests were run against the endpoint ; 3.15 requests per second were handled by the API, on average. 

![14 Apache benchmark runs against the endpoint](https://github.com/icenine81/Operationalizing_Machine_Learning/blob/47798a1d29f4cecf821d426726bb41302d2dcef5/Required%20Screenshots/14%20Apache%20benchmark%20runs%20against%20the%20endpoint.jpg)



##### Publish an ML Pipeline

###### Create and publish a pipeline

This screenshot shows the Pipelines section of Azure ML Studio and the pipelines that have been successfully created. Note, the failed pipelines were due to various snippets of legacy code in the Jupyter Notebook that referenced the Bike Sharing experiment instead of the Bank Marketing experiment.   

![15 Azure ML pipelines section showing created pipelines](https://github.com/icenine81/Operationalizing_Machine_Learning/blob/47798a1d29f4cecf821d426726bb41302d2dcef5/Required%20Screenshots/15%20Azure%20ML%20pipelines%20section%20showing%20created%20pipelines.jpg)



This screenshot shows that the Bankmarketing dataset was used as the dataset for the automl_module in the Pipeline. On the right side of the screenshot, it also shows the REST endpoint for the Published Pipeline with a status of "Active".

![17 Azure Published Pipelines Overview 3](https://github.com/icenine81/Operationalizing_Machine_Learning/blob/47798a1d29f4cecf821d426726bb41302d2dcef5/Required%20Screenshots/17%20Azure%20Published%20Pipelines%20Overview%203.jpg)



###### Configure a pipeline with the Python SDK

In this screenshot, the Jupyter Notebook shows “RunDetails Widget” with the step runs that were performed. 



![18 Pipeline created with Jupyter Notebook Python SDK](https://github.com/icenine81/Operationalizing_Machine_Learning/blob/47798a1d29f4cecf821d426726bb41302d2dcef5/Required%20Screenshots/18%20Pipeline%20created%20with%20Jupyter%20Notebook%20Python%20SDK.jpg)



###### Use a REST endpoint to interact with a Pipeline

This screenshot from Azure ML studio shows that the pipeline endpoint has a Status of "Active"

![16 Azure Published Pipelines Overview 1](https://github.com/icenine81/Operationalizing_Machine_Learning/blob/47798a1d29f4cecf821d426726bb41302d2dcef5/Required%20Screenshots/16%20Azure%20Published%20Pipelines%20Overview%201.jpg)



## Link to project walk-through screencast

![youTube Link](https://youtu.be/kYGW7kUUAc0)

