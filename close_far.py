# Given three ints, a b c, return True if one of b or c is "close"
# (differing from a by at most 1), while the other is "far",
# differing from both other values by 2 or more.
# Note: abs(num) computes the absolute value of a number.

# close_far(1, 2, 10) → True
# close_far(1, 2, 3) → False
# close_far(4, 1, 3) → True


def check_distance(x,y,z):
  if abs(x-y)<=1:
    if abs(y-z) > 1 and abs(x-z) > 1:
      return True
    else:
      return False

def close_far(a, b, c):
  if check_distance(a, b, c) is True:
    return True
  elif check_distance(b,c,a) is True:
    return True
  elif check_distance(c, a, b) is True:
    return True
  else:
    return False