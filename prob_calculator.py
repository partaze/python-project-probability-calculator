import copy
import random

class Hat:
  """@AUTHOR Cheryl Vadivello.
  Class Hat instantiates a Hat object which contains different 
  coloured balls.
  
  The number and color of balls are assigned upon hat creation
  depending on the arguments passed to the constructor.
  This class randomly draws a given number of colored balls."""

  def __init__(self,**balls):
    """Attributes
       ----------
    contents : list, color of each individual ball
    """
    if len(balls) == 0 :
      raise Exception("Minimum of 1 ball is needed to make a hat.")
    else:
      self.contents = []
      ball_color = [*balls]
      for color in ball_color :
        i = balls[color]
        self.contents += [color]*i

  def draw(self,num_balls) :
    """Draws a given number of balls from the hat at random
    without putting them back. Hence, reduces the number of balls
    in the hat."""
    
    if num_balls > len(self.contents) :
      drawn = copy.copy(self.contents)
      self.contents.clear()
    else:
      drawn =[]
      for i in range(num_balls):
        j= random.randint(0,len(self.contents)-1)
        drawn.append(self.contents[j])
        del self.contents[j]
    
    return drawn  
      

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  """ This function calculates the probability of drawing a given minimum number
  of different colored balls from a specified number of trials.
  """
  
  match = 0 
  for i in range(num_experiments):
    drawn = Hat.draw(copy.deepcopy(hat),num_balls_drawn)  
    drawn_balls = makeDict(drawn)
    match_check = []
    for item in expected_balls: 
      if item not in drawn_balls.keys():
        break
      if item in drawn_balls.keys() and drawn_balls[item]>= expected_balls[item]:
        match_check.append("match")
        if len(match_check) == len(expected_balls):
          match += 1
        else:
          continue
  probability = match/num_experiments
  return probability

def makeDict(drawn):
  """Populates a dictionary from the list of balls drawn."""
  drawn_balls ={}
  for ball in drawn :
    if ball in drawn_balls :
       drawn_balls[ball] += 1
    else:
       drawn_balls[ball] = 1

  return drawn_balls
