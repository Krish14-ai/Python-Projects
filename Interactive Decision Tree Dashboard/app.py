import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier, plot_tree

# 1. Page Configuration
st.set_page_config(page_title="Decision Tree Explorer", layout="wide")
st.title("🌲 Interactive Decision Tree Dashboard")
st.markdown("Adjust the hyperparameters on the left to see how the model's logic and feature priorities change.")

# 2. Load Data (Using the Wine dataset for classification)
@st.cache_data
def load_data():
    data = load_wine()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data.target
    return df, data.target_names, data.feature_names

df, target_names, feature_names = load_data()

# 3. Sidebar - Hyperparameter Controls
st.sidebar.header("Model Hyperparameters")
max_depth = st.sidebar.slider("Max Depth", min_value=1, max_value=10, value=3)
min_samples_split = st.sidebar.slider("Min Samples to Split", min_value=2, max_value=20, value=2)
criterion = st.sidebar.selectbox("Criterion (Split Quality)", ["gini", "entropy"])

# 4. Train the Model
X = df.drop(columns=['target'])
y = df['target']

clf = DecisionTreeClassifier(
    max_depth=max_depth, 
    min_samples_split=min_samples_split, 
    criterion=criterion,
    random_state=42
)
clf.fit(X, y)
accuracy = clf.score(X, y)

st.sidebar.markdown("---")
st.sidebar.metric(label="Model Accuracy", value=f"{accuracy:.2f}")

# 5. Dashboard Layout (Two Columns)
col1, col2 = st.columns(2)

with col1:
    st.subheader("Feature Importance")
    st.markdown("Observe how the Gini importance shifts as you restrict the tree's depth.")
    
    # Calculate and plot feature importance
    importances = clf.feature_importances_
    feat_imp_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
    feat_imp_df = feat_imp_df.sort_values(by='Importance', ascending=True)
    
    fig_bar, ax_bar = plt.subplots()
    ax_bar.barh(feat_imp_df['Feature'], feat_imp_df['Importance'], color='skyblue')
    ax_bar.set_xlabel('Importance Score')
    st.pyplot(fig_bar)

with col2:
    st.subheader("Tree Logic Diagram")
    st.markdown("The mathematical splits happening under the hood.")
    
    # Plot the actual tree
    fig_tree, ax_tree = plt.subplots(figsize=(12, 8))
    plot_tree(
        clf, 
        feature_names=feature_names, 
        class_names=target_names, 
        filled=True, 
        rounded=True, 
        ax=ax_tree,
        fontsize=10
    )
    st.pyplot(fig_tree)
