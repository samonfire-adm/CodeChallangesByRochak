def find_two_largest_sum(rolls):
    # Initialize the two largest numbers as negative infinity
    max1, max2 = float('-inf'), float('-inf')
    

    for roll in rolls:
        if roll > max1:
            max2 = max1
            max1 = roll
        elif roll > max2:
            max2 = roll
    

    return max1 + max2

def determine_winner(rishi_rolls, sam_rolls):

    rishi_sum = find_two_largest_sum(rishi_rolls)
    sam_sum = find_two_largest_sum(sam_rolls)
    

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
