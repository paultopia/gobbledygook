title: Introduction to Python and setup.
tags: python, code, week1, setup
date: 2018-10-22

In this class, we will be using the [Python](https://www.python.org/) programming language. In this first week, we will have a basic introduction to Python and to the fundamentals of computer programming. 

Before we get started programming, we have to set up a system to write our code and get the computer to read it. Most introductory Python texts, including the texts we'll be working with, ask you to install an "interpreter"---a program on your own computer that can read and execute Python code. We won't be doing that here.

Instead, all your code will run in the cloud. We'll be using a free service by Microsoft called [Azure Notebooks](https://notebooks.azure.com/). This service will let you type in and execute your code online, through your web browser. This has some very large advantages: 

- You don't have to install anything locally, which can be problematic (especially for Windows users), and I don't have to try to debug your local installations.

- Azure Notebooks runs on notebook software called [Jupyter](http://jupyter.org/) which is built for data analysis (all the cool data scientist kiddos use it), so it has lots of nice facilities for exploring data and code incrementally, visualizing data, displaying tables, etc. 

In addition, I will ask you to make use of the free [Github](https://github.com/) service to "clone" (copy) assignments, which will be in notebook files that you can just run on Azure, as well as to turn those assignments in. Also, you will sign up for [DataCamp](https://www.datacamp.com), I've set up free access for the duration of the class.

We'll get set up with all this stuff on the first day of class. **Please bring a computer to class every day**.  Macs, Windows computers, and Linux computers will all work fine (though if you're a Linux user, you might be too advanced for this class).  We can make Chromebooks work too if need be. Anything else, talk to me. 

### Advanced user note

The Azure Notebooks environment can be slow and a little awkward. It's better for beginners than installing Python locally, because of issues different operating systems and occasionally causing conflicts with other versions of things.  However, if you want to install locally, here's what you should use: 

- Install the [Anaconda Python distribution](https://www.anaconda.com) for your operating system.  This is important: you want to use the **Python 3.7** version of the installer, *not* Python 2.7. 

- If you want to do this, I'll help as much as I can, but you should know how to use the command line for your operating system. If you use Windows, I won't be able to help you as much as if you use a Mac or Linux. For Windows users, you might try setting up the Windows Subsystem for Linux and installing Anaconda through the instructions [in this article](https://medium.com/hugo-ferreiras-blog/using-windows-subsystem-for-linux-for-data-science-9a8e68d7610c), but I can't promise this will work. For Chromebook users, you probably won't be able to install Python locally unless you have a Pixelbook or some other [Chromebook that supports Crostini](https://www.reddit.com/r/Crostini/wiki/getstarted/crostini-enabled-devices). 

- In additional to installing Python, you'll probably want a good development-quality text editor if you get into programming outside of Jupiter notebooks. I recommend [Atom](https://atom.io) or [VS Code](https://code.visualstudio.com), both of which should work on Mac, Windows, or Linux. 