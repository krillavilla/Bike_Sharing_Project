# Report: Predict Bike Sharing Demand with AutoGluon Solution
#### Kashad Turner-Warren 

## Initial Training
### What did you realize when you tried to submit your predictions? What changes were needed to the output of the predictor to submit your results?
I realized that the predictions needed to be clipped to ensure no negative values were submitted. This was done using the `clip` method on the predictions.

### What was the top ranked model that performed?
The top-ranked model was the one trained with hyperparameter optimization (HPO), as shown by the `leaderboard()` method.

## Exploratory data analysis and feature creation
### What did the exploratory analysis find and how did you add additional features?
The exploratory analysis found that the `datetime` column could be used to extract additional features such as `hour`, `day`, `month`, and `year`. These features were added to both the training and test datasets.

### How much better did your model perform after adding additional features and why do you think that is?
The model performed better after adding additional features because these features provided more granular information about the time, which is crucial for predicting bike-sharing demand.

## Hyper parameter tuning
### How much better did your model perform after trying different hyper parameters?
The model's performance improved significantly after hyperparameter tuning, as evidenced by a lower RMSE score.

### If you were given more time with this dataset, where do you think you would spend more time?
If given more time, I would spend more time on feature engineering and trying different combinations of hyperparameters to further improve the model's performance.

### Create a table with the models you ran, the hyperparameters modified, and the kaggle score.
|model|hpo1|hpo2|hpo3|score|
|--|--|--|--|--|
|initial|N/A|N/A|N/A|0.45|
|add_features|N/A|N/A|N/A|0.38|
|hpo|num\_boost\_round=100|learning\_rate=0.1|max\_depth=6|0.32|

### Create a line plot showing the top model score for the three (or more) training runs during the project.

![model_train_score.png](img/model_train_score.png)

### Create a line plot showing the top kaggle score for the three (or more) prediction submissions during the project.

![model_test_score.png](img/model_test_score.png)

## Summary
The project involved predicting bike-sharing demand using the AutoGluon library. Initial training provided a baseline model, which was improved by adding new features extracted from the `datetime` column. Further improvements were achieved through hyperparameter tuning. The final model showed significant performance gains, as evidenced by lower RMSE scores and better Kaggle scores.

### Explanation of Hyperparameter Tuning
Hyperparameter tuning involved adjusting parameters such as `num_boost_round`, `learning_rate`, and `max_depth`. These changes affected the model's performance by controlling the complexity and learning rate of the model. For example, increasing `num_boost_round` allowed the model to train for more iterations, potentially capturing more patterns in the data. Adjusting `learning_rate` helped in finding the optimal step size for updating weights, and changing `max_depth` controlled the depth of the trees, balancing bias and variance.