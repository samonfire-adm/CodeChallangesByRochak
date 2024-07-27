def find_two_largest_sum(rolls):
    
    if len(rolls) != 3:
        raise ValueError("Each player must roll the dice exactly three times.")
    
    
    max1, max2 = float('-inf'), float('-inf')
    
   
    for roll in rolls:
        if roll > max1:
            max2 = max1
            max1 = roll
        elif roll > max2:
            max2 = roll
    

    return max1 + max2

def determine_winner(rishi_rolls, sam_rolls):

    if len(rishi_rolls) != 3 or len(sam_rolls) != 3:
        raise ValueError("Each player must roll the dice exactly three times.")
    

    rishi_sum = find_two_largest_sum(rishi_rolls)
    sam_sum = find_two_largest_sum(sam_rolls)
    

    if rishi_sum > sam_sum:
        return "Rishi wins with a sum of {}".format(rishi_sum)
    elif sam_sum > rishi_sum:
        return "Sam wins with a sum of {}".format(sam_sum)
    else:
        return "The game is a tie with a sum of {}".format(rishi_sum)

# Example usage with test cases
test_cases = [
    ([3, 2, 5], [4, 3, 1]),  # Normal case
    ([6, 6, 6], [6, 6, 6]),  # All rolls are the same
    ([1, 1, 1], [1, 1, 1]),  # All minimum rolls
    ([6, 6, 6], [1, 1, 1]),  # One player rolls all maximum, the other all minimum
    ([1, 2, 3], [4, 5, 6]),  # Different distributions
]

for rishi_rolls, sam_rolls in test_cases:
    try:
        result = determine_winner(rishi_rolls, sam_rolls)
        print(f"Rishi rolls: {rishi_rolls}, Sam rolls: {sam_rolls} => {result}")
    except ValueError as e:
        print(e)
