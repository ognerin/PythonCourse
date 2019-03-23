with open('rosalind_rna.txt', 'r') as file:
    t = file.read()
print(t.replace("T", "U"))
