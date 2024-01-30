# This is a tutorial program that illustrates the use of
# the while and if statements with simple user input and output

# initialize variables
counter = 0
score_total = 0
test_score = 0


# get scores and add to sum
while test_score != 999:
    test_score = int(input("Enter test score (0-100 or 999 to exit): "))
    if test_score >= 0 and test_score <= 100:
        score_total += test_score    # add score to total
        counter += 1                 # add 1 to counter

print("Average score: = " + str(score_total/counter))
