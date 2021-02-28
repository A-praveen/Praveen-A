file=open('sample_input.txt',"r") # opening a input file sample_input.txt
lines=file.readlines() #read file 
goodies=[] # initializing a list
num_of_emp=int(lines[0][-2])  #num of employee
for i in range(4,len(lines)):
    l=lines[i].split(":") #spliting the name and variable using :(colon)i.e['Fitbit Plus: 7980'] to ['Fitbit Plus', 7980]
    goodies.append([l[0],int(l[1])])
    #print(goodies)
goodies=sorted(goodies,key=lambda x:x[1]) #sorted the list
#print("goodies",goodies)
min_diff=float('inf') #maximum value assigned to min_diff
for i in range(0,len(goodies)-num_of_emp+1):
    diff=goodies[i+num_of_emp-1][1]-goodies[i][1]
    #print("diff",diff)

    if diff<min_diff:
        min_index=i
        min_diff=diff
        mins=str(min_diff)
        goods=str(goodies)
file1=open('sample_output.txt',"w") #opening a new file sample_output.txt to write the data
file1.write("Number of the employees: ")
employee=str(num_of_emp)
file1.write(employee)
file1.write('\n')
file1.write('\n')
file1.write("Here the goodies that are selected for distribution are\n")
for i in range(min_index,min_index+num_of_emp):
    #result=str(goodies[i])
    #str1=result[i]
    #file1.write(str1)
    name=goodies[i][0]
    value=goodies[i][1]
    final=name+": "+str(value) # assigning the goodies name and value  
    file1.write(final) 
    file1.write('\n')
file1.write('\n')    
file1.write("And the difference between the chosen goodie with highest price and the lowest price is ")    
file1.write(mins) # printing the difference value between the highest price and the lowest price
file.close() #closing file i.e sample_input.txt file
file1.close() #closing file i.e sample_output.txt file

