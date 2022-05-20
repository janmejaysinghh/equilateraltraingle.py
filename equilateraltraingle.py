s=int(input("Enter the first side of the traingle\n"))
s1=int(input("Enter the second side of the traingle\n"))
s2=int(input("Enter the third side of the traingle\n"))
if s==s1 and s1==s2:
 print("Equilateral Traingle")
if (s==s1 and s1!=s2)or(s1==s2 and s1!=s)or(s2==s and s!=s1):
 print("Isoscles Traingle")
if s!=s1 and s!=s2 and s1!=s2:
 print("Scaler Traingle")