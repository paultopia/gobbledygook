title: Problem Set 1 
tags: psets
date: 2018-01-16

This problem set is worth 17.5% of the grade in this course. It is due on Friday, February 1, at 5pm, via a dropbox in ICON that I shall set up for the purpose. 

There are three problems on this set, one relatively small/easy one worth 20 points, and two large/difficult ones worth 40 points each; the large problems also contain alternative versions that can be done for half credit.  Subsequent problem sets will probably have more problems in them. 

**How to turn in this problem set**: each of the problems asks you to write a single Python function which carries out a designated operation.  You should include working code for each of these functions in a single Jupyter Notebook file, entitled `lastname_ps1.ipynb` (obviously with your last name), which you will turn in to the dropbox on ICON.

- For each of the problems, you need not package all of your code in a single function. For example, you may write helper functions, import libraries outside of your function, etc.  However, you must turn in a single Jupyter Notebook file with all the code that makes your functions work as well as the functions themselves.  I expect to be able to run all the cells in the notebook you turn in, and, at the end, have a working function for each problem, so that I can call those functions with appropriate input and get the correct result. In all cases, your functions should return `None` if they receive inappropriate input. 

## HONOR CODE

Each student must agree to the following honor code; if you do not agree to this honor code, do not turn in this problem set and drop the course. 

*I will not solicit, receive, or provide any unauthorized assistance on this or any problem set in this course. I understand that unauthorized assistance includes seeing the work of any other student, including code, calculations, data analysis, or answers to problems. Students are permitted to discuss their general strategies for solving problems with one another, help one another understand lesson material or documentation for Python libraries, and the like, or other conversation short of sharing actual answers, calculations, data analysis, or code. Students are not permitted to seek or receive assistance or advice whatsoever from any person not enrolled in this course---this prohibition includes asking for help on public online forums such as stackoverflow.com, although students are free to search such websites and learn from preexisting discussions in which they are not participants.*

*If I have any doubt about the permissibility of any kind of assistance, I will seek a ruling from the professor. I will report any violations of this honor code of which I am aware. Violating this honor code is grounds for immediate disenrollment from this course, or other sanctions as provided for by College of Law and University policy on academic dishonesty.*


## Problem 1 (20 points): Rock, Paper, Scissors

Write a function named `rps` that plays rock, paper, scissors with a human.  It should first select randomly between rock, scissors, and paper, keeping that selection secret, then ask the user for input (no cheating and doing it the other way around!). After the user provides the appropriate input, it should decide who won or if there's a tie by the standard means (rock beats scissors beats paper beats rock) and reveal both its choice and the winner to the user.

**Rules and definitions for this problem:**

- rps must accept input in uppercase, lowercase, and any weird mixed-up case the user types in, it must also accept input with any number of spaces before or after the word. For example, `rock` `Rock` `ROCK` `     rock` and `rOcK   ` are all acceptable input.  

- If the user tries to enter anything other than rock, paper, or scissors, it should print the message `"Please enter rock, paper, or scissors."` and then ask the user for input again.

- The response must be of the form `"I picked [rock/paper/scissors]. [You/I/Nobody] won!"`

**Example correct input and output:**

(arrow symbols designate things the computer prints out)

```
rps()
# computer picks rock in the background
-> Pick rock, paper or scissors!
# User types in "rocK"
-> I picked rock. Nobody won!
```


## Problem 2 (40 points): Date Calculator

Rule 6 of the Federal Rules of Civil Procedure specifies a procedure for calculating the various dates (like the date to file a reply to a complaint) under the rules. Reduce that procedure to code. 

Specifically, write a function, named `calculate_days`, that takes two parameters: `num_days` which is the number of days to count, and `start_date` which is the date to begin counting from (for example, the date from which a complaint is served, triggering the clock for a reply). It should return the correct due date under FRCP 6. 

**Rules and definitions for this problem:**

- `start_date` should have a default value of the current date when the script is run, in the time zone of the computer on which it is run. I should, in other words, be able to call `calculate_days(10)` and get a FRCP 6-compliant date ten days from the date on which I call the function.

- Dates should be passed into the function as strings in the form MM-DD-YYYY, for example, `"12-27-2017"`.  It should output dates as strings in plain English in a form like `"Tue, January 02, 2018"`. 

- Your calculation needs to take into account weekends and federal holidays that have a fixed date (New Years, Christmas, Veterans Day, and Independence day). It does not need to take into account holidays that have a weird date like "the fourth Monday in March" or whatever (e.g. Memorial Day, Thanksgiving). Also, it doesn't need to take into account "observed" holidays, for example, federal workers getting Monday off if Veterans Day happens to fall on a Sunday. 

- However, you can receive five bonus points for correctly handling floating holidays like Memorial Day, and another 5 bonus points for correctly handling holidays where the statute says that if it falls on a Sunday it's observed on a Monday/if it falls on a Saturday, it's observed on a Sunday.

- *Hint:* look into the built-in Python library `datetime`. There are lots of tutorials about how to use it.

**Example correct input and output:**

`calculate_days(3, "01-16-2019")` should return `Mon, January 21, 2019`

`calculate_days(19, "06-15-2019")` should return `Fri, July 05, 2019`

### Half credit version of problem 2

You may write a version of `calculate_days` that does not take into account weekends and holidays for half credit.  The half credit version also does not need to provide output in precisely the format specified above, although it should still output a string that is recognizably a date and is comprehensible to an ordinary lawyer. 

## Problem 3 (40 points): Cite Finder

Write a function, named `cite_finder`, that takes one parameter, `case`, a string with a citation to an Illinois Supreme Court case, and returns the following: 

A.  `None`, if the citation does not correspond to an actual case.

B. An empty list, if the citation corresponds to an actual case, but the text of that case does not include any citations to the U.S. Supreme Court.

C.  A Python `list` of unique U.S. Supreme Court citations that appear in the text of the case, if the citation corresponds to an actual case and the case contains any U.S. Supreme Court citation.  

**Rules and definitions for this problem:**

- "Unique" means a citation to a specific case from a specific reporter. 

- "Citation to an Illinois Supreme Court case" means a string reflecting a citation to the official reporter of the Illinois Supreme Court, in the form `12 Ill. 345` or `12 Ill.2d 345`. 

- "U.S. Supreme Court citation" means any full citation (not supra, id, etc.) from the official U.S. Supreme Court reporter as abbreviated `U.S.`. Party names, years, and page numbers need not be included. Archaic citations (like to Cranch), S.Ct., and L.Ed. Citations should not be included. Subsequent cites/pin cites to a case of the form `123 U.S. at 456` should not be included.

- "Text" of a case includes all opinions (majority, concurrence, dissent, etc.) but does not include syllabus or any other content. 

- Your function must use the [Caselaw Access Project (case.law) API](https://case.law). 

- The list must be sorted using Python’s built-in list sorting functionality with default options.

- Each citation must appear only once.

**Example correct input and output:**

- `cite_finder("231 Ill.2d 474")` should return `['387 U.S. 136', '419 U.S. 102', '424 U.S. 1', '429 U.S. 252', '508 U.S. 520', '509 U.S. 43']`

- `cite_finder("231 Ill.2d 475")` should return `None`

- `cite_finder("215 Ill.2d 219")` should return `['339 U.S. 594', '387 U.S. 136', '467 U.S. 837', '538 U.S. 803']`

### Half credit version of problem 3: 

You may get half credit on this problem by writing a function, called `justice_finder`, which takes an Illinois Supreme Court citation as defined above and returns a list of every justice who wrote an opinion. This must also use the Caselaw Access Project API.

Example correct input and output for half-credit version: 

- `cite_finder("231 Ill.2d 474")` should return `['JUSTICE THOMAS', 'JUSTICE FREEMAN,']`
