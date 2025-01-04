from random import randint

mines_map_example = [[0,1,0,1],
                     [1,0,1,0],
                     [1,1,1,1]]

mines_map_without_bombs = [[0,0,0,0],
                           [0,0,0,0],
                           [0,0,0,0]]

"""mines_max_example[номер подмассива][номер элемента в подмассиве]"""

print(f'Это первый массив: {mines_map_example}') 


"""y
^
|
|
|
|
+---------------> x"""



def print_mines_map(mines_map : [[int]]) -> None:
    for y in range(0,len(mines_map),1):
        for x in range(0,len(mines_map[y]),1):
            print(mines_map[y][x],end='')
        print()


a=[42,13,666]

'''a[0]<len(a) -> false
a[1]
a[2]''' 

def border_for_mines_map(mines_map:[[int]], x:int, y:int) -> int:
    if y >= len(mines_map) or x >= len(mines_map[y]):
       return 0
    if x < 0 or y < 0:
       return 0
    else:
       return mines_map[y][x]

"""print(border_for_mines_map(mines_map_example, 7,5))
print(border_for_mines_map(mines_map_example,-1,-2))"""

def count_of_bombs(mines_map:[[int]],x: int, y:int) -> int:
     bombs_count = \
     border_for_mines_map(mines_map,x,y) + \
     border_for_mines_map(mines_map,x-1,y) + \
     border_for_mines_map(mines_map,x+1,y) + \
     border_for_mines_map(mines_map,x,y+1) + \
     border_for_mines_map(mines_map,x+1,y+1) + \
     border_for_mines_map(mines_map,x-1,y-1) + \
     border_for_mines_map(mines_map,x+1,y-1) + \
     border_for_mines_map(mines_map,x-1,y+1)
     return bombs_count

"""print_mines_map(mines_map_example)"""

print()

def bombs_map(length:int, height:int) ->[[int]]:
    bomb_place = []
    for y in range(0,height,1):
        bomb_place1 = []
        for x in range(0, length,1):
                bomb_place1.append(0)
        bomb_place.append(bomb_place1)
                 # bomb_place=[].append(0)
                 # x = 42+1
    return bomb_place

print("Это карта без бомб")
print_mines_map(bombs_map(3,5))

def print_bombs_map(mines_map:[[int]]) -> [[int]]:
           for y in range(0,len(mines_map),1):
               for x in range(0,len(mines_map[y]),1):
                 print(count_of_bombs(mines_map_example,x,y),end='')
               print()


def creating_maps_of_bombs(mines_map:[[int]],count_of_bombs:int) -> [[int]]:
    for i in range(0,count_of_bombs):
       while True:
        mines_map_bomb_y = randint(0,len(mines_map) - 1)
        mines_map_bomb_x = randint(0,len(mines_map[mines_map_bomb_y]) - 1)
        if mines_map[mines_map_bomb_y][mines_map_bomb_x] == 0: 
            mines_map[mines_map_bomb_y][mines_map_bomb_x]  = 1 
            break
    return mines_map

print_mines_map(creating_maps_of_bombs(mines_map_without_bombs,5))

"""map_of_bombs(mines_map_example)

print(count_of_bombs(mines_map_example,0,0))"""

#print(mines_map)