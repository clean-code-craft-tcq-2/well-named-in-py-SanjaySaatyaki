from color_codes import MAJOR_COLORS,MINOR_COLORS
import color_codes as colors

def get_color_from_pair_number(pair_number):
  '''
  Description : Based on the even count color code it will return both major and minor color for the pair
  Input Params : pair_number (int)
  Output Params : major_color and minor color (str)
  '''  
  zero_based_pair_number = pair_number - 1
  major_index = zero_based_pair_number // len(MINOR_COLORS)
  if major_index >= len(MAJOR_COLORS):
    raise Exception('Major index out of range')
  minor_index = zero_based_pair_number % len(MINOR_COLORS)
  if minor_index >= len(MINOR_COLORS):
    raise Exception('Minor index out of range')
  return MAJOR_COLORS[major_index], MINOR_COLORS[minor_index]

def get_pair_number_from_color(major_color, minor_color):
  '''
  Description : Based on the even count color code it will give the pair number for the major and minor colors
  Input Params : major_color, minor_color (str)
  Output Params : pair_number
  '''  
  try:
    major_index = MAJOR_COLORS.index(major_color)
  except ValueError:
    raise Exception('Major index out of range')
  try:
    minor_index = MINOR_COLORS.index(minor_color)
  except ValueError:
    raise Exception('Minor index out of range')
  return major_index * len(MINOR_COLORS) + minor_index + 1
