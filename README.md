# ![Logo](https://github.com/alyaa999/personality-test/blob/main/personality%20test.png)

The project aims to develop a prototype of a platform that  predict the personality of person using his feedback. It’s supervised type problem which will create classes of different personality traits. User will fill the feedback form and ML supervised model will analyze in which classification algorithms  (of personality traits) the user lies. 

The predictive analysis of personality assessments provides an overview of a candidate’s behavioural tendencies and that allows recruiters to really understand if a candidate will, in fact, be a top performer and if he will fit the culture of the company. Having this kind of insights before making the hiring decision is crucial to decide better!

## Table of Contents
* [Demo](#demo)
* [Instructions](#instructions)
* [Background](#background)
* [Components of the Application](#components-of-the-application)
* [Personality Test](#personality-test)
* [Dataset Description](#dataset-description)
* [Team behind this piece of art](#team-behind-this-piece-of-art)

## Demo 

The video below shows a live demo of how the web application works.

[Presonality Test  Video](https://drive.google.com/file/d/1vK57Axwk87LRR92NywPguKGldwTPefnm/view?usp=sharing)



## Instructions

* Clone the [repository](https://github.com/alyaa999/personality-test.git)
* Install  Visual Studio Code
* Install Anaconda
* Install all required libraries in Aanconda
    * Matplotlib.pyplot
    * Catboost
* Install all required libraries in vscode 
    * Flask 
    * Pickle 
 * To link Model with API install pickle library
    * Anaconda
          save your model after training  as .pkl 
         ```sh
         pickle.dump(algorithm name, open('algorithm name', 'wb'))
        ```  
     * API 
        link your model.pkl with api 
         ```sh
         model_algorithm name =pickle.load(open('Path of the model on your PC' ,'rb'))
        ```
* Now run the api file that called  app.py.


## Background 

There are various tests that help to determine personality types such as the Big Five, Rorschach test, and MBTI test. In this project, prediction of personality is done by considering the MBTI test.

The MBTI personality classification system grew out of Jungian psychoanalytic psychology as a systematization of archetypal personality types used in clinical practice. The system is divided along four binary orthogonal personality dimensions, altogether comprising a total of 16 distinct persons.

### The dimensions are as follows

* Extraversion (E) vs Introversion (I): a measure of how much an individual prefers their outer or inner world.

* Sensing (S) vs Intuition (N): a measure of how much an individual processes information through the five senses versus impressions through patterns.

* Thinking (T) vs Feeling (F): a measure of preference for objective principles and facts versus weighing the emotional perspectives of others.

* Judging (J) vs Perceiving (P): a measure of how much an individual prefers a planned and ordered life versus a flexible and spontaneous life
 
 
## Components of the Application
* Sub to try machine algorithm

* home to take personality test

* Result page 


#### Candidate View Process Flow
* Test Page (page.html)

![Test Page](https://github.com/alyaa999/personality-test/blob/main/Untitled.png)


* Choose Your Model (sub.html)
![Login](https://github.com/alyaa999/personality-test/blob/main/Untitled2.png)


* famous person match with your personality (final.html)

![famous person match with your personality](https://github.com/alyaa999/personality-test/blob/main/Untitled3.png)




 ## Personality Test
Social media establishes uninterrupted connectivity, between its users and external world through revealing personal details and their viewpoints in every aspect of life. The focal aim of this here is to analyze how twitter (dataset) can be used to predict personality.
We show processes of developing  Machine Learning models on textual data. With this candidates can see their predicted personality types  according to Myers-Briggs Personality Types Indicator using their twitter user names since twitter is the classic entry point for practicing machine learning. With Twitter data, you got an interesting blend of data (tweet contents) and meta-data (location,hashtags, users, re-tweets, etc.) that opened up paths for analysis.
This training contains following topics:
* Exploratory Data Analysis
* Handling Imbalanced Dataset
* Vectorization of Text Data
* Model Creation


## Dataset Description

The publicly available personality type dataset from Kaggle, containing  rows 59998 of data, was used in this test. In this dataset, each row consists of 62 columns. The first 61 columns are for features of a given person, and the last column(result) includes 16 types of personality. 
Each feature contains answers in the Scale that we use:

* Fully Agree

* Partially Agree

* Slightly Agree

* Neutral 

* Slightly disagree

* Partially disagree

* Fully disagree

## Team behind this piece of art

- [Jamela Ahmed ](https://github.com/Jameeelaahmed)
- [Aya Abdelkhalk Ahmed](https://github.com/AyaAbdelkhalk)
- [Shimaa Mohamed Taky](https://github.com/shimaamhmd)
- [Sama Mohamed Abdelmohsen](https://github.com/Samaamhmd)
- [Alyaa Mamoon](https://github.com/alyaa999)





