answers = {
    "animal": "Panthera tigris",
    "tree": "Pinus densiflora",
    "flower": "Forsythia koreana"
}

while True:
    q = input()
    if q == "end":
        break
    print(answers[q])
