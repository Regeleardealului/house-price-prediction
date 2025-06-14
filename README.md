# House Price Estimator

This project delivers a robust solution for predicting house prices, encompassing data preparation, model development, web application creation, and deployment using modern cloud technologies. Key Accomplishments:

### ✅ Data Preparation & Analysis
* **Dataset Utilization:** Leveraged the widely recognized `house-price-dataset` from Kaggle.
* **Rigorous Preprocessing:** Implemented essential preprocessing steps, including:
    * **Feature Encoding:** Transformed categorical features into numerical representations.
    * **Feature Scaling:** Standardized numerical features to optimize model performance.
* **Statistical Validation:** Applied advanced statistical tests to ensure data quality and model reliability:
    * **Shapiro-Wilk Test:** Assessed the normality of data distributions.
    * **Variance Inflation Factor (VIF):** Identified and addressed multicollinearity among features.
    * **Interquartile Range (IQR):** Detected and managed outliers to enhance model accuracy.

### ✅ Model Development
* **Linear Regression Model:** Developed and meticulously fine-tuned a Linear Regression model.
* **Exceptional Performance:** Achieved an impressive R² value of **97%**, demonstrating excellent predictive accuracy and model fit.
* **Model Serialization:** Serialized the production-ready model using `pickle` for seamless integration and deployment.

### ✅ Web Application
* **Intuitive User Interface:** Designed and developed a user-friendly web application using Flask, complemented by HTML and CSS, to provide an accessible interface for making house price predictions.
* **Dependency Management:** Ensured reproducibility and ease of setup with a comprehensive `requirements.txt` file, documenting all project dependencies.

### ✅ Containerization & Deployment
* **Docker Integration:** Containerized the entire application using Docker, enabling consistent environments across different platforms.
* **Docker Hub Publication:** Published the Docker image to Docker Hub, making it readily available for public access.
    * **Pull Command:** `docker pull regeleardealului/house-price-estimator`
* **Google Cloud Deployment:** Successfully deployed the containerized application on Google Cloud using the Google Cloud SDK.
* **Live Application:** The live application is accessible at: [https://house-price-predictor-190261199531.us-central1.run.app/](https://house-price-predictor-190261199531.us-central1.run.app/)
