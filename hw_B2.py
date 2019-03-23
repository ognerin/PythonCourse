s = "AAAACCCGGT"
def revc(s):
    s = s.replace("A", "t")
    s = s.replace("C", "g")
    s = s.replace("G", "c")
    s = s.replace("T", "a")
    s = s[::-1]
    print(s.upper())
revc(s)






