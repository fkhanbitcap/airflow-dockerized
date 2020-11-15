"""
Main
----
"""
import json
import argparse
from devchallenge import __version__
from devchallenge import punk_requests


def parse_arguments():
    """
    Creates a new argument parser.
    """
    parser = argparse.ArgumentParser("devchallenge")
    parser.add_argument('--version', '-v', action='version', version='%(prog)s ' + __version__)

    sub_parser = parser.add_subparsers(dest="sub", required=True)

    by_name = sub_parser.add_parser("byname", help="String beer name information as partial or full match")
    by_name.add_argument("--name", "-n", type=str, help="Name as string", required=True)

    by_id = sub_parser.add_parser("byid", help="Str exact id or ids in (id|id|...) format")
    by_id.add_argument("--id", "-i", type=str, help="id as string", required=True)

    by_id = sub_parser.add_parser("byinterval", help="Get beer brewed in interval")
    by_id.add_argument("--from-date", "-f", type=str, help="date i.e. 10-11", required=True)
    by_id.add_argument("--until-date", "-u", type=str, help="date i.e. 10-11", required=True)

    return parser.parse_args()


if __name__ == '__main__':
    """
    Main entry point for your project.
    """
    args = parse_arguments()

    if args.sub == "byname":
        print(json.dumps(punk_requests.get_beer_by_name(args.name),
                         indent=4))

    elif args.sub == "byid":
        print(json.dumps(punk_requests.get_beer_by_id(args.id),
                         indent=4))

    elif args.sub == "byinterval":
        print(json.dumps(punk_requests.get_beer_brewed_in(args.from_date, args.until_date),
                         indent=4))
