2. Regular Expressions

2.1 Defining regular expressions

Defining a regular expression is to provide a sequence of characters, the
pattern, that will match sequences of characters in a target.

Here are several places to look for help:

Python Library Reference: 4.2.1 Regular Expression Syntax
Regular Expression HOWTO
The patterns or regular expressions can be defined as follows:

Literal characters must match exactly. For example, "a" matches "a".
Concatenated patterns match concatenated targets. For example, "ab" ("a"
followed
by "b")
matches "ab".  Alternate patterns, separated by a vertical bar, match either of
the alternative patterns. For example, "(aaa)|(bbb)" will match either "aaa" or
"bbb".  Repeating and optional items: "abc*" matches "ab" followed by zero or
more occurances of "c", for example, "ab", "abc", "abcc", etc.  "abc+" matches
"ab" followed by one or more occurances of "c", for example, "abc", "abcc",
etc, but not "ab".  "abc?" matches "ab" followed by zero or one occurances of
"c", for example, "ab" or "abc".  Sets of characters -- Characters and
sequences of characters in square brackets form a set; a set matches any
character in the set or range. For example, "[abc]" matches "a" or "b" or "c".
And, for example, "[_a-z0-9]" matches an underscore or any lower-case letter or
any digit.  Groups -- Parentheses indicate a group with a pattern. For example,
"ab(cd)*ef" is a pattern that matches "ab" followed by any number of occurances
of "cd" followed by "ef", for example, "abef", "abcdef", "abcdcdef", etc.
There are special names for some sets of characters, for example "\d" (any
igit),
"\w" (any alphanumeric character), "\W" (any non-alphanumeric character), etc.
See Python Library Reference: 4.2.1 Regular Expression Syntax for more.
Because of the use of backslashes in patterns, you are usually better off
defining regular expressions with raw strings, e.g. r"abc".

2.2 Compiling regular expressions

When a regular expression is to be used more than once, you should consider
compiling it. For example:

import sys, re

pat = re.compile('aa[bc]*dd')

while 1:
    line = raw_input('Enter a line ("q" to quit):')
    if line == 'q':
        break
    if pat.search(line):
        print 'matched:', line
    else:
        print 'no match:', line
Comments:

We import module re in order to use regular expresions.  "re.compile()"
compiles a regular expression so that we can reuse the compiled regular
expression without compiling it repeatedly.

2.3 Using regular expressions

Use match to match at the beginning of a string (or not at all).

Use search to search a string and match the first string from the left.

Here are some examples:

>>> import re
>>> pat = re.compile('aa[0-9]*bb')
>>> x = pat.match('aa1234bbccddee')
>>> x
<_sre.SRE_Match object at 0x401e9608>
>>> x = pat.match('xxxxaa1234bbccddee')
>>> x
>>> type(x)
<type 'NoneType'>
>>> x = pat.search('xxxxaa1234bbccddee')
>>> x
<_sre.SRE_Match object at 0x401e9608>
Notes:

When a match or search is successful, it returns a match object. When it fails,
it returns None.  You can also call the corresponding functions match and
search in the re module, e.g.:
>>> x = re.search(pat, 'xxxxaa1234bbccddee') x
<_sre.SRE_Match object at 0x401e9560>


2.4 Using match objects to extract a value

Match objects enable you to extract matched sub-strings after performing a
match. A match object is returned by successful match.

Here is an example:

import sys, re

pat = re.compile('aa([0-9]*)bb')

while 1:
    line = raw_input('Enter a line ("q" to quit):')
    if line == 'q':
        break
    mo = pat.search(line)
    if mo:
        value = mo.group(1)
        print 'value: %s' % value
    else:
        print 'no match'
Explanation:

In the regular expression, put parentheses around the portion of the regular
expression that will match what you want to extract. Each pair of parentheses
marks off a group.  After the search, check to determine if there was a
successful match by checking for a matching object. "pat.search(line)" returns
None if the search fails.  If you specify more than one group in your regular
expression (more that one pair of parentheses), then you can use "value =
mo.group(N)" to extract the value matched by the Nth group from the matching
object. "value = mo.group(1)" returns the first extracted value; "value =
mo.group(2)" returns the second; etc. An argument of 0 returns the string
matched by the entire regular expression.  In addition, you can:

Use "values = mo.groups()" to get a tuple containing the strings matched by all
groups.  Use "mo.expand()" to interpolate the group values into a string. For
example, "mo.expand(r'value1: \1 value2: \2')"inserts the values of the first
and second group into a string. If the first group matched "aaa" and the second
matched "bbb", then this example would produce "value1: aaa value2: bbb".

2.5 Extracting multiple items

You can extract multiple items with a single search. Here is an example:

import sys, re

pat = re.compile('aa([0-9]*)bb([0-9]*)cc')

while 1:
    line = raw_input('Enter a line ("q" to quit):')
    if line == 'q':
        break
    mo = pat.search(line)
    if mo:
        value1, value2 = mo.group(1, 2)
        print 'value1: %s  value2: %s' % (value1, value2)
    else:
        print 'no match'
Comments:

Use multiple parenthesized substrings in the regular expression to indicate the
portions (groups) to be extracted.  "mo.group(1, 2)" returns the values of the
first and second group in the string matched.  We could also have used
"mo.groups()" to obtain a tuple that contains both values.  Yet another
alternative would have been to use the following; "print mo.expand(r'value1: \1
value2: \2')".  2.6 Replacing multiple items

You can locate sub-strings (slices) of a match and replace them. Here is an
example:

import sys, re

pat = re.compile('aa([0-9]*)bb([0-9]*)cc')

while 1:
    line = raw_input('Enter a line ("q" to quit): ')
    if line == 'q':
        break
    mo = pat.search(line)
    if mo:
        value1, value2 = mo.group(1, 2)
        start1 = mo.start(1)
        end1 = mo.end(1)
        start2 = mo.start(2)
        end2 = mo.end(2)
        print 'value1: %s  start1: %d  end1: %d' % (value1, start1, end1)
        print 'value2: %s  start2: %d  end2: %d' % (value2, start2, end2)
        repl1 = raw_input('Enter replacement #1: ')
        repl2 = raw_input('Enter replacement #2: ')
        newline = line[:start1] + repl1 + line[end1:start2] + repl2 + line[end2:]
        print 'newline: %s' % newline
    else:
        print 'no match'

Explanation:

Alternatively, use "mo.span(1)" instead of "mo.start(1)" and "mo.end(1)" in
order to get the start and end of a sub-match in a single operation.
"mo.span(1)"returns a tuple: (start, end).  Put together a new string with
string concatenation from pieces of the original string and replacement values.
You can use string slices to get the sub-strings of the original string. In our
case, the following gets the start of the string, adds the first replacement,
adds the middle of the original string, adds the second replacement, and
finally, adds the last part of the original string: newline = line[:start1] +
repl1 + line[end1:start2] + repl2 + line[end2:] You can also use the sub
function or method to do substitutions. Here is an example:

import sys, re

pat = re.compile('[0-9]+')

print 'Replacing decimal digits.'
while 1:
    target = raw_input('Enter a target line ("q" to quit): ')
    if target == 'q':
        break
    repl = raw_input('Enter a replacement: ')
    result = pat.sub(repl, target)
    print 'result: %s' % result


And, finally, you can define a function to be used to insert calculated
replacements. Here is an example:

import sys, re, string

pat = re.compile('[a-m]+')

def replacer(mo):
    return string.upper(mo.group(0))

print 'Upper-casing a-m.'
while 1:
    target = raw_input('Enter a target line ("q" to quit): ')
    if target == 'q':
        break
    result = pat.sub(replacer, target)
    print 'result: %s' % result


Notes:

If the replacement argument to sub is a function, that function must take one
argument, a match object, and must return the modified (or replacement) value.
The matched sub-string will be replaced by the value returned by this function.
In our case, the function replacer converts the matched value to upper case.
This is also a convenient use for a lambda instead of a named function, for
example:

import sys, re, string

pat = re.compile('[a-m]+')

print 'Upper-casing a-m.'
while 1:
    target = raw_input('Enter a target line ("q" to quit): ')
    if target == 'q':
        break
    result = pat.sub(
        lambda mo: string.upper(mo.group(0)),
        target)
    print 'result: %s' % result
