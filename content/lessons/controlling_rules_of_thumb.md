title: Some Rules of Thumb for Controlling
tags: statistics, regressions, week11
date: 2020-03-31

You've seen a lot of talk about controlling for things, for e.g., in multiple regression (or more generally, conditioning on things).  It's worth having a quick list of some rules of thumb that will suffice for many cases.  Of course, the design of observational studies is much more complicated than this, but some general principles will do, again, for triggering your spidey-sense if you see a regression that breaks these rules. 

**DO control for confounders**

If something could cause both the X variable of interest, and the Y variable, control for it.

**DO control for alternative causes**

This rule only applies if controling for the variable doesn't violate some other rule.  But generally, one problem with observational data is that you might have *bad luck*: you might end up with a dataset where the real cause happens to be correlated with the thing that you think might be the cause (but really isn't), purely by chance.  Without controlling for the real cause, you can get a spurious association.

**DON'T control for colliders**

See the lecture on causal inference for a discussion of collider bias. This comes up most often when you condition on a post-treatment variable, and this includes selecting your data based on some criterion (intentionally or unintentionally) in a way that might be influenced by the treatment (i.e., the X variable of interest).  [This page has a helpful discussion of how this breaks you](https://catalogofbias.org/biases/collider-bias/).

**SOMETIMES control for mediators**

For this, we need to distinguish between two ideas: the "direct effect" of some variable, and the "total effect" of some variable.  Consider the theory of a sex discrimination case, according to which an employer may discriminate against women because of bias, but it might *also* be the case that women are paid less on average because they have less work experience, because society at large has disproportionately foisted caretaking responsibilities (especially, but not exclusively, for children) on them.  The effect of gender on pay within the same experience level---that is, because of employer disparate treatment or bias---is called the "direct effect" (and it's also the thing that will get an employer held liable under Title VII); the effect of gender on pay accounting for *both* bias and the indirect effect gender --> experience --> pay is the "total effect."  If you're trying to get the total effect, don't control for a mediator; if you're trying to get the direct effect, do control for the mediator. Be aware, however, that mediator analysis is notoriously hard in general. 

**DON'T control for random stuff**

If you don't have a story for why you're controlling for something, don't control for it.  It will just eat up degrees of freedom (making it harder to see significant results), plus run the risk of p-hacking if you're doing a bunch of different versions of a regression to see which ones pan out.
