"""
Balanced Chemical Reactions


For a chemical reaction represented by a string, verify that the chemical
reaction is a balanced reaction (i.e. that we didn't somehow lose or gain
an atom during reaction). If the reaction is balanced return true,
otherwise return false.

For example, for the hydrogen combustionreaction:

    '2 H2 + O2 -> 2 H2O'

would output true because the number of atoms in the reactants match up
with the number of atoms in the product.

However, for the precipitation of silver-chloride:

    'NaCl + AgNO3 -> NaNO3 + Ag'

the output should be false because we're missing the chlorine atom in
the products.

The reactancts and products will always be separated by a right
pointing arrow "->" and the individual molecules within the
reactants/products are always separated by a "+" sign. Multiple
molecules are represented by a number and space prefacing the
molecule (e.g., "2 H20").
"""
import re
from collections import defaultdict

s = 'NaCl + AgNO3 -> NaNO3 + Ag'
s = '2 H2 + O2 -> 2 H2O'

mid = s.index('->')
left = s[:mid].strip().split('+')
right = s[mid+2 :].strip().split('+')

def findComp(left):
    composition = defaultdict(int)
    for e in left:
        element = e.strip().split()    # ['2', 'H2O'] ['NaCl'] ...
        if len(element) == 2:
            tmp = re.findall(r'([A-Z][a-z]*)(\d*)', element[1])
            for x in tmp:
                if x[1] == '':
                    composition[x[0]] += int(element[0]) * 1
                else:
                    composition[x[0]] += int(element[0]) * int(x[1])
        else:
            # re.findall(r'([A-Z][a-z]*)(\d*)', 'NaClO3')
            # tmp: [('Na', ''), ('Cl', ''), ('O', '3')]
            tmp = re.findall(r'([A-Z][a-z]*)(\d*)', element[0])
            for x in tmp:
                if x[1] == '':
                    composition[x[0]] += 1
                else:
                    composition[x[0]] += int(x[1])
    return composition


print left, right

print findComp(left)
print findComp(right)
print findComp(left) == findComp(right)


# https://leetcode.com/problems/number-of-atoms/description/
"""
The first regex ([A-Z]{1}[a-z]?|\(|\)|\d+) splits up the input string into a few kinds of tokens for parsing: (1) An atom (2) A number (3) Open bracket (4) Closing bracket. These are the only tokens we need to do our parsing.

An input of Mg(OH)2 will be tokenized into: ['Mg', '(', 'O', 'H', ')', '2'].
An input of K4(ON(SO3)2)2 will be tokenized into: ['K', '4', '(', 'O', 'N', '(', 'S', 'O', '3', ')', '2', ')', '2'].

As we iterate through the tokens, there are three cases that we need to handle:

Open bracket - We push a new dictionary onto a stack to keep track of the atoms and its count in this current group
Close bracket - The next token might be a number/count. Check whether if it is a count. If it is, multiply all the atoms at the top of the stack by the count and combine it with a dictionary below it in the stack.
Normal atom - The next token might be a number/count. Check whether if it is a count. If it is, add that atom and its count to the top of the stack.
Cases 2 and 3 are very similar, so we can combine them.

At the end, sort the atoms alphabetically and format them nicely to be returned.

- Yangshun
"""
class Solution(object):
    def countOfAtoms(self, formula):
        import re
        from collections import defaultdict
        tokens = list(filter(lambda c: c, re.split('([A-Z]{1}[a-z]?|\(|\)|\d+)', formula)))
        stack, i = [defaultdict(int)], 0
        while i < len(tokens):
            token = tokens[i]
            if token == '(':
                stack.append(defaultdict(int))
            else:
                count = 1
                # Check if next token is a number.
                if i + 1 < len(tokens) and re.search('^\d+$', tokens[i + 1]):
                    count, i = int(tokens[i + 1]), i + 1
                atoms = stack.pop() if token == ')' else { token: 1 }
                # Combine counts of atoms.
                for atom in atoms:
                    stack[-1][atom] += atoms[atom] * count
            i += 1
        return ''.join([atom + (str(count) if count > 1 else '') for atom, count in sorted(stack[-1].items())])