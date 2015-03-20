"""
Problem Statement
Given a line of text which possibly contains the latitude and longitude of a point, can you use regular expressions to identify the latitude and longitude referred to (if any)?

Input Format 
The first line contains an integer N, which is the number of tests to follow. 
This is followed by N lines of text. Each line contains a pair of co-ordinates which possibly indicate the latitude and longitude of a place.

Constraints 
1 <= N <= 100 
The latitude and longitude, if present will always appear in the form of (X, Y) where X and Y are decimal numbers. 
For a valid (latitude, longitude) pair: 
-90<=X<=+90 and -180<=Y<=180. 
They will not contain any symbols for degrees or radians or N/S/E/W. There may or may not be a +/- sign preceding X or Y. 
There will be a space between Y and the comma before it. 
There will be no space between X and the preceding left-bracket, or between Y and the following right-bracket. 
There will be no unnecessary zeros (0) before X or Y.

Output Format 
"Valid" where X and Y are the latitude and longitude which you found to be a valid (latitude,longitude) pair. 
If the given pair of numbers are not a valid (latitude,longitude) pair, output "Invalid".

Sample Input
12
(75, 180)
(+90.0, -147.45)
(77.11112223331, 149.99999999)
(+90, +180)
(90, 180)
(-90.00000, -180.0000)
(75, 280)
(+190.0, -147.45)
(77.11112223331, 249.99999999)
(+90, +180.2)
(90., 180.)
(-090.00000, -180.0000)

Sample Output
Valid
Valid
Valid
Valid
Valid
Valid
Invalid
Invalid
Invalid
Invalid
Invalid
Invalid
"""
import re
import sys
regex = r"\([+\-]?([1-8]?\d(\.\d+)?|90(\.0+)?), [+\-]?((1)?(?(5)[0-7]|[1-9]?)\d(\.\d+)?|180(\.0+)?)\)"
p = re.compile(regex)

n = input()

while n > 0:
    s = sys.stdin.readline()
    if p.match(s):
        print "Valid"
    else: print "Invalid"
    n -= 1
