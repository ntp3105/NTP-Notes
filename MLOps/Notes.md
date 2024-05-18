https://www.qwak.com/post/mlops-pipeline-with-open-source-tools
# 5 Best Open Source Tools to Build End-to-End MLOps Pipeline in 2024
The tools discussed include **Feast** for __feature management__, **MLflow** for __model tracking__ and __versioning__, **Seldon** for __model deployment__, **Evidently** for __real-time monitoring__, and **Kubeflow** for __workflow orchestration__.

## Why Production-Grade ML is Different

-   **Dynamic vs Static**: Unlike experimental ML, which often uses fixed datasets, production environments are dynamic. They require systems that can adapt to fluctuating user demand and data variability.
-   **Inelastic Demand**: User requests in production can come at any time, requiring a system that can auto-scale to meet this inelastic demand.
-   **Data Drift**: Production systems need constant monitoring for changes in data distribution, known as data drift, which can affect model performance.
-   **Real-Time Needs**: Many production applications require real-time predictions, necessitating low-latency data processing.

## The Traditional Machine Learning Setup

In a traditional machine learning setup, the focus is often on experimentation and proof-of-concept rather than production readiness. The workflow is generally linear and manual, lacking the automation and scalability required for a production environment. 

Let's break down what this traditional setup usually entails, using a Credit Risk prediction model as an example:

*   **Data preprocessing** and **feature engineering** are typically done in an ad-hoc manner using tools like Jupyter notebooks. There's usually __no version control for the data transformations or features__, making it __difficult to reproduce results__.
*   The model is **trained** and **validated** using the same Jupyter notebook environment. **Hyper-parameters** are often __tuned manually__, and the training process __lacks systematic tracking of model versions__, __performance metrics__, or __experiment metadata__.
*   Once the model is trained, **predictions** are __run in batch mode__. This is a __manual step__ where the model is applied to a dataset to generate predictions, which are then saved for further **analysis** or **reporting**.
*   The prediction results, along with any model artifacts, are __manually saved to a data storage service__, such as a cloud-based data store. There's usually __no versioning or tracking__, making it __challenging to manage model updates or rollbacks__.