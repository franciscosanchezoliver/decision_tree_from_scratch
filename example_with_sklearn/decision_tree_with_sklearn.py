import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, export_text

# Sample data

data = pd.DataFrame(
    [
        {"groaning": "yes", "eating_brains": "yes", "is_zombie": "yes"},
        {"groaning": "yes", "eating_brains": "no", "is_zombie": "no"},
        {"groaning": "no", "eating_brains": "yes", "is_zombie": "no"},
        {"groaning": "no", "eating_brains": "no", "is_zombie": "no"},
        {"groaning": "yes", "eating_brains": "yes", "is_zombie": "yes"},
        {"groaning": "yes", "eating_brains": "yes", "is_zombie": "yes"},
        {"groaning": "yes", "eating_brains": "no", "is_zombie": "no"},
    ]
)


# Encode yes/no values
le = LabelEncoder()
df_encoded = data.copy()
for col in ["groaning", "eating_brains", "is_zombie"]:
    df_encoded[col] = le.fit_transform(df_encoded[col])

# Train decision tree
X = df_encoded[["groaning", "eating_brains"]]
y = df_encoded["is_zombie"]
tree = DecisionTreeClassifier(max_depth=2)  # simple tree
tree.fit(X, y)

# Print tree rules
tree_rules = export_text(tree, feature_names=list(X.columns))
print(tree_rules)
