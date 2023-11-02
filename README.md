# Youtube Channels Global Analysis - Final Project 

## *Motivation*

The information networks have totally evolved and the way in which we get informed and gather data has been totally disrupted by new digital platforms as Youtube. Youtube has evolved as well from being only a video/music platform to become a the biggest social network in 2023. It is worth to examine and understand the strategy Youtube has implemented to attract content creators and viewers in ordert to position the company on the top.


## *Dataset*

The datasets used for this project are "Global_YouTube_Statistics", found on https://www.kaggle.com/datasets/nelgiriyewithana/global-youtube-statistics-2023

### **Questions and Answers**

My Final Bootcamp Project aims to answer the following questions based on exploratory data analysis (EDA) and modeling:

1. YouTube Analytics: Which are the success factors of top YouTube channels and what sets them apart from the rest?

The project includes a Power Point presentation that addresses and visualizes thoroughly these factors. 

2. Content Strategy: Which are in 2022 the most popular categories and upload frequencies that resonate with audiences?

To understand the overall viewers preferences over time, the project explores historical trends of the Youtube channels. 

3. Trending Topics: how certain categories gain popularity over time and correlate with world events?

To understand the overall viewers preferences over time, the project explores historical trends of the Youtube channels.

4. Regional Influencers: Who are the influential YouTube creators from different countries and which is their impact on a global scale?

To identify the influencers, the project creates a function that allows to create a personalized ranking per country.

5. Earnings Analysis: How does the correlation between channel performance and estimated earnings looks like?

To understand this question the project creates and visualize a correlation matrix.

6. Geospatial Visualization: How looks the distribution of successful YouTube channels on a world map like and which geographical trends can be observed?

To visualize this distribution the project includes a thorough Tableau map. 

7. Modeling: future subscribers. 

The project aims to reproduce a model able to predict future subscribers based on the clean dataset. In order to do this 3 different models are created: Linear Regression, Decision Trees, and Random Forest.


## *Challenges*

- Modified question: Model highest earnings. I try to model subscribres instead.

- The data set does not have sufficient information (granularity) as regards earnings that can be used to model earnings. 

- It is worth to keep analyzing models and columns that can be predicted with accuracy given the present data.


### Running the Project
To run this dataset onto my jupyter notebook I used "data = pd.read_csv('../data/raw/Global_YouTube_Statistics.csv', encoding=encoding) 
'encoding': 'ISO-8859-1'".
