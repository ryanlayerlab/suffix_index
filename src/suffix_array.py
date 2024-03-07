import argparse
import utils
import suffix_tree

SUB = 0
CHILDREN = 1

def get_args():
    parser = argparse.ArgumentParser(description='Suffix Tree')

    parser.add_argument('--reference',
                        help='Reference sequence file',
                        type=str)

    parser.add_argument('--string',
                        help='Reference sequence',
                        type=str)

    parser.add_argument('--query',
                        help='Query sequences',
                        nargs='+',
                        type=str)

    return parser.parse_args()

def build_suffix_array(T):
    tree = suffix_tree.build_suffix_tree(T)
    # Your code here
    return None


def search_array(T, suffix_array, q):

    # Your code here

    # binary search
    lo= -1
    hi = len(suffix_array)
    while (hi - lo > 1):
        mid = int((lo + hi) / 2)
        if suffix_array[mid] < q:
            lo = mid
        else:
            hi = mid
    return hi

def main():
    args = get_args()

    T = None

    if args.string:
        T = args.string
    elif args.reference:
        reference = utils.read_fasta(args.reference)
        T = reference[0][1]

    array = build_suffix_array(T)

    if args.query:
        for query in args.query:
            match_len = search_array(array, query)
            print(f'{query} : {match_len}')

if __name__ == '__main__':
    main()
