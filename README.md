## Google Foobar Hack
### Jack Wagner

Google Foobar is a invite-only coding challenge that Google uses to hire software developers.  Certain terms associated with coding will cause a secret invitation to pop up in one's browser saying:

###"You're speaking our language.  Up for a challenge?###

| I want to play                        | No thanks                          |Don't show me this again                          |
|------------------------------------------|------------------------------------------|------------------------------------------|


If the user accepts the invitation, then they will receive a series of ten coding problems from Google and will be given a strict time frame in which to complete each project.  If they complete all the problems, then they skip ahead in the Google hiring process.



###*browserTabs.py* 

In browserTabs.py*, I took a list of computer science terms from `https://en.wikipedia.org/wiki/Glossary_of_computer_science` and loaded them into *lotsOfTerms.txt* and *searchTerms.txt*.  The program then chooses to random terms, randomly chooses between either "Python" or "Java", and creates a string in the following format:

`str(term1) + " and " + str(term2 + " in " + str(language))`

The program then waits a doubly-random amount of seconds.  Doubly-random means that randomly chooses either 2 or 3 and multiplies that by a random number in the range [0, 1).  With simply singly-random wait time, the google servers will block the user's IP address.

*browserTabs.py* waits the specified doubly-random wait time, then opens a browswer in Google and searches for the string.
