title: Last Problem Set! (Pset 4)
tags: psets
date: 2019-04-02

Due Thursday, May 9, at 5pm Central time. This is an **absolutely firm** deadline, as it is the last day of the exam period. 

As before, please turn in your answers in a single notebook, emailed to Diana Dewalle. 


## "Problem" (not really a problem) 1: Help Next Year's Students (15 points)

1.A. (10 points).  I've centralized the course repository in [a new (well, newly public) github repository](https://github.com/paultopia/gobbledygook).  You created a github account at the begnning of this course.  Use that account to file an issue, making a suggestion about the content of this course that will be helpful to students in future iterations of this course. 

1.B. (5 points).  Make at least one constructive comment on someone else's suggested change in the github issues. 

1.C. (5 bonus points) For five bonus points, create a pull request that actually implements the change.  Github has lots of tutorial material on how to make a pull request. Figuring out how to do this might be a bit of a hassle, so you should consider this optional/bonus. 

NOTE: problem 1 will be graded pass/fail: if you make any kind of serious and substantive suggestion/comment, you get full points. In order to preserve the anonymity of the rest of the grading for this problem set, do not report anything about your github suggestions on the notebook that you turn in for the rest.  

Also, **in order to give everyone enough time to make a constructive comment (1.b), suggestions (1.a.) will be due a week before the rest of the pset, i.e., on May 2.**

## Problem 2: Resampling Ricci (30 points) 

Let's go back to the Ricci v. DeStafano case and associated dataset we examined in week's 10-11 (on the class server as NewHavenData.csv ---although you shouldn't actually need the dataset for this problem).  

The case excerpt we have includes information about how many applicants of each of the three racial groups took the examination, how many passed, and how many were eligible for selection, for each of the two ranks for which tests were given.  

2.A. (10 points) Use simulation to draw a large number of random samples, with replacement, of the appropriate size (i.e., the number passing, the number eligible for promotion), from a pool with the appropriate number of test-takers of each race. Report the probability of getting passing and eligible-for-selection pools with the number of passing/eligible white applicants that were observed for each test. This means you should do four simulations, and report four probabilities: the probability of getting at least X white passers of the captain's test (where X is the number of white passers in the actual Ricci case), the probability of getting at least Y white people eligible for promotion to captain, and then the equivalent numbers for lieutenant.

2.B. (10 points) Characterize the results of 2.A. in statistical as well as legal terms. Have we learned anything from that simulation exercise? What have we learned? Could that result be useful in disparate impact inquiries? How? (Hint: think about Shonubi.)

2.C. (10 points) Now consider a *fair* test (defined as one where the likelihood of passing doesn't depend on race). Simulate a fair test with the parameters (passing rate, racial distribution of the test-takers) given in the case. You need only do this for the lieutenant's exam, and only for passing the test (not for ultimately being eligible for selection under the n+2 rule). Use your simulation to calculate the probability of a fair test violating the EEOC's 4/5 rule, and explain what your results mean for the utility of that rule in cases like this.

## Problem 3: Shirt Identification Redux (30 points)

On ICON, I've posted days 4 and 5 of the trial transcript for the case that I mentioned on April 2, where a defendant was convicted on the basis of shirt-matching evidence (sorry it's a little blurry). Day 4 has direct examination of the key witness, beginning on transcript page 922, including the critical testimony about the shirts.  Day 5 begins with cross examination of that witness. 

3.A. (15 points) In a paragraph or two, tell me some things that defense counsel should have tried to elicit from this witness or highlight in cross-examination (or closing argument, as appropriate) about the shirt matching.  If you feel extra-ambitious, write a question or two, but this is not required. (Remember, I'm not particularly a trial-ey person, so I won't have very high or strict standards here, I just want you to think about stuff that the defense lawyer should found some way to bring to the jury's attention.) 

3.B. (15 points) Now change roles: as the prosecutor, suppose you believe that the shirts actually match. What additional research would you ask your expert to do in order to have more defensible evidence of that match? (Hint: such research should also be capable of showing you evidence that you're wrong, i.e. that the shirts don't match.)

## Problem 4: Discrimination Deep Dive (25 points)

The course server contains two datasets: `greiner_ipc.csv` and `greiner_nhc.csv`.  Together, they represent the relevant data for a simulated employment discrimination case (created by Jim Greiner of Harvard Law School, hence the filenames); the two files represent the datasets for two distinct committees within an employer that are responsible for employee selection and promotion (an internal promotions committee and a new hire committee).  On ICON, I have posted a collection of material about this simulated case, including codebooks describing the data, stipulated facts describing the underlying situation, and so forth. 

Come to the most well-supported conclusion that you can reach, given the techniques you've learned in this course, about whether employment discrimination (disparate intent or disparate impact) has occurred. Defend your conclusion. 
