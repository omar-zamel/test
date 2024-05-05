import pandas as pd
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv("brandnew_reduced_fraud_detection_dataset.csv")
data


# In[12]:


from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

df = data

# Selecting numeric columns for PCA
numeric_cols = ['amount', 'is_fraud', 'age', 'income', 'debt', 'credit_score']
X = df[numeric_cols]

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Perform PCA
pca = PCA()
pca.fit(X_scaled)

# Extracting importance of components
importance_components = pd.DataFrame(pca.explained_variance_, columns=['Standard deviation'])
importance_components['Proportion of Variance'] = pca.explained_variance_ratio_
importance_components['Cumulative Proportion'] = importance_components['Proportion of Variance'].cumsum()

print(importance_components)


# In[ ]:




