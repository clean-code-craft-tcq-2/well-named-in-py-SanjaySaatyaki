from color_codes import MAJOR_COLORS,MINOR_COLORS,color_pair_to_string
from even_count_color_generator import get_color_from_pair_number

def print_color_code():
  print("Reference Manual")
  print("{:<15} {:<15}".format('Pair Number', 'Major Minor ColorPairs'))
  color_codes = get_all_color_codes()
  for color_code in color_codes:
    print(color_code)

def get_all_color_codes():
  color_codes = []
  no_of_pairs = len(MAJOR_COLORS)*len(MINOR_COLORS)+1
  for pair_number in range(1,no_of_pairs):
    major_color , minor_color = get_color_from_pair_number(pair_number)
    color_pair_code = color_pair_to_string(major_color,minor_color)
    color_codes.append("{:<15} {:<15} ".format(pair_number, color_pair_code))
  return color_codes