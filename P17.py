name = input("Enter String ")
 
even_char = ""
for i in range(len(name)):
    if i % 2 == 0:
        even_char += name[i]
 
print("Characters at even index:", even_char)
