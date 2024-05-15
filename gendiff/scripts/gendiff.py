import argparse
from gendiff.generate_diff import generate_diff
from gendiff.parser import parse


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
        )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument(
        '-f',
        '--format',
        type=str,
        default='stylish',
        help='set format of output'
    )

    args = parser.parse_args()
    data1 = parse(args.first_file)
    data2 = parse(args.second_file)
    format_data = args.format

    str_diff = generate_diff(data1, data2, format_data)
    print(str_diff)


if __name__ == '__main__':
    main()

'''
generate_diff принимает пути
main с 7 по 14 отдельная функция, эту функцию поместить в парссер(cli.py)
пакет(папка) formatters - to json to plain to json убрать приставку to
generate_diff условия сделать отдельной функцией
'''
