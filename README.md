# Automated Depression Detection

 
Overview
Depression is a type of mood illness characterised by a continuous sense of melancholy and a loss of interest.
Time-bound life is prevalent in today's culture. People who can’t adopt this type of environment, experience tension and mental depression as a result of this. Mental depression is becoming more common all around the world. The saddest part of this problem is that many of them are completely unaware that they are depressed while also being terrified of doctors.
In this critical situation, intelligent software that can detect depression automatically will be extremely beneficial to humanity.

The Problems
The majority of people are unaware that they are depressed. They simply accept the situation and consider it normal behaviour.
In our society, mental illness is considered taboo.  People fear or dislike going to visit the doctor(psychiatrist) or discussing their mental health in public.

Project Objective
It would be ideal if the software or an app could instantly detect whether or not someone is depressed. It would overcome both concerns by raising awareness and reducing doctor apprehension.
Target Audience
At least three audiences must be targeted in order to enhance the lives of people with mental illnesses:
Government legislators 
Those who have or may have mental health issues
The general public

Dataset Description
The data set “emotions.csv”, which is available on the Kaggle website, was used in this study. It has 2549 columns and 2132 rows. The first 2548 columns comprise independent attributes taken from the EEG (Electroencephalogram) brainwave data, such as mean, standard deviation, Fast Fourier transformation, min and max values, Eigenvalues, entropy, and so on. The dependent attribute label is represented by the last column, which has three classes: positive, negative, and neutral. There are 716 neutral values, with 708 in each of the positive and negative classifications.
Methodologies: Dimensionality Reduction
The dataset contains too many variables which makes it difficult to work with. To make it a little bit simpler we are using some dimensionality reduction techniques.

PCA
Principal Component Analysis, or PCA, is a dimensionality-reduction approach for reducing the dimensionality of large data sets by transforming a large collection of variables into a smaller one that retains the majority of the information in the large set.


Methodologies: Classification
SVM
A support vector machine, or SVM, is a supervised learning technique that can be used to solve issues like classification and regression.
It is, however, mostly employed to solve categorization difficulties. The purpose of SVM is to generate a decision boundary or hyperplane that can divide datasets into multiple classes.

Support vectors are the data points that assist define the hyperplane, hence the algorithm is called a support vector machine.

	

Methodologies: Interface Design
It is very important to make sure that, this kind of software reaches the masses. So we are developing it as platform-independent software. As the whole project is built upon python, so we are using Tkinter framework for our development.

Experimentation
Applying PCA
Applying Principal Component Analysis, or PCA dimensionality is reduced from 2132 x2548(excluding the ‘label’ column) to 2132x316. This reduction costs only 2% of data loss i.e 98% of information is preserved.

Applying SVM
We have applied SVM on dimensionally reduced data. We have trained our model using 70% of that information i.e. using approximately 1492 records. And rest 30% of the data is used to test our model.

Fine Tuning the Algorithm
To improve accuracy we have tuned the Regularization parameter, i.e. we have tuned the margin of the hyperplane.
App Development
As we have used python for our project, it becomes obvious to use  Tkinter framework to build the App interface. It contains two pages or frames. One is for Login and another is for a dashboard.
Result
After successful completion, our project is going to give an accuracy of greater than 97%


Conclusion
We've reached the conclusion of our project on Automated Depression Detection. We did our best to include all of the important elements pertaining to the provided topic. We got part of the information for the project from the internet, and we also referenced certain books. This project includes information on Automated Depression Detection, Machine Learning Algorithms, and their applications, among other things. We hope that our endeavour will be entertaining as well as educational.
