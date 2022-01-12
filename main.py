from even_count_color_generator_test import excute_testcases
from reference_manual_test import test_get_all_color_codes
import reference_manual as manual

if __name__ == '__main__':
  excute_testcases()
  manual.print_color_code()
  test_get_all_color_codes()
  print('Done :)')
