# decision_tree_from_scratch
Repo with a tutorial that tells you how to build a decision tree from scratch


# Structure

## What is a Decision Tree?

Ideas, points:
- A decision tree uses a tree structure to represent a number of possible decision paths
and an outcome for each path.
- Decision trees have a lot to recommend them:
  - They are very easy to understand and interpret -> the process by which they reach a prediction is completely transparent.
  - Can easily handle a mix of numeric and categorical attributes.
  - Can classify data for which attributes are missing.
- Finding an optimal decision tree for a set of training data is computationally a ver hard problem -> try to build a good-enough tree rather than an optimal one.
- Its very easy (and very bad) to build decision trees that are overfitted to the training data, and that don't generalize well to unseen data.
- We can divide decision trees into classification trees (produce categorical outputs) and regression trees (which produces numeric output).
- For the explanation, we'll focus on classification trees, and we'll work through the ID3 algorithm for learning a decision tree from a set of labeled data, this will help us understand how decision trees work. And we'll restrict the problem to binary ones.
