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
                    composition[x[0]] += int(element[0])
                else:
                    composition[x[0]] += int(element[0]) * int(x[1])
        else:
            # re.findall(r'([A-Z][a-z]*)(\d*)', 'NaClO3')
            # [('Na', ''), ('Cl', ''), ('O', '3')]
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
