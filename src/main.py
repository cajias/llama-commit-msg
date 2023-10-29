import json

from gen import explain_diff
from git_diff import staged_diffs
import argparse
from dotenv import load_dotenv


def parse_args():
    # method that parses comamndlne arguments and returns a dictionary of arguments
    parser = argparse.ArgumentParser(description='A tool that generates commit messages from git diffs')
    parser.add_argument('-p', '--path', help='Path to git project', required=True, type=str)
    return vars(parser.parse_args())


# Example usage:
if __name__ == "__main__":
    load_dotenv()
    options = parse_args()
    print(json.dumps(options, indent=4))

    repo_path = "../"
    for diff in staged_diffs(repo_path):
        print(diff["path"])
        print(explain_diff(diff))
