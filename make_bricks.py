# We want to make a row of bricks that is goal inches long.
# We have a number of small bricks (1 inch each) and big bricks
# (5 inches each). Return True if it is possible to make
#  the goal by choosing from the given bricks. This is
# a little harder than it looks and can be done without
# any loops. See also: Introduction to MakeBricks

# make_bricks(3, 1, 8) → True
# make_bricks(3, 1, 9) → False
# make_bricks(3, 2, 10) → True


def make_bricks(small, big, goal):
    goal_small = goal % 5
    goal_big = goal / 5
    big_needed = (goal-small) / 5
    big_needed_leftover = (goal-small) % 5
    if big==goal_big and small >= goal_small:
        return True
    elif big >= big_needed and big_needed_leftover == 0:
        return True
    elif goal - 5*big <= small and goal - 5*big > 0:
        return True
    else:
        return False

def make_bricks2(small, big, goal):
  if big*5 + small < goal:
    return False
  elif goal % 5 > small:
    return False
  else:
    return True


make_bricks(3, 1, 8)


