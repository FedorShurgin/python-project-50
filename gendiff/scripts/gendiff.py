import argparse
from gendiff.generate_diff import generate_diff, parse, building_diff


def main():
    parser = argparse.ArgumentParser(description="Compares two configuration files and shows a difference.")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()
    data1 = parse(args.first_file)
    data2 = parse(args.second_file)
 
    buid_diff = building_diff(data1, data2)
    #print(buid_diff)
    
    str_diff = generate_diff(buid_diff, depth=0)
    print(str_diff)
    

if __name__ == '__main__':
    main()
