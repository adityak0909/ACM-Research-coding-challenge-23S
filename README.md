# The Problem

### Initial Thoughts 
The moment I clicked on the Kaggle dataset, I already knew I wanted to use linear regression to predict the type of star based on other parameters. As soon as I saw the prompts provided, and the statement of coming up with our own problem to solve, I quickly switched to modeling the prediction of Spectral Class instead. Unfortunately, as I researched what goes into giving a star its spectral class, I found mainly two things- surface temperature and atmospheric pressure. The provided dataset lacks atmospheric pressure, and so I would be training a model based on a single variable, which isn't much fun. 

### Choosing the problem
Thus, I decided to go back to my original idea, and in this, I effectively removed the "Star color" column, as admittedly, I'm not too sure how to convert these categorical variables into numerical ones. Even though I know that I could use convert each color to a number to address the categorial issue of the "Spectral Class" column, it was essentially a replica of the temperature column, and there wasn't much point to this.

# Implementing My Solution

### My previous knowledge  
I've already had a little experience in data science using Python, but I've personally never actually trained a machine learning model to make predictions. My limited knowledge of pandas and basic understanding of Python prior to this project definitely helped. 

### Using YouTube and Stack Overflow 
The first resource I used was YouTube. After stumbling around the site clicking on difference videos, I finally landed on [this](https://www.youtube.com/watch?v=J_LnPL3Qg70&list=PLeo1K3hjS3uvCeTYTeyfe0-rN5r8zn9rw&index=3) video, in which I gained much of the knowledge I required for this project. Furthermore, I also used [this](https://www.youtube.com/watch?v=VCJdg7YBbAQ&list=LL&index=2&t=2653s) video to use sklearn's train_test_split on the dataset. I researched into sklearn's documentation on my own, which also helped give an understanding of exactly what I was doing. I ran into multiple problems, such as a linear regression model not being able to use sklearn's accuracy_model, which wasn't in the YouTube video I watched. This, and many other problems were solved by researching on Stack Overflow. 

### How I trained a machine learning model to predict star type  
Using the second video mentioned, I created my independent and dependent variables using all columns other than Star type and categorical variables as X, and only the Star type as Y. Using sklearn's library, I created a linear regression model, and fit the training data gained from train_test_split to the regression model. After gaining the predictions to find the R<sup>2</sup> value, I printed out the regression model's coefficients, y-intercept, and the R<sup>2</sup> score.

<img width="677" alt="Screenshot 2023-01-18 at 6 08 24 PM" src="https://user-images.githubusercontent.com/88306051/213325704-6a669f70-73c2-426f-bd38-4ced2ee9e505.png">


# Final Thoughts

### Additional Information 
I would like to mention that our predicted variable starType can be modeled using the equation y = 0.0000152482590x<sub>1</sub> + -0.000000385217577x<sub>2</sub> + 0.000544613271x<sub>3</sub> + -0.136426009x<sub>4</sub> + 2.906325081589083  
x<sub>1</sub> = Temperature  
x<sub>2</sub> = Luminosity  
x<sub>3</sub> = Radius  
x<sub>4</sub> = Absolute Visual Magnitude  

In addition, our equation can be used to understand how each factors affect the resulting star type. Based on our equation, the factors that have the highest influence on star type are Absolute Visual Magnitude and Radius.

Furthermore, it seems that the maximum accuracy of around 92% is gained when using exactly 75% of the dataset. As we increase or decrease the dataset used for the model, our accuracy decreases.

This project overall took me about 120-150 minutes to complete.

### What I learned & Looking to the Future
What I learned throughout this project was how to use Linear Regression on a dataset using the sklearn machine learning library. Overall, it was a super enjoyable experience, and I now understand how people are coming up with these types of things. In terms of this project, I would have loved to implement a visualization of the linear regression equation, but I'm unfortunately completely unfamiliar with any graphing libraries. In the future, I wish to really delve into how I can implement machine learning models using categorical data, and I would love to know why exactly 75% of the dataset renders the highest accuracy.
