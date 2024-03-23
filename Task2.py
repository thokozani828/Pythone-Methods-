"""Task 2: Comprehensions (lists and sets).

§ 
§ 
§ 
§ """

#The libraries is using the codes 14, 15, 16, 17, 18, 19, 20 to all programming related books:

codes = [14, 15, 16, 17, 18, 19, 20]

#Create a normal and comprehensive list that will display the codes.

codesN  = []

for i in codes:
    codesN.append(i)

print ("The normal lis that display the codes : ",codesN)

codesC = [c for c in codes]

print ("The comrehansive list codes: ", codes)

#Create a normal list that will add the codes together for auditing purpose.

addCodesN =[]
sumN =0

for n in codes:
    sumN = sumN + n

addCodesN.append(n)

print ("The total of the normal adding list: ", sumN)

#Creat a comprehensive list that will add the codes together for auditing purpose.

sumC = 0

addCodesC = [sumC := sumC + cComp for cComp in codes]

print("A comprehensive list that add the codes together for auditing purpose: ",addCodesC)

#Create a normal list that will display only codes that are tracked by odd numbers.

oddCodesN = []

for oN in codes:
    if oN%2 != 0:
        oddCodesN.append(oN)

print("A normal list that display only codes that are tracked by odd numbers: ",oddCodesN)


#Create a comprehensive list that will display only codes that are tracked by odd numbers.

oddCodesC = [oC for oC in codes if oC%2 !=0]

print ("A comprehensive list that display only codes that are tracked by odd numbers: ", oddCodesC)

#Create a set to display the list of codes

setList = set(codes)
print (" a set to display the list of codes: ", setList)