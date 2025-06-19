'''Love Calculator
💪 This is a difficult challenge! 💪
You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people:
1. Take both people's names and check for the number of times the letters in the word TRUE occurs.
2. Then check for the number of times the letters in the word LOVE occurs.
3. Then combine these numbers to make a 2 digit number and print it out.
e.g.
name1 = "Angela Yu" name2 = "Jack Bauer"
T occurs 0 times
R occurs 1 time
U occurs 2 times
E occurs 2 times
Total = 5
L occurs 1 time
O occurs 0 times
V occurs 0 times
E occurs 2 times
Total = 3
Love Score = 53
Example Input

calculate_love_score("Kanye West", "Kim Kardashian")

Example Output

42
How to test your code and see your output?
Udemy coding exercises do not have a console, so you cannot use the input() function. You will need to call your function with hard-coded values like so:
'''

def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()
    t = combined_names.count('t')
    r = combined_names.count('r')
    u = combined_names.count('u')
    e = combined_names.count('e')
    true_score = t + r + u + e

    l = combined_names.count('l')
    o = combined_names.count('o')
    v = combined_names.count('v')
    e2 = combined_names.count('e')
    love_score = l + o + v + e2

    # Combine into a two-digit number
    love_score_total = int(str(true_score) + str(love_score))
    print(love_score_total)

# Example test
calculate_love_score("Kanye West", "Kim Kardashian")
