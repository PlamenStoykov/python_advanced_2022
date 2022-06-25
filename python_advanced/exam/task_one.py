from collections import deque

eggs = deque(map(int, input().split(', ')))
pieces_of_paper = deque(map(int, input().split(', ')))
filled = 0
while eggs and pieces_of_paper:
    egg = eggs.popleft()
    piece = pieces_of_paper.pop()
    if egg <= 0:
        pieces_of_paper.append(piece)
        continue
    if egg == 13:
        first = pieces_of_paper.popleft()
        pieces_of_paper.appendleft(piece)
        pieces_of_paper.append(first)
        continue
    if egg + piece <= 50:
        filled += 1
if filled > 0:
    print(f"Great! You filled {filled} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")
if eggs:
    print(f"Eggs left: {', '.join([str(i) for i in eggs])}")
if pieces_of_paper:
    print(f"Pieces of paper left: {', '.join([str(i) for i in pieces_of_paper])}")
