You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs. 

Then check for the number of times the letters in the word LOVE occurs. 

Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:

"Your score is **x**, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:

"Your score is **y**, you are alright together."
Otherwise, the message will just be their score. e.g.:

"Your score is **z**."
e.g.

name1 = "Angela Yu"
name2 = "Jack Bauer"
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

Print: "Your score is 53."

Example Input 1
name1 = "Kanye West"
name2 = "Kim Kardashian"
Example Output 1
Your score is 42, you are alright together.
Example Input 2
name1 = "Brad Pitt"
name2 = "Jennifer Aniston"
Example Output 2
Your score is 73.



///**** CODE ****///

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1 = name1.lower()
name2 = name2.lower()

name = name1 + name2
a = name.count("t")
b = name.count("r")
c = name.count("u")
d = name.count("e")

y = a+b+c+d

m = name.count("l")
n = name.count("o")
o = name.count("v")
v = name.count("e")

z = m+n+o+v

total = str(y) + str(z)
total = int(total)

if total < 10 or total > 90:
    print("Your score is {}, you go together like coke and mentos.".format(total))
elif total > 40 and total < 50:
    print("Your score is {}, you are alright together.".format(total))
else:
    print("Your score is {}.".format(total))
