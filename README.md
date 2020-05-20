# Breast-Cancer-Detection
The program initally implements the use of Gradient Boosting & displays which features are most important or have the most effect on whether or not an individual has Breast Cancer on a model. The code also implements Machine Learning with the use of a Convolutional Neural Network to detect Breast Cancer. Tensorflow is also incorporated in the project as well. Sci-kit libraries' Breast Cancer dataset was used to accomplish this project.

**Step 1)** 

The first step is importing the necessary libaries we need.

![CancerImport](https://user-images.githubusercontent.com/60532479/82481861-fb055980-9aa3-11ea-9c7d-7f41be8e0ab1.png)


**STEP 2)**

Load the breast Cancer dataset from the SciKit library.

![Cancer1](https://user-images.githubusercontent.com/60532479/82482182-6ea76680-9aa4-11ea-9025-66076ef24555.png)


**STEP 3)**

Use Gradient Boosting and train your data to visualaze the effectiveness of it on the dataset.

![Cancer2](https://user-images.githubusercontent.com/60532479/82493202-8d622900-9ab5-11ea-9bef-e2ecaedd4989.png)


**STEP 4)**

Plot the dataset's most important features and view which features have the greatest impact when it comes to Breast Cancer. In this case, worst concave points have the biggest importance on our dataset.

![Cancer3](https://user-images.githubusercontent.com/60532479/82493431-f34eb080-9ab5-11ea-98a0-606eb9abfe88.png)

![Cancer4](https://user-images.githubusercontent.com/60532479/82494341-69074c00-9ab7-11ea-887f-9da82d61e9be.png)


**STEP 5)**


Set up the dataframe and analyze the data by calling X back.

![Cancer5](https://user-images.githubusercontent.com/60532479/82495200-c059ec00-9ab8-11ea-9752-bcc78219eab5.png)


**STEP 6)**

Take a look at how much data is currently contained by checking the shape of X.

![Cancer6](https://user-images.githubusercontent.com/60532479/82495471-234b8300-9ab9-11ea-91e4-d5795b1d6981.png)


**STEP 7)**


Take 80% of data into a training set and the other 20% into a test set.

![Cancer 7](https://user-images.githubusercontent.com/60532479/82495762-99e88080-9ab9-11ea-9844-5f8e41b284d8.png)

**STEP 8)**

Confirm the sizes of the training and test datasets are in fact an 80/20 split.

![Cancer8](https://user-images.githubusercontent.com/60532479/82496073-209d5d80-9aba-11ea-83f5-e62ab0200330.png)

**STEP 9)**

Scale and shape the data into a 3 dimensional array for usability.

![Cancer9](https://user-images.githubusercontent.com/60532479/82496543-ee403000-9aba-11ea-8695-d5daa6bb86b2.png)


**STEP 10)**

Develop the model while implemnting the use of a Convolutional Neural Network. Take a look at the model afterwards. 


















