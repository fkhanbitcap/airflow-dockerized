"""
Main
-------------
"""
import argparse
from devchallenge import __version__
import devchallenge.punk.punk


def get_parser():
    """
    Creates a new argument parser.
    """
    parser = argparse.ArgumentParser('devchallenge')
    version = '%(prog)s ' + __version__
    parser.add_argument('--version', '-v', action='version', version=version)
    return parser


def main(args=None):
    """
    Main entry point for your project.

    Args:
        args : list
            A of arguments as if they were input in the command line. Leave it
            None to use sys.argv.
    """

    parser = get_parser()
    args = parser.parse_args(args)

    # Put your main script logic here
    # print('No action defined for devchallenge module!')

    # import json
    # print(
    #     json.dumps(devchallenge.punk.punk.get_beer_by_id("193"),
    #                indent=4))

    # import json
    # print(
    #     json.dumps(devchallenge.punk.punk.get_beer_by_name("B "),
    #                indent=4))

    import json
    print(
        json.dumps(devchallenge.punk.punk.get_beer_brewed_in("10-2011", "10-2020"),
                   indent=4))


if __name__ == '__main__':
    main()
