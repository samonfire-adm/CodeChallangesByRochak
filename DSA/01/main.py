def determine_winner(rishi_rolls, sam_rolls):
    rishi_rolls.sort()
    rishi_sum = rishi_rolls[-1] + rishi_rolls[-2]
    sam_rolls.sort()
    sam_sum = sam_rolls[-1] + sam_rolls[-2]

    if rishi_sum > sam_sum:
        return "Rishi wins with a sum of {}".format(rishi_sum)
    elif sam_sum > rishi_sum:
        return "Sam wins with a sum of {}".format(sam_sum)
    else:
        return "The game is a tie with a sum of {}".format(rishi_sum)


rishi_rolls = [3, 2, 5]
sam_rolls = [4, 3, 1]
result = determine_winner(rishi_rolls, sam_rolls)
print(result)
