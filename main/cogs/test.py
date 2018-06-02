

with open("tags.txt","r") as myfile:
    for line in myfile:
        linetoedit = line

    print(linetoedit)
    lines = []
    for line in myfile:
        lines.append(line.rstrip().split(" HELLOTHEREIAMADIVIDER "))
    print(lines)
    for line in myfile:
        currentline = line.rstrip().split(" HELLOTHEREIAMADIVIDER ")
    

    


        
 
