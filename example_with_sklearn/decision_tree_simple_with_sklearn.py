import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.preprocessing import LabelEncoder
import numpy as np

# Sample data

data = {
    "groans_per_minute": [12, 0, 3, 15, 0, 7, 20, 5, 2, 17, 9, 1, 14, 6, 13],
    "eye_color": [
        "red",
        "blue",
        "green",
        "blue",
        "green",
        "red",
        "blue",
        "green",
        "red",
        "green",
        "blue",
        "red",
        "green",
        "blue",
        "red",
    ],
    "has_bite_marks": [
        "yes",
        "no",
        "yes",
        "unknown",
        "no",
        "yes",
        "unknown",
        "no",
        "yes",
        "yes",
        "no",
        "unknown",
        "no",
        "yes",
        "unknown",
    ],
    "is_zombie": [1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1],
}


df = pd.DataFrame(data)

# Handle missing values: fill with "unknown"
df["has_bite_marks"].fillna("unknown", inplace=True)

# Encode categorical features
le_eye_color = LabelEncoder()
le_bite = LabelEncoder()

df["eye_color_enc"] = le_eye_color.fit_transform(df["eye_color"])
df["has_bite_marks_enc"] = le_bite.fit_transform(df["has_bite_marks"])

# Features and target
X = df[["groans_per_minute", "eye_color_enc", "has_bite_marks_enc"]]
y = df["is_zombie"]

# Train decision tree
clf = DecisionTreeClassifier(max_depth=4, random_state=42)
clf.fit(X, y)

# Display tree structure
tree_rules = export_text(clf, feature_names=list(X.columns))
print(tree_rules)
