from src.gen import explain_diff
from src.git_diff import staged_diffs

# Example usage:
if __name__ == "__main__":
    repo_path = "../"
    for diff in staged_diffs(repo_path):
        print(diff["path"])
        print(explain_diff(diff))
