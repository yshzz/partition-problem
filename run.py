import argparse
from list_partition import is_partitionable


def main():
    parser = argparse.ArgumentParser(description="Partition Problem")
    parser.add_argument(
        '-l',
        '--list',
        help='Arbitrary list of positive integers of any length and in any order',
        required=True,
        nargs='+',
        type=int
    )
    nums = parser.parse_args().list
    print(f'List: {nums}')
    print(f'Is partitionable: {is_partitionable(nums)}')


if __name__ == '__main__':
    main()
