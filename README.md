# ![Logo](https://github.com/alyaa999/personality-test/blob/main/personality%20test.png)

The project aims to develop a prototype of a platform that  predict the personality of person using his feedback. It’s supervised type problem which will create classes of different personality traits. User will fill the feedback form and ML supervised model will analyze in which classification algorithms  (of personality traits) the user lies. 

The predictive analysis of personality assessments provides an overview of a candidate’s behavioural tendencies and that allows recruiters to really understand if a candidate will, in fact, be a top performer and if he will fit the culture of the company. Having this kind of insights before making the hiring decision is crucial to decide better!

## Table of Contents
* [Demo](#demo)
* [Prerequisites & Development Libraries](#prerequisites-development-libraries)
* [Installation](#installation)
* [Instructions](#instructions)
* [Background](#background)
* [Components of the Application](#components-of-the-application)
* [Personality Test](#personality-test)
*

## Demo 

The video below shows a live demo of how the web application works.

[Presonality Test  Video](https://drive.google.com/file/d/1vK57Axwk87LRR92NywPguKGldwTPefnm/view?usp=sharing)



## Instructions

* Clone the [repository](#installation)
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
           * pickle.dump(algorithm name, open('algorithm name', 'wb'))
        * API 
           * model_algorithm name =pickle.load(open('Path of the model on your PC' ,'rb'))
* Now run the api file that called  app.py.

