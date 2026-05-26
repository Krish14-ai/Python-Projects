# 🌲 Interactive Decision Tree Dashboard

## Overview
This project is an interactive web application built with Streamlit that visualizes how a Decision Tree machine learning algorithm makes predictions. It allows users to adjust hyperparameters in real-time and immediately observe the impact on both the tree's mathematical structure and the importance of specific dataset features. 

Currently, the dashboard uses the classic Wine dataset to classify different types of wine based on their chemical properties.

## Features
* **Real-time Hyperparameter Tuning:** Adjust `Max Depth`, `Min Samples to Split`, and the splitting `Criterion` (Gini vs. Entropy) using an intuitive sidebar.
* **Dynamic Visualizations:** * **Tree Logic Diagram:** See the exact mathematical thresholds and splits happening under the hood.
  * **Feature Importance Chart:** A dynamic bar chart that shifts as the model's parameters change, highlighting which variables drive the model's decisions.
* **Instant Feedback:** The model accuracy metric updates automatically with every parameter tweak.

## Tech Stack
* **Python** (Core Logic)
* **Streamlit** (Web Interface)
* **Scikit-Learn** (Model Training & Tree Extraction)
* **Matplotlib & Pandas** (Data Manipulation & Plotting)

## How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Krish14-ai/Interactive-Decision-Tree-Dashboard.git](https://github.com/Krish14-ai/Interactive-Decision-Tree-Dashboard.git)
   cd Interactive-Decision-Tree-Dashboard
   
2.**Install Libraries:** 
   ```bash
    pip install streamlit scikit-learn pandas matplotlib
```
3.**Run the app:**
 ```bash
  streamlit run app.py
