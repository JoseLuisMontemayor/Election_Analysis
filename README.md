# Election_Analysis

Helping on the analysis of an audit election to determine the winner and the total results. 

## Overview of Election Audit

In this analysis we will review the audit of an election. With the help of Python, Visual Studio Code and other tools we were able to examine the total results in details of a data given with all the votes from the election. Within a matter of seconds with a finished code we are able to get the results from more than 300,000 lines of data. We could find how many number of votes of each county had, for each candidate, and define who the winner was within the total of votes. Within the making of the project we encountered with problems that made us try different alternatives to run a solution (code) and to understand better the language of Python. The data was given perfectly and we could manipulate them to find the beest solution. 

## Election Audit Results

After running the data, the results were the next: 

* Total votes in the election: 369,711
* Total votes in each county:
    - Jefferson: 10.5% (38,855)
    - Denver: 82.8% (306,055)
    - Arapahoe: 6.7% (24,801)
* County with the most amount of votes: Denver
* Total votes for each candidate: 
    - Charles Casper Stockham: 23.0% (85,213)
    - Diana DeGette: 73.8% (272,892)
    - Raymon Anthony Doane: 3.1% (11,606)
* The winner of the election evidently was Diana DeGette, with 73.8% of the total votes (272,892). 

## Election-Audit Summary

The code can be used for any type of election, it is already programmed to throw out the results as in the text file. The only changes that there would be needed would be the change in terms of Text/Strings, counties and names. Within changing the that information the results with other candidates can be expected. In terms of data, the original excel would need to be manipulated with another data, but as long as the threee columns are kept as they are the code would still work, as long as it coincides with the information in the code. 

An example of the code of the winner of the results, it would be as the next part of the code: 

![](https://github.com/JoseLuisMontemayor/Election_Analysis/blob/main/Winning_candidates.PNG)

As we can see, we assinged the results of the vote count to be arranged with comas and the percentage to only have one decimal. By assigned this type of outcome, we had to end with the *,}\n"* signs in the vote count and with the *.1f}%\n"* signs in the winning percentage. The outcome appears like this: 






