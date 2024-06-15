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

![Fig 1: Traditional ML model development.](images/1.png)
Fig 1: Traditional Machine Learning Setup

## The Journey from Notebooks to Production: An Integrated ML System
MLOps aims bridges the gap between a model in a Jupyter notebook and a full-fledged, production-grade ML system. This notes focusses more on how specific open-source tools can be orchestrated to create a robust, production-ready ML setup. Although we won't be discussing Kubernetes in detail, it's worth noting that the architecture we explore can be deployed on container orchestrators like Kubernetes for further scalability and robustness.

![Fig 2: Integrated ML model ssytem.](images/2.png)
Fig 2: Integrated ML model ssytem

## Why MLOps Open Source Tools 

Open-source tools in MLOps offer a high degree of **flexibility** and **customization**. This is particularly beneficial for teams with unique or evolving requirements that may not be well-served by a one-size-fits-all solution. Open-source tools allow you to tailor the software to meet the specific needs of your ML projects, whether it’s modifying the code to add new features or integrating with existing systems and tools.\

A key benefit of open-source MLOps tools is **cost-effectiveness**. Many of these tools are free or incur minimal costs, making them accessible to organizations of all sizes. This can be particularly advantageous for startups and smaller teams with limited budgets.\

**Integration capabilities** are another strong point of open-source MLOps tools. They are often designed to work well within a heterogeneous technology ecosystem, providing connectors and APIs for seamless integration with a variety of data sources, machine learning frameworks, and deployment environments.\

Lastly, using open-source tools can offer significant opportunities for **learning** and **skill development**. Teams working with these tools are exposed to the latest technologies and practices in the field. This hands-on experience is invaluable for professional growth and staying abreast of the rapidly evolving MLOps landscape.\

## Managed MLOps Platforms

Provide a more **streamlined** and **integrated approach**. These platforms are typically easier to set up and use, offering a comprehensive suite of tools and services designed to work together seamlessly. This can significantly reduce the complexity and time involved in managing ML operations, making it an attractive option for teams with limited operational expertise or those looking to simplify their workflow.

The decision between open-source tools and managed platforms depends on various factors, including the size and expertise of your team, budget constraints, specific project requirements, and long-term strategic goals.

In the next sections, we’ll explore the five most important MLops Open-Source Tool categories:
## 1. Data Management and Feature Engineering

Managing and engineering features for machine learning models with a feature store, ensuring that they are consistently managed, stored, and served.
### What is a Feature Store?

A **feature store** is a centralized repository that acts as a bridge between raw data and machine learning models. It streamlines the feature engineering process and ensures consistency across different models. Feature stores can be broadly categorized into two types:

    **Offline Feature Store** - is primarily used for batch processing of features. It's where you store historical feature data that can be used for training machine learning models. The offline store is optimized for analytical workloads, allowing you to query large volumes of data efficiently.

    **Online Feature Store** - serves features in real-time for model inference. When a prediction request comes in, the online feature store quickly retrieves the relevant features to be fed into the model. This is crucial for applications that require low-latency predictions. Online feature stores are often backed by high-performance databases like Redis to ensure quick data retrieval.

### Considerations When Adopting an Open Source Feature Store Solution

    1. Data Processing Infrastructure
    2. Offline and Online Storage
    3. Monitoring Infrastructure

### Open source feature stores
1. Feast: https://feast.dev/
2. Hopsworks: https://www.hopsworks.ai/open-source-hopsworks
 