# INFO-6105- DATA SCIENCE ENG METHODS FINAL PROJECT
# Walk_Run_Image_Prediction
Data Science Project Using Convolution Neural Network(CNN)

**Summary**
Image classification is a fundamental task in the field of computer vision, enabling machines to categorize and interpret visual content. The "Walk or Run Image Prediction" project focuses on developing a machine learning model capable of distinguishing between images depicting a person walking and a person running. This project holds significance across domains like surveillance, health monitoring, sports analysis, and more.

**Definition of the Problem**
The primary objective of this project is to build a predictive model that can accurately classify images as either "walking" or "running." Given an input image, the model's task is to determine the activity portrayed by the person in the image. This problem falls under the category of binary image classification, where the target variable is binary, indicating whether the image features a walking or running activity.

**Rationale of Target Variable Selection**
Looking at the Training Dataset we can see the images have classes assigned to either Walk or Run. We can see that the images represent Running or Walking, hence we will classify an image to be a walk or run. i.e, Target variable is to classify image as Walk or Run.

**Suitable Machine Learning Approach**
For this problem we have used three machine learning algorithms, we concluded that Convolutional Neural Networks (CNNs) using Inception V3 architecture are the most suitable machine learning algorithm.
The other two ML algorithm that we used is Random Forest Classifier and Logistic Regression

**Conclusion**
In conclusion, the "Walk or Run Image Prediction" project addresses a significant task in computer vision. Among the machine learning algorithms considered, Convolutional Neural Networks (CNNs) emerged as the most suitable choice, achieving an impressive accuracy of 81.56%. In comparison, the Random Forest Classifier with default parameters exhibited an accuracy of 47.51% and with tunned hyperparameters it gives as accuracy of 48.22% whereas Logistic Regression with default parameters approach achieved an accuracy of 48.9% and with tunned hyperparameters it gave accuracy of 58.15%. These results underscore the superior performance of CNNs in tackling the intricate task of accurately categorizing 'walking' and 'running' images.

**Scope for Future Work**
As with any data science project, there are several opportunities for future work and improvement.
Some potential directions include:
Using different CNN architectures: Experimenting with various CNN architectures, hyperparameters, and regularization techniques to optimize model performance.
Other deep learning methods: Using other deep learning methods with high accuracy. Ensemble Methods: Combining predictions from multiple models or architectures to boost accuracy and reliability.

**Developed User Interface**
We've designed an intuitive user interface using Streamlit, allowing users to effortlessly upload an image. Once uploaded, the system performs an instantaneous analysis on the image, promptly delivering a conclusive output indicating whether the depicted activity is 'walk' or 'run'.
Here's a look of the frontend:

![image](https://github.com/pradhanmona7/Walk_Run_Image_Prediction/assets/114325852/86bf219d-0b39-49cd-a7f9-a707a94f7008)

![image](https://github.com/pradhanmona7/Walk_Run_Image_Prediction/assets/114325852/fae9ea89-5968-4c89-8100-f00e7cbb1042)


