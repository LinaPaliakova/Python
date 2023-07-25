import random
def print_map(p_map):
    print('\n'.join([' '.join(['{:2}'.format(item) for item in row]) for row in p_map]))

map1 = [["⬜️","️⬜️","️⬜️"],["⬜️","️⬜️","️⬜️"],["⬜️","️⬜️","️⬜️"]]
print("This is our initial map...")
print_map(map1)

number = input("What do you think: where is the Golden Star in the map? ")

coordinate1 = int(number[0])
coordinate2 = int(number[1])
star_coordinate1 = random.randint(0,2)
star_coordinate2 = random.randint(0,2)

map1[coordinate1 - 1][coordinate2 - 1] = "🆇"
map1[star_coordinate1][star_coordinate2] = "⭐️"
if map1[coordinate1][coordinate2] == map1[star_coordinate1][star_coordinate2]:
  print("Congratulations!!! You have found the Golden STAR!")
else:
  print("Unfortunatly you could find it 🙁")
print_map(map1)
