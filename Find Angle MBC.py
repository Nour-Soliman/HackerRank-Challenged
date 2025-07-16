# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
a=int(input())
b=int(input())
# c=math.sqrt(a**2+b**2)
# d=c/2
# ratio=d/b
# ratio=max(-1.0,min(1.0,ratio))
rad=math.atan2(a,b)
deg=math.degrees(rad)
deg_sign="\u00B0"
print(f"{round(deg)}{deg_sign}")