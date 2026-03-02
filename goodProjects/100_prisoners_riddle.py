import random

def iterate(box_num, prisoner_num):
    global succeeded_prisoners, tries
    tries += 1
    if prisoner_num == boxes[box_num]:
        succeeded_prisoners += 1
    elif tries < 50:
        iterate(boxes[box_num], prisoner_num)

boxes = [i for i in range(0, 100)]
prisoners = boxes.copy()
random.shuffle(boxes)
succeeded_prisoners = 0
prisoner_tries = []

for prisoner in prisoners:
    current_box = prisoner
    tries = 0
    iterate(current_box, current_box)
    prisoner_tries.append(tries)

executed = "No" if succeeded_prisoners == 100 else "Yes"

print(f"Number of prisoners who succeeded: {succeeded_prisoners}")
print(f"Executed: {executed}")
print("Prisoner's tries:")
print(*prisoner_tries)