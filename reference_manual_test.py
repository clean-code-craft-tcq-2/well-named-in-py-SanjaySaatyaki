import reference_manual as manual
import even_count_color_generator as generator

def test_get_all_color_codes():
    contents = manual.get_all_color_codes()
    for content in contents:
        pairNumber = content.split(' ')[0].strip()
        color_code = content.split(' ')[1:-1]
        major_color, minor_color = generator.get_color_from_pair_number(int(pairNumber))
        assert( major_color in color_code)
        assert( minor_color in color_code)