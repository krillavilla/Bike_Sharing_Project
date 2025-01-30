import matplotlib.pyplot as plt

# Data for training runs
training_runs = ["initial", "add_features", "hpo"]
train_scores = [0.45, 0.38, 0.32]

# Data for Kaggle submissions
kaggle_submissions = ["submission1", "submission2", "submission3"]
kaggle_scores = [0.68432, 0.65217, 0.63891]

# Create line plot for training runs
plt.figure(figsize=(10, 5))
plt.plot(training_runs, train_scores, marker='o', linestyle='-', color='b')
plt.title('Top Model Score for Training Runs')
plt.xlabel('Training Runs')
plt.ylabel('Score')
plt.grid(True)
plt.savefig('/home/krillavilla/Documents/AWS_Machine_Learning_Udacity/Bike_Sharing_Project/img/model_train_score.png')
plt.show()

# Create line plot for Kaggle submissions
plt.figure(figsize=(10, 5))
plt.plot(kaggle_submissions, kaggle_scores, marker='o', linestyle='-', color='r')
plt.title('Top Kaggle Score for Prediction Submissions')
plt.xlabel('Kaggle Submissions')
plt.ylabel('Score')
plt.grid(True)
plt.savefig('/home/krillavilla/Documents/AWS_Machine_Learning_Udacity/Bike_Sharing_Project/img/model_test_score.png')
plt.show()