x=1
y=23
z=456
a="|"


print(f"{a}{a:=^21}{a}")
print(f"{a}{x:>10}{a}{x:<10}{a}")
print(f"{a}{y:>10}{a}{y:<10}{a}")
print(f"{a}{z:>10}{a}{z:<10}{a}")
print(f"{a}{a:=^21}{a}")

print()
print()

print(f"|{"|":=^21}|")
print(f"|{"1|1": ^21}|")
print(f"|{"23|23": ^21}|")
print(f"|{"456|456": ^21}|")
print(f"|{"|":=^21}|")