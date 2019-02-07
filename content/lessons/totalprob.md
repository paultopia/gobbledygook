title: Week 4 recap: Total Probability Rule
tags: probability, conceptual, week4
date: 2018-02-05

The probability lecture this week kind of hit a wall at one point in our Bayes Rule example.  Here's a clearer explanation.

Remember, we had an example problem involving figuring out the posterior probability of someone being drunk, given that they blew a positive result on a breathalyzer.  

The place where we got stuck was when we were trying to do was calculate the probability of blowing a positive breathalyzer, i.e., $P(blew)$.  But all we had was the true positive rate, i.e., the probability that the machine would produce a positive result conditional on someone being drunk $P(blew|drunk)$ and the false positive rate, i.e., the probability that the machine would produce a positive result conditional on someone being sober $P(blew|sober)$, as well as the prior probability of being drunk $(.1)$.  

We needed $P(blew)$ because it is the denominator in our Bayes Rule calculation. Here's Bayes Rule again: 

$$P(B|A) = \frac{P(A|B)P(B)}{P(A)}$$

We were trying to calculate $P(drunk|blew)$ and, per Bayes rule, that means we need to know the overall probability of a positive result (that's A here). Plugging in our terms, we were trying to figure out.

$$P(drunk|blew) = \frac{P(blew|drunk)P(drunk)}{P(blew)}$$

What I asserted to you is that we can use the following calculation to go from what we know to the denominator of that equation: 

$$P(blew) = P(blew|drunk) \cdot P(drunk) + P(blew|sober) \cdot P(sober)$$

This is known as the law of total probability. [Wikipedia gives another good example](https://en.wikipedia.org/wiki/Law_of_total_probability#Example).  

Here's a hopefully-more intuitive explanation of why you should believe this.  What we're really doing is partitioning the world.  You can only be drunk or sober, right?  You can't be drunk AND sober, and you can't be neither drunk nor sober.  Drunkenness and soberness are mutually exclusive and exhaustive. 

So what that means is that there are only two ways to blow a positive breathalyzer.  You can either blow a breathalyzer when you're drunk, or you can blow a breathalyzer when you're sober. 

And then what we're asking is for the union of those two events, the "or" question.  The question "what's the probability of blowing a positive breathalyzer test" is just "what's the probability of blowing a positive breathalyzer test and being drunk, OR blowing a positive breathalyzer test and being sober."  And we know those have to be mutually exclusive events (because, yet again, can't be drunk and sober at the same time), so we know that we just add them up.  The addition rule gets us to: 

$$P(blew) = P(blew \cap drunk) + P(blew \cap sober)$$

Ok, so how do we calculate those?  Well, let's reason through it.  What's the probability of both being drunk and blowing a positive result?  Well, it's gotta be lower than the probability of being drunk (because the probability of A and B always has to be lower than the probability of A alone, or identical to it in the pathological case where the probability of B is 1). The trick is to realize that conditional probabilities encode the information "given that I know A happened, what's the probability of B."  So it stands to reason that if you want to know whether A and B happened, you'd be interested in the probability of A, as well as the conditional probability of B given A.  

This is what, in the earlier reading, I called "the expanded multiplication rule.  The formula is as follows: 

$$P(A \cap B) = P(A)P(B|A)$$

To remind you, here's what I said in the first reading to explain this: 

> The classic example to understand the reasoning behind the expanded multiplication rule is drawing cards. If you draw cards from a normal deck and don't put them back, then the probability of the first card being a heart is just 13/52 = 1/4. What's the probability of drawing a second heart?

> Well, imagine that instead of drawing from the same deck, someone just gave you a second deck of cards with 51 cards in it, 12 of which were hearts. We know the probability of drawing a heart in that second deck, right? 12/51. That world is just the world described by the conditional probability of drawing a second heart given that you've already drawn a first. So what's the probability of drawing a heart out of the normal deck and a heart out of the weird second deck? Easy: 1/4 * 12/51.

So that gets us as far as $P(A \cap B) = P(A)P(B|A)$.  And, it should be obvious that  $P(A \cap B) = P(B \cap A)$ ("A and B" is the same as "B and A"). If we substitute "drunk" and "sober" for A in the two sides of our addition, and substitute "blew" for B, then, by plugging in, we can conclude that 

$$P(blew) = P(blew|drunk) \cdot P(drunk) + P(blew|sober) \cdot P(sober)$$

Which is the assertation I originally made, expressing the law of total probability, and which allows us to get the denominator of our Bayes Rule calculation.

Subsequent weeks will not have nearly this much notation.  Do not fear.


[Download lesson PDF]({attach}../images/totalprob.pdf)

