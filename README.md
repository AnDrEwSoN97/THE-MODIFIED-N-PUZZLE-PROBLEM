# THE-MODIFIED-N-PUZZLE-PROBLEM
Suppose the standard n-puzzle problem is modified so that there are two empty locations (instead of one) allowing you to pick any one tile adjacent to any one of the two empty locations and move it to the adjacent empty location. You are given a starting configuration and are supposed to rearrange the tiles by move them into the empty locations as necessary to end up in a given goal configuration. Figure 1 shows an example of a starting and a goal configuration

THE MODIFIED N-PUZZLE PROBLEM

• To solve the modified n puzzle problem, we were required to create 100 inputs to test the 
Manhattan and misplaced method, so I used “[1,5,'-',2,7,4,6,3,'-']” as the possible values to 
generate the random inputs.

• While running the algorithm for the Manhattan method, different moves required was 
calculated and stored in the file “manhattan.txt”

• While running the algorithm for the misplaced method, different moves required was calculated 
and stored in the file “misplaced.txt”

• Then the difference between the above methods was calculated and obtained a mean value of 
“54.94”

• By considering “Misplaced” as null hypothesis and “Manhattan” as alternative the probability 
of obtaining results at least as extreme as the observed results of a statistical hypothesis test is 
calculate using statistics method in SciPy library. It is “p=.12239756224987167”

• By considering “Manhattan” as null hypothesis and “Misplaced” as alternative the probability 
of obtaining results at least as extreme as the observed results of a statistical hypothesis test is 
calculate using statistics method in SciPy library. It is “p=.12239756224987167”

• But A p-value higher than 0.05 (> 0.05) is not statistically significant and indicates strong 
evidence for the null hypothesis. This means we retain the null hypothesis and reject the 
alternative hypothesis. You should note that you cannot accept the null hypothesis, we can only 
reject the null or fail to reject it. A statistically significant result cannot prove that a research 
hypothesis is correct (as this implies 100% certainty). Instead, we may state our results “provide 
support for” or “give evidence for” our research hypothesis (as there is still a slight probability 
that the results occurred by chance and the null hypothesis was correct – e.g. less than 5%).

• So we cannot come to a conclusion to choose one as the best method
