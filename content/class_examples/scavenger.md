title: In-Class Exercise: Data Scavenger Hunt
tags: data, week5
date: 2019-02-13

## Pandas Filtering

Before we do our scavenger hunt, here's a piece of useful information you should know: you can filter rows of a Pandas dataframe using something that returns a boolean.

For example, suppose you have a DataFrame called copdf with police officer names in a column called "name" and the number of tickets they've written in a column called "tickets."  You could use the code `copdf[copdf.tickets>100].name` to get the names of all the cops with more than 100 tickets. (However, be careful about changing subsets of DataFrame like that---sometimes Pandas will change the original DataFrame when you make a change to a subset.  It's a good idea to [explicitly copy a dataframe](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.copy.html) before doing any changes to a subset of it that you don't want to leak into the original.) 

## A scavenger hunt.

We're going to work with houston_medicine.csv, a dataset that I've posted on ICON, and which supposedly featured in a sex discrimination lawsuit.  (n.b., this is a dataset that's been floating around the internet for a while; I can't find the original litigation; it was downloaded from [here](https://www.kaggle.com/hjmjerry/gender-discrimination/home)). 

Allegedly, the following describes the columns of the data: 

- Dept 1=Biochemistry/Molecular Biology 2=Physiology 3=Genetics 4=Pediatrics 5=Medicine 6=Surgery

- Gender 1=Male, 0=Female

- Clin 1=Primarily clinical emphasis, 0=Primarily research emphasis

- Cert 1=Board certified, 0=not certified

- Prate Publication rate (# publications on cv)/(# years between CV date and MD date)

- Exper # years since obtaining MD

- Rank 1=Assistant, 2=Associate, 3=Full professor (a proxy for productivity)

- Sal94 Salary in academic year 1994

- Sal95 Salary after increment to 1994

**Everyone should go look for the following information.  When everyone has found everything, we'll go round getting code, running it on the main screen, and discussing.** 

Some of the questions are deliberately ambiguous. Try to make an assumption about what I mean, but take note of when you do so, and we'll talk about the ambiguity afterward.

1.  How many observations are there in the dataset? 

2.  What can you say about the distribution of salaries?  Does it look like the standard bell-shaped curve that we all know and love?  If not, why not? 

3.  What are the mean, median, and mode of salaries?  How do they change from year to year?  

4.  What data visualization would you use to get a look at the relationship between gender and salaries? What do we learn from that visualization? 

5. Can we subdivide the dataset in some useful way to get more insight about the relationship between gender and salaries under different conditions?  Come up with something that helps us learn more, and visualize it.

6.  How many people in the dataset make more than 450k a year?  What else do we know about them? 

7.  How many standard deviations away from the mean is the most highly-paid person in the dataset?  What about the lowest person?

8. What's the biggest department?  The smallest?  Can you order them from largest to smallest?

9.  What's the most highly paid department?  What's the lowest paid department? What measure did you use to make that decision, and could a different measure have yielded different results?

10. Competition time: what's the most fancy data visualiation you can come up with to make of these data?  What's the most informative? (What would you want to know?)

Finally, what do you think you would want to know in order to figure out whether there's evidence of discrimination in this dataset.  What would your next steps be?  Come to some idea. 

