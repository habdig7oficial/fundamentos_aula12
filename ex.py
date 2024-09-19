values= "0.23,0.4"

values = values.split(",")

correspondency = {}
for value, i in zip(values,  range(len(values))):
    correspondency[str(i)] = float(value)
    print(value)
print(correspondency)
