# file (5 lines input)
file=open("input.txt",'w')
print("Enter 5 lines.")
for n in range(1,6):
    line=input(f"Enter line {n}:")
    file.write(line + "\n")
file.close()
print("you can read it in input.txt.")
# to reverse each line
with open("input.txt",'r') as infile, open("output.txt",'w') as outfile:
    for idx, line in enumerate(infile,start=1):
        word=line.strip().split()
        reverse_words=word[::-1]
        reversed_line=' '.join (reverse_words)
        outfile.write(f"{idx} : {reversed_line}\n")
print("Reversed word are saved to output.txt")


