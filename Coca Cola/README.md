Title: The Coca-Cola Conundrum

**Question:**
You know those days when you're just lounging around, pondering life's greatest questions? Well, I had one of those moments while sitting at a café sipping my Coca-Cola. Suddenly, I began to wonder how to entertain myself. Then it hit me: what if I devised a quirky little algorithm to play with numbers that could decide whether to say "Coca," "Cola," or "CocaCola" based on divisibility? So here's the thing...

**Description:**
Imagine you're hosting a party, and you've got a bunch of numbers mingling around. Now, some of these numbers are a little quirky. For instance, if a number is divisible by 3, you shout "Coca." If it's divisible by 5, you yell "Cola." And if it's divisible by both 3 and 5, you bellow "CocaCola." But hey, if a number doesn't fit into any of these categories, you just announce the number itself. Crazy, right? It's like a mathematical party game!

**Input Format:**
- The first line contains a single integer **n**, representing the total numbers.
- The next **n** lines contain a single integer each, denoting the numbers at the party.

**Output Format:**
- For each number, output either "Coca," "Cola," "CocaCola," or the number itself, depending on the divisibility rules.

**Constraints:**
- 1 ≤ n ≤ 100
- 1 ≤ Number ≤ 1000

**Sample:**

| Input | Output      |
|-------|-------------|
| 1    | 1           |
| 2     | 2           |
| 3     | Coca        |
| 4     | 4           |
| 5     | Cola        |
| 6     | Coca        |
| 7     | 7           |
| 8     | 8           |
| 9     | Coca        |
| 10    | Cola        |

**Explanation:**
- For instance, when you see 3, you say "Coca" because it's divisible by 3. When you see 5, you shout "Cola." But when you see 15, you gotta go all out and scream "CocaCola" because it's divisible by both 3 and 5. And the numbers just hanging out without fitting any of these categories? Well, you just let them be, like the quiet ones at the party.