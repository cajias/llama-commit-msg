import git


def staged_diffs(path: str):
    modified_files = []
    try:
        repo = git.Repo(path)
        for diff in repo.index.diff(None).iter_change_type("M"):
            content = diff.a_blob.data_stream.read().decode('utf-8')
            if not content:
                continue
            modified_files.append({
                "path": diff.a_path,
                "content": content
            })
        return modified_files

    except git.InvalidGitRepositoryError:
        print(f"Error: {path} is not a valid Git repository.")
    except git.NoSuchPathError:
        print(f"Error: {path} does not exist.")

