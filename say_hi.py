"""
Problem Statement
You are given N lines and your task is to find out which of the N lines starts with

hi<BLANK>
where hi is case-insensitive and is not immediately followed by a space and a letter d(or D). 
In the above representation, BLANK denotes a space character.

Input Format
First line contains an integer N. N lines follow each line with a sentence not more than 10 words W each, separated by a single space.

Constraints
1 <= N <= 10 
If C is the count of the number of words W in every sentence, then 
1 <= C <= 10 
Each non-empty character in W is either a lowercase or an uppercase letter only

Output Format
Print each line that satisfies the constraint as mentioned in the problem statement.

Sample Input
5
Hi Alex how are you doing
hI dave how are you doing
Good by Alex
hidden agenda
Alex greeted Martha by saying Hi Martha

Sample Output
Hi Alex how are you doing
"""
import re
import sys

p = re.compile(r"^[hH][Ii] [^Dd]")

n = input()

while n > 0:
    s = sys.stdin.readline().strip()
    if p.match(s):
        print s
    n -= 1
