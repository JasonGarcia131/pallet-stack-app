"""
a program that accepts user input for any number of box dims(l,w,h).
the program will take all the box dims and calculte the 
most efficient way to stack the boxes given l,w,h limits(pallet dims)

ex: (l1,w1,h1) + (l2,w2,h2) +... <= 48
    (l1,w1,h1) + (l2,w2,h2) +... <= 40
    (l1,w1,h1) + (l2,w2,h2) +... <= {ex:70} (this value will be from user input)


"""


print('--------Box1---------')
l1 = float(input('enter length'))
w1 = float(input('enter width'))
h1 = float(input('enter heigth'))
box1 = [l1,w1,h1]

print('--------Box2---------')
l2 = float(input('enter length'))
w2 = float(input('enter width'))
h2 = float(input('enter heigth'))
box2 = [l2,w2,h2]

# # print('--------Box3---------')
# l3 = float(input('enter length'))
# w3 = float(input('enter width'))
# h3 = float(input('enter heigth'))
# box3 = [l3,w3,h3],


def max_box_fun(*boxes):
    max_box_dim = [boxes]
    return max_box_dim

pallet_dims_l = 48
pallet_dims_w = 40
pallet_dims_max_height = float(input('Max height: '))

from itertools import combinations

def max_width():
    # perm = permutations(max_box_fun(box1,box2))
    print(f'max width: {list(combinations(max_box_fun(box1,box2),3))}')
    # for l in perm:
        # print(l)
        # if(lenght <= 6):
        #     print('Under')
        # else:
        #     print('Over')
        

print(max_width())

# find out more about permutations and combinations. plan out the logic on paper first

# (l1,w1,h1) + (l2,w2,h2) +... = 48
# (l1,w1,h1) + (l2,w2,h2) +... = 40
# (l1,w1,h1) + (l2,w2,h2) +... = given by the user

# possible_length = [(l1,w1,h1), (l2,w2,h2), ...]

# for l in possible_length:
    # sum(l.combinations())