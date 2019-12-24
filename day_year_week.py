#Description : Write a program to convert days into years, weeks and days.

days=int(input("Enter days: "))
years=days//365
weeks=(days%365)//7
days=days-((years*365)+(weeks*7))

print("Year is: ",years)
print("Weeks is: ",weeks)
print("Days is: ",days)
