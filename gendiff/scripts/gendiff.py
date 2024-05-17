from gendiff.generate_diff import generate_diff
from gendiff.cli import cli


def main():
    args = cli()
    str_diff = generate_diff(args.first_file, args.second_file, args.format)
    print(str_diff)


if __name__ == '__main__':
    main()
