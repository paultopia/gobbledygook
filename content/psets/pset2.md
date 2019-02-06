title: Problem Set 2
tags: psets
date: 2018-02-02

Due Friday, February 22, at 5pm Central time. 

As before, please turn in your answers in a single notebook.  For the questions that require you to write down prose, hopefully by now you've realized that you can change the type of a notebook cell to "markdown" to write regular text rather than Python code. 

In recognition of the fact that the last problem set was a little too difficult, I've lightened this one up a bit. 

## Problem 1 (60 points): Suspicious Persons

The Customs and Border Patrol (CBP) is concerned about drug trafficking on the many international flights landing in Cedar Rapids Airport (CID) (humor me).  Accordingly, it consults the research, and develops a Drug Trafficker profile, which combines factors which have been shown to predict drug trafficking.  Let's call those factors *Seediness*, *Sketchiness*, and *Shadiness*. CBP officers identify Seediness, Sketchiness, and Shadiness with perfect accuracy, and Seediness, Sketchiness, and Shadiness are conditionally independent both on drug trafficking and the complement of drug trafficking.

Based on the evidence available to the CBP: 

- If an international traveler entering CID is carrying illegal drugs, then $\alpha %$ (alpha) of the time that person is also Seedy.  That is, out of every 100 people who are carrying drugs, $\alpha$ of those people are Seedy. 

- If an international traveler entering CID is carrying illegal drugs, then $\beta %$ (beta) of the time that person is also Sketchy.

- If an international traveler entering CID is carrying illegal drugs, then $\gamma %$ (gamma) of the time that person is also Shady.

- If a person does not have drugs, then they are unlikely to be Seedy, Sketchy, or Shady---the probability of an international traveler entering CID being one of those things conditional on them not carrying illegal drugs is $\psi$ (psi). (To be completely clear: $P(Seedy|NotDrugs) = \psi$ and $P(Sketchy|NotDrugs) = \psi$ and $P(Shady|NotDrugs) = \psi$.)

- Out of all international travelers entering CID, $\mu %$ (mu) have drugs. 

Accordingly, the CBP issues a directive to its border control agents at the Cedar Rapids airport.  Every international traveler entering CID who is Seedy, Sketchy, and Shady must be stopped and searched for drugs.  (It turns out this kind of nonsense is constitutional at borders.) 

**Problem 1.A** (20 points): Write a function, `search_results(...)` which takes appropriate parameters based on the information above and computes the probability that a person who is stopped under the above-described CBP directive is carrying illegal drugs.

**Problem 1.B** (20 points): Explain the math behind your function. 

**Problem 1.C.** (20 points): Now suppose Sketchiness is not conditionally independent of Shadiness given non-drug-carrying (it is still conditionally independent given drug-carrying). Would your calculation change?  Briefly explain why and how.

## Problem 2 (40 points): Benford's Law

There's a well-known empirical regularity according to which the first digits in people's real-world income tend to be predominantly lower---i.e., lots more 1s than 9s, and so forth. This is known as Benford's law, and it is often used to detect tax cheats, accounting fraud, and the like.  

Illustrate Benford's law with a simulation of randomly chosen U.S. incomes.  You should assume that income follows either a lognormal or an exponential distribution (both will work)  Show the resulting distribution of digits with an appropriate data visualization.  

*hint*: You'll have to tweak the scale on either distribution in order to get it to an appropriate magnitude that represents typical U.S. incomes. Experiment!

*bonus* For more on Benford's law, see [this Forbes article](https://www.forbes.com/sites/danielfisher/2014/05/30/the-simple-mathematical-law-that-financial-fraudsters-cant-beat/#53798c8e4612) and [this academic article paper reporting a simulation study of different distributions](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0010541).  If you interview for any job involving detecting financial fraud (IRS, SEC, etc.), you can probably make yourself look awesome by knowing about this. 





