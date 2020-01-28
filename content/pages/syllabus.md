title: Syllabus
save_as: index.html

# Introduction to Quantitative & Computational Legal Reasoning  (LAW:8645)

Spring 2020; Monday + Tuesday 2:00-3:30; Classroom 265.

Professor: Paul Gowder 

- Office: 408

- Email: paul-gowder@uiowa.edu

- Phone: 319-384-3202

- Office Hours: Mon., Tue. 11am-1pm, and by appointment

Assistant: Diana DeWalle 

- Office: 469

- Email: diana-dewalle@uiowa.edu 

- Phone: 319-335-9036

## Welcome

Welcome to Introduction to Quantitative and Computational Legal Reasoning, informally named "Sociological Gobbledygook" in honor of [Chief Justice Roberts's slightly math-phobic remark at oral argument in Gill v. Whitford](https://fivethirtyeight.com/features/the-supreme-court-is-allergic-to-math/).  This course is offered at the University of Iowa College of Law in Spring 2020, by [Paul Gowder](https://gowder.io), and has previously been offered in Spring 2019: you can go look at [last year's syllabus]({filename}../archive/syllabus-2019.md) if you're curious.  For a little bit more about the motivation for the course, you can check out the [manifesto]({filename}manifesto.md).

This is a totally open-source course. There is a [Github repository](https://github.com/paultopia/gobbledygook) which contains all of our materials and discussions. Please feel free to make a suggestion or start a conversation in the issues, or even make a pull request. For unstructured navigation of this website, you can use the [list of tags](/tags.html** that describe the subject matter of our lessons.

**Note**: If you're accessing this syllabus in PDF form on ICON, some of the links may not work, and it may not be fully updated. The canonical syllabus will always appear in HTML form on [https://sociologicalgobbledygook.com](https://sociologicalgobbledygook.com). Much of the language below (like "this website") assumes that you are accessing the syllabus from there.

## Course Summary

This course will review basic principles of probability, statistics, and computational reasoning (including elementary programming) for law students. Throughout, the emphasis will be on mathematically modest intuition, practical skills, and legal applications. No mathematical background beyond high school algebra will be assumed.

This course is not advised for students with substantial statistical or computational backgrounds---it is designed as a beginner course. Nor will it prepare students to be competent empirical researchers or computer programmers---the goal is to give students the capacity to critically evaluate and understand statistical reasoning, and to use computational methods to do so (as well as in their legal practices more generally). Focus will be on breadth rather than depth, as well as legal applications.

Introduction to Quantitative and Computational Legal Reasoning is experimental. This syllabus is not a contract; I reserve the right to make radical changes in how the course operates throughout the semester, depending on how student learning progresses. (However, as this is version 2 of the course, you can expect the changes to be a bit less radical compared to last year.)

## Course Resources

- Course website: [https://sociologicalgobbledygook.com/](https://sociologicalgobbledygook.com/) 

- [Course Github repository](https://github.com/paultopia/gobbledygook/) 

Note that lessons are downloadable directly from this website, including (where lessons are in that format) Jupyter notebooks that you can execute on the IDAS service (about which below), but also in PDF. 

## Readings 

### Texts

The main readings for this course will be on this website.  There may be a little bit of copyrighted stuff that I can't distribute publicly on ICON.

In addition, there will be supplemental readings drawn from [Charles Severance, Python for Everybody](https://www.py4e.com/book), which is available for free online, and [Michael Finkelstein & Bruce Levin, Statistics for Lawyers](https://link.springer.com/book/10.1007%2F978-1-4419-5985-0) which should be free to download as PDF through our library's subscription. (You may have to be on the campus network to download it; you might also have to search for it through the library's directory.) We will also be using some excerpts from the [Federal Judicial Center's Reference Manual on Scientific Evidence](https://www.fjc.gov/content/reference-manual-scientific-evidence-third-edition-1) 

We'll make use of some videos and exercises online. We'll talk more about this on the first day, but I will be assigning you mini-online-introductory courses to do in order to get practice with programming, from [Dataquest](https://dataquest.io)'s free tier (maybe) and from [Hackerrank](https://www.hackerrank.com/) and [Project Euler](https://projecteuler.net/). You'll want to grab accounts at those places.

We will also use some free instructional materials from the nonprofit organizations [Software Carpentry](https://software-carpentry.org/lessons/) and [Data Carpentry](https://datacarpentry.org/lessons/). 

For the contents of this website, it's probably easiest to access them using the week-by-week links below or the [content-based tags](tags.html) built into this website. There might be formatting glitches with some of the lessons, due to conversion between different file types and html, but every lesson will have a link to a downloadable and printable PDF at the bottom which will ordinarily have cleaner formatting (except for long lines of code, which may be cut off in PDF but should be fine on web).  Some lessons should also have downloadable Jupyter notebooks associated with them, which will also be linked at the bottom.


### Bonus Reading Suggestions

I am committed to only assigning resources which are free to students. However, the nature of this material is that sometimes one explanation will just "click" where another might not.  So in addition to the assigned readings, I offer you this list of additional, non-free, readings which you might consult for a different perspective on the material---or for deeper engagement and exploration.  

#### Statistics

I really like the Aspen textbook by Lawless, Robbennolt and Ulen, [Empirical Methods in Law](http://www.aspenlawschool.com/books/empirical_methods/). It has very good clear explanations of a number of research methods topics, and is not overly math-y. If you want to dig deeper into stats and empirical research in law, I highly recommend it.  I also recommend Lee Epstein & Andrew Martin, [An Introduction to Empirical Legal Research](https://global.oup.com/academic/product/an-introduction-to-empirical-legal-research-9780199669066?cc=us&lang=en&). 

If you want to do serious research on your own, you will need to move to more advanced texts, but the direction you go will depend on the particular kind of research you want to conduct. For expermental research, especially experimental research out in the world (like the kinds of things done by discrimination testers, about which we will talk), a classic text is Gerber & Green [Field Experiments: Design, Analysis and Interpretation](https://global.oup.com/academic/product/an-introduction-to-empirical-legal-research-9780199669066?cc=us&lang=en&); if you are more interested in observational research, I really like Angrist & Pischke, [Mastering Metrics](http://masteringmetrics.com/). Both of those books are rather-more math-y than the others (or our class).

Charles Wheelan, *Naked Statistics: Stripping the Dread from the Data*, is a well-liked book on the other end of the spectrum---it focuses on intuitive and non-math-y explanations of statistics topics. It's quite good in that respect, but I'm not fully comfortable recommending it for other reasons. The author thinks he's funnier than he actually is, and the book features a number of fairly tasteless, and in some cases offensive, jokes. If you can put up with that, however, the book is good at explaining stats in a clear way.

Some other books that might be of interest to you, though I haven't reviewed them as closely and hence can't clearly endorse, include:

- Peter Bruce & Andrew Bruce, Practical Statistics for Data Scientists

- Michael A. Bailey, Real Stats: Using Econometrics for Political Science and Public Policy

- Uri Bram, Thinking Statistically

#### Python Programming

My favorite introductory Python book (not free) is John Guttag, [Introduction to Computation and Programming Using Python](https://mitpress.mit.edu/books/introduction-computation-and-programming-using-python-revised-and-expanded-edition).  This book is also the basis for a wonderful electronic [course by almost the same name from MIT on EdX](https://www.edx.org/course/introduction-to-computer-science-and-programming-using-python) --- and you can go through the course for free, and without buying the book.  I really do think that course (and the second course in the same series) is an amazing way to learn Python, and programming in general.

Blessedly, there are a lot of good introductory Python programming books out there which are also available online for free. One of my favorites is Al Sweigart, [Automate the Boring Stuff with Python](https://automatetheboringstuff.com). For more advanced (and non-free) learning, I really love Luciano Ramalho's [Fluent Python](http://shop.oreilly.com/product/0636920032519.do), although by the time you need that you should be looking at building fairly substantial programs. 

It is better to use a Python book that is based on Python 3, not Python 2. 

#### General Learning

I highly recommend Barbara Oakley's book [A Mind for Numbers](https://barbaraoakley.com/books/a-mind-for-numbers/), which is basically a self-help book on the psychology of learning difficult things---which can help you not just in math-y classes but in law school and other classes in general. There's an online course based on her book on Coursera, called [Learning How to Learn](https://www.coursera.org/learn/learning-how-to-learn); I've never looked at that course but everyone who has done so has raved about it. 

## How Class Will Go

This course is structured as a vaguely "flipped" lab-style process. You will largely consume the talking-ish "content" kind of instruction outside of the classroom, primarily through readings. In classroom time, I will demonstrate the practical usage of the things you've learned about outside of class, maybe do a teeny tiny and (more commonly) assign exercises for you to carry out, with the opportunity to work together to figure them out and with me looming over your shoulder to help. 

Please bring a computer to every class. Mac, Linux, or Windows computers will work best. Chromebooks and tablets will work less well, though we can get them to work if need be. 

The coverage, pace, and workload in this class will be a continuing work in progress. Because this class isn't taught a lot in law schools, there is not much collective wisdom on how to do it successfully, and I expect to have to adapt the assignments and the pace to accommodate how readily the class takes to the material. So don't expect the syllabus to stay stable as we move through the course. 

## Class technological resources

This class will use the University's [Interactive Data Analytics Service](https://its.uiowa.edu/interactive) (IDAS).  You do not need to request access to this, I've made arrangements to get accounts for the whole class, and I'll walk you through getting access to this resource on the first day of class. (You can also see the links on the bottom of this page.)

In addition, every session will be recorded on Panopto; and we'll use ICON to  and distribute materials which (for copyright reasons, etc.) we're not allowed to distribute outside of the class. Also, you will use the discussion feature of ICON to share information and ask questions out of class.

This class is intended in part to produce resources which will be available to the legal profession at large in order to help your fellow lawyers understand code and stats as well; accordingly, many of the reading assignments will be to lessons posted on this website at sociologicalgobbledygook.com. Those assignments will also be available on the course GitHub repository; you will find it useful to get the assignments there in order to execute and mess around with the code yourself. I'll explain how GitHub works on the first day of class too.


## Evaluation

Evaluation will be primarily based on four problem sets. The first two will be computer programming-based (with the second possibly including a probability problem or two), and will be worth 17.5% of the grade each. The third will be probability and statistics based and will be worth 25% of the grade.  The fourth will be comprehensive, with emphasis on the statistics side, and will be worth 30% of the grade.

The weird fractions are to accommodate 10% of the grade which will be based on classroom participation and preparation, and which is meant to enforce the lab-style classroom format. Students who get full credit for that 10% will complete the simple out-of-class tasks which I will periodically assign and participate in good faith in collective problem-solving in the classroom. (This is an effort-based 10%, not a performance-based 10%.) 

Under the policy described in Student Handbook section B.3 ("The curve is not applicable in upper-level seminars and other upper- level classes in which a student's grade is based primarily on the student’s performance on graded skills-oriented tasks (including writing) other than a final exam."), this course will not be curved.

In order to ensure that students in this course aren’t disadvantaged by unfamiliarity with the format or a collection of too-hard problem sets on which everyone struggles, there will be a floor for the distribution of grades for this course: at the lowest, the median grade for this course will be the official law school median of 3.3. In other words, you can’t do worse than the standard curve would otherwise dictate. But you can do better. 

Last year's problem sets are available on this website, along with answers to them; looking them over will give you an idea of the approximate challenges that you'll be asked to complete.

All problem sets will be turned in via email to Diana Dewalle. The only place your name should appear in problem sets is in the filename.

### Collaboration

Problem sets should be your own work. You are allowed to discuss the general approach to problem sets with one another, but you are not allowed to show one another your math or code. 

For example: "I solved that problem by writing a loop over the list of cases" is acceptable. "Look at this code I wrote" is not. 

Students will be asked to agree to an honor code.

Collaboration on in-class tasks and on homework assignments that are not one of the official problem sets is highly encouraged and probably necessary. However, you should try to do the homework assignments on your own first before consulting with your classmates, in order to maximize your learning. (Struggle and frustration are normal, expected, and healthy.)

## Technology, Bugs, and Accommodations

This course will be technologically driven, obviously. Please let me know ASAP if there are any glitches of any kind.

Also, please contact me or the dean of students as soon as humanly possible if you need accommodations, so that these accommodations can be built into the tech. All course materials will be provided in formats that I believe are accessible (e.g., to screen readers), however, if I'm mistaken about their accessibility, please let me know and the problem will promptly be fixed.

## Office Hours, Contacts, etc.

I will maintain office hours (Mon., Tue. 11am-1pm, and by appointment). I'm also happy to make appointments at other times, and you're always free to drop by when my door is open. I'm very good at replying to e-mail and very bad at checking telephone messages.

That being said, I **very strongly encourage you to ask substantive questions in a way that will be accessible to your fellow students**.  This means using the copious time that will be made available in class time for that purpose, as well as making use of the discussion forum on ICON (in which I will very actively participate).  If you have a question, it's almost certainly the case that several other people do too.

## Some schedule notes

Spring Break is March 14-22. No class then, obviously. 

Problem sets are due on the following Fridays, each at 5pm Central: Feb 7 (week 3), Feb 28 (week 6), Apr. 3 (week 10) and May 8 (in the middle of finals period).


### Learning outcomes

By the end of the course, you should be able to:

- Write simple Python scripts to automate common tasks and explore data

- Visualize data, and understand basic data visualizations 

- Understand common errors made in empirical research and quantitative claims, and identify those errors in published and expert reports.

- Conduct basic statistical analyses.

- Reason about probability and statistics at a sufficient level to be an informed consumer of quantitative claims.

- Identify the confusions in the following, from oral argument in [Department of Commerce v. New York](https://www.scotusblog.com/case-files/cases/department-of-commerce-v-new-york/): 

![embedded image: Justice Gorsuch makes a statistical oops]({filename}../images/gorsuch.png)

## Coverage by Week

The first few weeks will be spent on computation; subsequent weeks will be spent on data analysis and statistics. As we get further into the future, the below becomes more subject to change, obviously. 

### Week 1 (Jan 21)

Coverage: Basic ideas of programming, units of computation, functions and loops. Computational logic and legal logic, law as computation. We will front-load the quantity of reading a little heavily to get us started quickly, but it'll ease off as we move on to more conceptually difficult material. (Also, I know the reading seems like a lot, but it goes faster than cases in 1L year!)  In particular, don't feel obliged to fully absorb everything from Python for Everybody on the first reading. Just read it quickly so you get a feel for the terrain, and then more carefully read the stuff posted on this site, then dig back into Python for Everybody to fill out the details.

Read: 

- the [Introduction to Python on this site]({filename}../Lessons/python_intro.md) 

- the [first Python lesson]({filename}../Lessons/basic_intro.ipynb). 

- [functions and scope]({filename}../Lessons/functions.ipynb)

- [more loops and control flow]({filename}../Lessons/control_flow.ipynb)

- [simple data types]({filename}../Lessons/simple_data_types.ipynb)

- [complex data types]({filename}../Lessons/complex_data_types.ipynb)  

- Software Carpentry lesson on [functions](https://swcarpentry.github.io/python-novice-inflammation/08-func/index.html) 

- Software Carpentry lesson on [making choices](https://swcarpentry.github.io/python-novice-inflammation/07-cond/index.html)

- the [Software Carpentry lesson on loops](https://swcarpentry.github.io/python-novice-inflammation/04-loop/index.html)

- pages 1-55 of Python for Everybody. 

Like I said, I know this is a lot of reading. Don't worry, there won't be nearly so much as we move forward. 

In the first day of class, we will get everyone set up with the different services and installation options for the software we need in the course, and, if there's time, demonstrate some basic programming ideas and work through some exercises.


For **Week 1 practice homework**, do the "Introduction" problems (click the introduction checkbox on the right of the screen) in the [HackerRank Python Domain](https://www.hackerrank.com/domains/python).

I'd also like you to complete the factorial exercise at the end of the [first Python lesson]({filename}../Lessons/basic_intro.ipynb); you don't need to turn it in, but let me know if you can't complete it; we'll look at people's solutions next week and use this as our test to make sure everyone is set up and functional.

**Here is the [in-class notebook]({filename}../class_examples/Day12020.ipynb) that we saw on day 1.**  


### Week 2 (Jan 27, 28)

Coverage: using Python to get access to other people's code, libraries. Accessing the filesystem and the internet from Python. Error handling. Strings.

Readings:

- Python for Everybody pg. 55-126 

- [my brief notes from week 1 in 2019]({filename}../Lessons/post-week1-notes.md) (some of this may be a little obsolete, like references to some of the specific resources we used last year, such as Microsoft Azure).

- [Libraries]({filename}../Lessons/libraries.md)

- [Errors]({filename}../Lessons/errors.ipynb)

- [Files and Strings]({filename}../Lessons/files-and-strings.ipynb)

- [Network Requests]({filename}../Lessons/network_requests.md)

In class on Tuesday for this week last year we worked through an example of accessing the Openstates API. We'll probably do that exercise again this year, and when it's done you can take a look at [the example here]({filename}../class_examples/openstates_example.ipynb).

For **Week 2 practice homework**, do the "Basic Data Types" problems (click the Basic Data Types checkbox on the right of the screen) in the [HackerRank Python Domain](https://www.hackerrank.com/domains/python), *except* the "List Comprehensions," and "Lists" problems, which you can skip (we'll try to do those in class).

**Here are our in-class notebooks for week 2**: [Jan 27 (Monday)]({filename}../class_examples/Jan27.ipynb) and [Jan 28 (Tuesday)]({filename}../class_examples/Jan28.ipynb). The due dates for the first two problem sets have also changed, and this change is reflected on the page you're looking at.  I've also moved around the practice homework a bit.

### Week 3 (Feb 3, 4)

Coverage: Regular expressions. Simulation and why you might want to do it. A very light introduction to object-oriented programming. (But we're a little behind and so we'll start this week with the networking and API stuff from last week.)

Readings: 

- Automate the Boring Stuff With Python chapter [6 (strings)](https://automatetheboringstuff.com/chapter6/)

- Automate the Boring Stuff With Python chapter [7 (regular expressions)](https://automatetheboringstuff.com/chapter7/) 

- Python for Everybody pp. 127-140 and 171-184 (chapters 11 and 14). 

- [Regular Expressions]({filename}../Lessons/regex.ipynb)

- [Object-Oriented Programming]({filename}../Lessons/oop.ipynb)

- [Simulations]({filename}../Lessons/simulation.md)  

For **Week 3 practice homework**, go to the "Strings" problems in the [HackerRank Python Domain](https://www.hackerrank.com/domains/python) and do: 

- "sWAP cASE"

- "String Split and Join"

- "Mutations"

- "Find a string"

- "String Validators" 

- "Text Wrap" and 

- "Capitalize!"

### Week 4 (Feb 10, 11)

Basic probability math. Bayes rule and conditional probability.

Focused legal applications: probabilistic causation in torts, junk science in criminal trials.

Readings: 

- the [Arbital Guide to Bayes Rule](https://arbital.com/p/bayes_rule/?l=1zq) (at the beginning, where it asks you to pick a level of depth, choose the full/deep presentation)

- [Probability]({filename}../Lessons/probability.md)

- Chapter 3 (pp. 61-100) of the Finkelstein and Levin Book. [Direct link to F&L assignment via UI Library Proxy Server](https://link-springer-com.proxy.lib.uiowa.edu/chapter/10.1007/978-1-4419-5985-0_3) 

- After reading the F&L assignment read [Abel and Baker Redux]({filename}../Lessons/abelbaker.md)

- (video) Peter Donnelly's TED talk [How Statistics Fools Juries](https://www.ted.com/talks/peter_donnelly_shows_how_stats_fool_juries)

- NBC News ['We are going backward': How the justice system ignores science in the pursuit of convictions](https://www.nbcnews.com/news/us-news/we-are-going-backward-how-justice-system-ignores-science-pursuit-n961256)

- A note from last year on a [week 4 recap/further explanation of the probability issue the class that year got stuck on]({filename}../Lessons/totalprob.md)

**[Problem set 1]({filename}../psets/pset1-2020.md) due Friday, February 14, at 5pm Central time.****

See last year's [Problem set 1]({filename}../archive/pset1.md), which you can do for practice if you'd like.  After doing that practice, you can check out [my answers to it]({filename}../archive/pset1_answers.ipynb).

No week 4 practice homework because the problem set is due.



### Week 5 (Feb 17, 18)

Initial explorations into data with data visualization in Python. Basic properties of data, measures of central tendency, exploratory data analysis.

Reading: 

- [Introduction to stats]({filename}../Lessons/intro-stats.md)

- [Key Python Data Libraries]({filename}../Lessons/key-libraries.ipynb)

- [Exploring data]({filename}../Lessons/exploratory_intro.ipynb)

- [Common Data Transformations]({filename}../Lessons/data-transformations.ipynb)

- [Federal Judicial Center Manual on Scientific Evidence](https://www.fjc.gov/content/reference-manual-scientific-evidence-third-edition-1) pp. 236-240

- Finkelstein & Levin [chapter 1](https://link-springer-com.proxy.lib.uiowa.edu/chapter/10.1007/978-1-4419-5985-0_1) (pp. 1-45)

- Explore the different data visualizations available with [From Data to Viz](https://www.data-to-viz.com/)

- Skim over the following two Data Carpentry lessons, paying special attention to the parts about Pandas (and ignoring the parts about SQL and visualization libraries, except insofar as they involve Pandas): 

    - [Data Analysis and Visualization in Python for Ecologists](https://datacarpentry.org/python-ecology-lesson/) 
  
    - [Data Analysis and Visualization with Python for Social Scientists](https://datacarpentry.org/python-socialsci/)

- (TBD: other Pandas tutorial material)

- [Week 5 recap from last year.]({filename}../Lessons/week5recap.md)

For **Week 5 practice homework**, do the "Errors and Exceptions" problems in the [HackerRank Python Domain](https://www.hackerrank.com/domains/python), then go to the "Regular Expressions and Parsing" section and do: 

- "Detect Floating Point Number"

- "Re.split()"

- "Validating phone numbers"

- "Validating and Parsing Email Addresses"


### Week 6 (Feb 24, 25)

Probability distributions, central limit theorem, hypothesis testing. 

Reading: 

- [Distributions]({filename}../Lessons/distributions.ipynb)

- [The Normal Distribtion]({filename}../Lessons/normal_clt.ipynb)

- [Hypothesis Testing]({filename}../Lessons/hypothesis-testing-intro.md)

- [a Catalogue of Basic Hypothesis Tests]({filename}../Lessons/basic_hypothesis_tests.ipynb)

- Finkelstein & Levin, pp. 101-126

- [A Concrete Introduction to Probability using Python](https://nbviewer.jupyter.org/url/norvig.com/ipython/Probability.ipynb) by Google's director of research,

- these two excellent blog posts by a Google data scientist: 

    - [Statistics for People in a Hurry](https://towardsdatascience.com/statistics-for-people-in-a-hurry-a9613c0ed0b) 
    
    - [Never Start With a Hypothesis](https://towardsdatascience.com/hypothesis-testing-decoded-for-movers-and-shakers-bfc2bc34da41)

For **Week 6 practice homework**, do the "Debugging" problems in the [HackerRank Python Domain](https://www.hackerrank.com/domains/python)

### Week 7 (Mar 2, 3)

Experiments, random assignment.  Causation and correlation.  Focused legal application: audit tests in discrimination cases.

Readings: 

- [Causation and Counterfactuals]({filename}../Lessons/causation_counterfactuals.md)

- Devah Pager, *The Use of Field Experiments for Studies of Employment Discrimination: Contributions, Critiques, and Directions for the Future*, 609 Annals of the American Academy of Political and Social Science 104 (2007). We have access to this article via our library's subscription, [this proxy link](https://journals-sagepub-com.proxy.lib.uiowa.edu/doi/abs/10.1177/0002716206294796) should work to download it.

- The Open Introduction to Statistics pp. 19-26. This book can be [downloaded for free](https://www.openintro.org/stat/textbook.php), but I will probably post an excerpt of the relevant parts on ICON (remind me!).

- [A collection of edited discrimination tester cases]({filename}../Lessons/tester-cases.md)



**Problem set 2 due Friday, March 6, at 5pm Central time.**

[See last year's problem set 2]({filename}../archive/pset2.md), which, as before, you should do for practice; afterward you can [look at my answers]({filename}../archive/pset2_answers.ipynb).


### Week 8 (Mar 9, 10)

Focus week: statistical extrapolation and simulation in the law. Shonubi case. 

Readings: 

- [United States v. Shonubi]({attach}../images/shonubi.pdf) (Edited version kindly supplied by Josh Fischman of UVA.)

- Commentary on Shonubi, posted on ICON

We'll spend this week catching up further, if necessary, discussing the Shonubi case, and replicating the data analysis used by experts in that case (approximately---we don't have quite the identical dataset).  As time permits, I'll introduce the basic concepts of linear regression for next week.

For **Week 8 practice homework**, do the [Multiples of 3 and 5](https://projecteuler.net/problem=1) and [Smallest multiple](https://projecteuler.net/problem=5) problems on Project Euler. (Note, you don't need to submit code on that site, just write the code to get the correct math answer.)

### Week 9 (Mar 23, 24)

Regression analysis. Linear regression. Statistical evidence of discrimination.

Readings: 

- [Regression Introduction]({filename}../Lessons/regression-intro.ipynb)

- Federal Judicial Center reference manual on scientific evidence, appendix to reference guide on multiple regression, pp. 333-356

- F&L pg. 369-371, bottom of 376-380, bottom of 385-393

- Lindsey Kuper, [Understanding the regression line with standard units](http://composition.al/blog/2018/08/31/understanding-the-regression-line-with-standard-units/)

- [ATA Airlines, Inc. v. Federal Express Corp.]({attach}../images/ata_v_fedex.pdf), 665 F.3d 882 (7th Cir., 2011), as edited

- [Post week 9 notes from last year]({filename}../Lessons/post-week9-notes.md)

For **Week 9 practice homework** do [Even Fibonacci numbers](https://projecteuler.net/problem=2) from Project Euler.  Also, look at the hypothetical dataset *mickel.csv*, and use the techniques we've learned in class to come to some conclusion about whether discrimination is occurring in the provision of public benefits in this disability services agency context. We'll go over this assignment in class at an appropriate time.

### Week 10 (Mar 30, 31)

Applications and reinforcement. Slow-down week, solidify our existing knowledge by thinking about a concrete use of statistics in law: determining disparate impact in Title VII cases.

Readings: 

- [Stewart v. St. Louis]({attach}../images/stewart.pdf)

- [Ricci v. DeStefano excerpts]({attach}../images/ricci.pdf)

- [Excerpts from 29 C.F.R. 1607]({attach}../images/29cfr1607.pdf) for reference/skim, no need to carefully read the whole thing

**Problem Set 3 due Fri, Apr. 3, at 5pm Central.**  

See [last year's problem set 3]({filename}../archive/pset-3.md).

### Week 11

P-values, p-hacking, publication bias, the replication crisis in psychology, power and underpoweredness, multiple comparisons, and other terrible pitfalls of scientific research.  

Readings:

- [P-Values and Bayes Rule]({filename}../Lessons/pvals2.md)

- [Power]({filename}../Lessons/power.md)

- Peter Norvig's blog post [Warning Signs in Experimental Design and Interpretation](http://norvig.com/experiment-design.html)

- [Statistics Gone Wrong](https://www.statisticsdonewrong.com/). I'd like you to read that whole website eventually, but for the beginning of the week, you can focus on the sections on:

    - [Statistical Power and Underpowered Statistics](https://www.statisticsdonewrong.com/power.html) 
    
    - [The P Value and the Base Rate Fallacy](https://www.statisticsdonewrong.com/p-value.html)  

- Fun reading: [P-values explained with puppies](https://hackernoon.com/explaining-p-values-with-puppies-af63d68005d0)

Discussion: what are the legal implications of scientific failures?

For **Week 11 practice homework** do [Power Digit Sum](https://projecteuler.net/problem=16) from Project Euler.  This will be the last of our practice homeworks, as I know that you're going to start freaking out about exams by now.

### Week 12

How regression analysis can go horribly wrong.  Assumptions of regression.  Failures of regression assumptions. Simpson's paradox.

Readings: 

- [Regressions gone wrong]({filename}../Lessons/regression_problems.ipynb)

- Federal Judicial Center reference manual, reference guide on multiple regression, pp. 303-332

- The following two blog posts/tutorials by "Statistics by Jim": 

    - [Confounding Variables](https://statisticsbyjim.com/regression/confounding-variables-bias/)
    
    - [Classical Assumptions of OLS](https://statisticsbyjim.com/regression/ols-linear-regression-assumptions/)


### Week 13

Focus week: statistics, probability and legal proof.  Bayesian approaches. 

This week will be seminar-style.  There will be some reading from academic articles, and Professor Sullivan will come and join us for Monday to talk through probability and proof.  On Tuesday, we will continue the discussion, and perhaps do an exercise, as time permits. 

Reading: 

**For Monday***

- Jonah Gelbach, *Estimation Evidence* (posted on ICON), pages 1-31 

- Sean Sullivan, [A Likelihood Story: The Theory of Legal Fact-Finding](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2837155) p. 11-37

**For Tuesday***

- Kiel Brennan-Marquez, [Plausible Cause](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2827733)

- [The Bayesian New Statistics: Hypothesis testing, estimation, meta-analysis, and power analysis from a Bayesian perspective](https://link-springer-com.proxy.lib.uiowa.edu/article/10.3758%2Fs13423-016-1221-4), 25 Psychonomic Bulletin and Review 178 (2018) (You may skip the sections entitled "Bayesian Hypothesis Test" and "Another example of frequentist and Bayesian approaches to hypothesis testing and estimation" from pp. 186-190  

- Optional bonus reading: I've added [a more basic-level explanation of some of the ideas in the above article]({filename}../Lessons/confidence-and-bayes.ipynb) to this website


### Week 14

Look at real-life expert witness reports, how arguments about quantitative methodology are used in court.

From statistics to machine learning: what is it that fancy data science people actually do with their time?  Prediction vs inference. Algorithmic accountability. Discrimination by computer, and legal implications of statistical discrimination (intentional racial profiling and unintentional racial profiling). 

Reading: 

- Example expert witness reports: excerpts from one plaintiff and one defendant report in ongoing litigation around Harvard admissions (a claim that they discriminate against Asian-Americans). On ICON.  Note: these documents are a bit choppy, as I tried to edit the PDFs to limit it to a handful of points of contention by deleting pages, so ignore any discontinuities. Please come to class prepared to comment on one question in particular: should any data analysis include people admitted as legacies or athletes? 

- [Prediction vs. Inference]({filename}../Lessons/prediction.md)

- Galit Shmueli, ["To Explain or to Predict?"](https://projecteuclid.org/euclid.ss/1294167961), Statistical Science 2010. (skim)

- Harini Suresh and John V. Guttag, ["A Framework for Understanding Unintended Consequences of Machine Learning"](https://arxiv.org/abs/1901.10002) 

Optional, bonus (but HIGHLY recommended) reading:

- Adam M. Lauretig and Bear F. Braumoeller, ["Statistics and International Security,"](http://www.oxfordhandbooks.com/view/10.1093/oxfordhb/9780198777854.001.0001/oxfordhb-9780198777854-e-10) in The Oxford Handbook of International Security (2018) 

- Andrew D. Martin, Kevin M. Quinn, Theodore W. Ruger, and Pauline T. Kim. ["Competing Approaches to Predicting Supreme Court Decision Making."](https://deepblue.lib.umich.edu/bitstream/handle/2027.42/116229/pop04.pdf?sequence=1&isAllowed=y) Perspectives on Politics 2004


### Final exam period

**Problem set 4 due on Friday, May 8, during the exam period, at 5pm Central.**

See [last year's problem set 4]({filename}../archive/pset4.md) and [a makeup assignment the class did]({filename}../archive/makeup-assignment.md). 
