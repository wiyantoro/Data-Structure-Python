import random

gmbr_dadu = {
    1: ("┌─────────┐",
        "│         │",
        "│    0    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  0      │",
        "│         │",
        "│      0  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  0      │",
        "│    0    │",
        "│      0  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  0   0  │",
        "│         │",
        "│  0   0  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  0   0  │",
        "│    0    │",
        "│  0   0  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  0   0  │",
        "│  0   0  │",
        "│  0   0  │",
        "└─────────┘")
}

dadu = []
total = 0
nilai_dadu = int(input("Berapa Banyak Dadu: "))

for i in range(nilai_dadu):
    dadu.append(random.randint(1, 6))


for line in range(5):
    for i in dadu:
        print(gmbr_dadu.get(i)[line], end="")
    print()

for i in dadu:
    total += i
print(f"banyak Dadu: {total}")