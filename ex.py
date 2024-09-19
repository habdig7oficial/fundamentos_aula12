values= "0.80, 0.12, 0.01, 0.22, 0.35, 0.25, 0.77, 0.50, 0.53, 0.45"
n = 5

values = values.split(",")

correspondency = {}
for value, i in zip(values,  range(len(values))):
    correspondency[str(i)] = float(value)
    print(value)
print(correspondency)

ordered = dict(sorted(correspondency.items(), reverse = True, key= lambda item: item[1]))
print(ordered)

res = []
for i in ordered:
    res.append(i)

p = "".join(res)
print(p[0:n])
