# K-means Cluttering with Quantum Annealing Applied to Electoral Redistricting



## Introduction
The past few presidential elections have faced tons of scrutiny with allegations of unfair voting practices, unfair access to voting centers, and racially-discriminatory electoral districts. If we were able to just have a computer decide district lines for us, could we potentially eliminate or, at least, ameliorate some of these criticisms? 

In this project, we used k-means clustering and D-Wave’s Leap hybrid Discrete Quadratic Model (DQM) solvers to find the optimal voting population distribution to prevent gerrymandering practices taken by government agencies.


## Motivation/Goals for the Project

Gerrymandering is the practice of redrawing geopolitical district boundaries to give an unfair advantage to a political party in elections. 

Our goal was to use the well-known method of k-means clustering and D-Wave’s Leap hybrid solver to prevent gerrymandering practices. Using population information from census data over the counties of a state, we are able to suggest best practices for districting in elections. 

We wanted to take quantum computing and demonstrate its applicability in topics that affect not just scientists and engineers, but the general public. 



## Description of the Work

We began with construction of a k-means clustering method for clusters of equal sizes. 

Using census data from the GitHub repository CensusData, which takes record of all previous years’ census for all US states and territories, we are able to import data from specific districts and make use of k-means for proper division of populations to be considered in elections. 


## Proposals for Future Work

* Create a website/front-end interface for users to interact with the data
* Code a function that automates the collection of the geographic data




## References
[https://arxiv.org/pdf/2008.02369.pdf](QUBO Formulations for Training Machine Learning
Models)
* Include more factors that may come into play with a realistic setting, i.e. more current geopolitical data, socioeconomic status, education, etc.

Other applications:
* We can apply our k-means clustering algorithm in fields of potent research interest, including solid state/condensed matter physics, etc, but we have demonstrated the ability to include statistical data for usage in economics, political science, etc. 
