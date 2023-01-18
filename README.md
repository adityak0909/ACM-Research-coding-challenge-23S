# The Problem

### Initial Thoughts 
The moment I clicked on the Kaggle dataset, I already knew I wanted to use linear regression to predict the type of star based on other parameters. As soon as I saw the prompts provided, and the statement of coming up with our own problem to solve, I quickly switched to modeling the prediction of Spectral Class instead. Unfortunately, as I researched what goes into giving a star its spectral class, I found mainly two things- surface temperature and atmospheric pressure. The provided dataset lacks atmospheric pressure, and so I would be training a model based on a single variable, which isn't much fun. 

### Choosing the problem
Thus, I decided to go back to my original idea, and in this, I effectively removed the "Star color" column, as admittedly, I'm not too sure how to convert these categorical variables into numerical ones. Even though I know that I could use One-Hot encoding to address the categorial issue of the "Spectral Class" column, it was essentially a replica of the temperature column, and there wasn't much point to this.

# Implementing My Solution

### My previous knowledge  
I've already had experience in data science using Python, but I've personally never actually trained a machine learning model to make predictions. My knowledge of numpy, pandas, and moderate experience in Python prior to this project definitely helped. 

### Using YouTube and Stack Overflow 
The first resource I used was YouTube. After stumbling around the site clicking on difference videos, I finally landed on [this](https://www.youtube.com/watch?v=J_LnPL3Qg70&list=PLeo1K3hjS3uvCeTYTeyfe0-rN5r8zn9rw&index=3) video, in which I gained much of the knowledge I required for this project. I researched into sklearn's documentation on my own, which also helped give an understanding of exactly what I was doing. I ran into multiple problems, such as being unable to properly fit the model onto all the parameters without the ".value" addition, which wasn't in the YouTube video I watched. This, and many other problems were solved by researching on Stack Overflow. 

# Final Thoughts

### Additional Information 
I would like to mention that our predicted variable starType can be modeled using the equation y = 0.00000818955718x<sub>1</sub> + -0.0000000792628656x<sub>2</sub> + 0.000468443580x<sub>3</sub> + -0.139032098x<sub>4</sub> + 2.9207251323827137  
x<sub>1</sub> = Temperature  
x<sub>2</sub> = Luminosity  
x<sub>3</sub> = Radius  
x<sub>4</sub> = Absolute Visual Magnitude  

### What I learned & Looking to the Future
What I learned throughout this project was how to use Linear Regression on a dataset using the sklearn machine learning library. Overall, it was a super enjoyable experience, and I now understand how people are coming up with these types of things. In the future, I wish to really delve into how I can implement machine learning models using categorical data, and I would love to understand the code that goes behind the scenes in which all the data processing is done using machine learning.
