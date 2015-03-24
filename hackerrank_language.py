import sys
import re
target = """C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA:
ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART
:GROOVY:OBJECTIVEC""".split(":")
target = [s.strip() for s in target]
target = "|".join(target)
regex = "^(%s)$" % target


p = re.compile(regex)

n = input()

while n > 0 :
    ID, lang = sys.stdin.readline().strip().split()

    if p.match(lang):
        print "VALID"
    else: print "INVALID"

    n -= 1
