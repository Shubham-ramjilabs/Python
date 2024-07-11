s1 = """
“'And' and 'or' are the basic operations of logic. Together with 'no' (the logical operation 
of negation) they are a complete set of basic logical operations — all other logical 
operations, no matter how complex, can be obtained by suitable combinations of these.” 
― John von Neumann, The Computer and the Brain
"""

s2 = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit 
esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt 
in culpa qui officia deserunt mollit anim id est laborum.
"""
counts = {}
for c in s1:
    if (ord(c) >= ord('a') and ord(c) <= ord('z')) or (ord(c) >= ord('A') and ord(c) <= ord('Z')):
        counts[c] = counts.get(c, 0) + 1
        
print(counts)

counts = {}
for c in s2:
    if (ord(c) >= ord('a') and ord(c) <= ord('z')) or (ord(c) >= ord('A') and ord(c) <= ord('Z')):
        counts[c] = counts.get(c, 0) + 1
        
print(counts)