# Trending YouTube Dashboard

Author: Natalie Cho

## Welcome!
Thank you for visiting my repository for my dash app! This document (README.md) will contain a link to the milestone proposal that explains more about the project purpose and motivation and also contains usage instructions for my dash app. You can either scroll down or click from the links below to jump to a specific section:

* [Project Proposal](#project-proposal)
* [Usage](#usage)
* [Dataset Used](#about-the-dataset)
* [Dashboard Breakdown](#dashboard-features)



## Project Proposal 
[Link to Group 20 Milestone Proposal](https://github.com/UBC-MDS/trending_youtube_viz_R/blob/main/reports/proposal.md)

## Usage
*To view the app via Render:*

[Click this link!](https://trending-youtube-dashboard.onrender.com/)
(Please allow the link some time to load)

*To run the app locally:*
- Clone this repository to your computer
- In a new terminal window, navigate to the repository folder
- Install and activate the environment stored in the environment.yml file 
```
$ conda env create -f environment.yml
```
```
$ conda activate trending_youtube_DASHboard_env
```
- Run the app in the terminal window
```
$ python src/app.py
```
- Copy and paste the server link provided to you in the terminal window to your web browser to view the app! (The app should run quicker locally than using the render link above)

## About the Dataset

Youtube. (2023). YouTube Trending Video Dataset (updated daily) [Data set]. Kaggle. https://doi.org/10.34740/KAGGLE/DSV/5003820 Note: As we are based in Canada, we are using data extracted from videos that were trending in Canada due to file size limitations and for ease of loading/extraction. However, given the flexibility of our web app, it can be easily extended to YouTube data from other countries.

## Dashboard Features

**Bar Chart**

Video creators might be curious about which genre of videos are the most popular. This chart provides insight into how many videos are posted within a specific genre within a specified time period.

**Box Plot**

Now that we know how many videos of a specific genre get posted with a time period, a more important question is how long does a video take to get to trending after being published? This boxplot breaks down by genre the statistics associated with the length of time between posting and trending date per genre, given a specific time frame.
