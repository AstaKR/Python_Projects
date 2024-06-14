scores = input("Enter the Scores : ").split()
for n in range(0, len(scores)):
    scores[n] = int(scores[n])
highest_scores = 0
for score in scores:
    if score >= highest_scores:
        highest_scores = score
       
print(highest_scores)

# Output:
# Enter the Scores : 90 20 30 40
# 90