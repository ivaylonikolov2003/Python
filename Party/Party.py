class Party:
    def __init__(self):
        self.guests = []

party = Party()
command = input()

while command != "End":
    party.guests.append(command)
    command = input()

print(f"Going: {','.join(party.guests)}")
print(f"Total: {len(party.guests)}")