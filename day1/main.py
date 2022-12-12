def string2int(s):
    return int(s)


f = open("input.txt", "r")
contents = f.read()
elves_string = contents.split("\n\n")
elves_list = [map(string2int,x.strip().split("\n")) for x in elves_string]
elves = [sum(x) for x in elves_list]
topelf = max(elves)
elves.sort(reverse=True)
top3 = sum(elves[0:3])
print(top3)