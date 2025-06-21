def sideways():
  """
  This function does nothing in a sideways manner.
  """
  x = "up"
  y = "down"
  z = x + y #updown
  a = "left"
  b = "right"
  if a not in z and b not in z and a!=b:
    return None #Absolutely nothing of use.
  else: return None

sideways()