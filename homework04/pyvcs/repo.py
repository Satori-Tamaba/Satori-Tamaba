import os
import pathlib
import typing as tp


def repo_find(workdir: tp.Union[str, pathlib.Path] = ".") -> pathlib.Path:
    # PUT YOUR CODE HERE
    ...
    work_dir = pathlib.Path(workdir)
    git_dir = os.environ("GIT_DIR") or ".git"
    path = work_dir / git_dir

    for path in path.parents:
        if dir.name == git_dir:
            return dir

    raise "Not founded"


def repo_create(workdir: tp.Union[str, pathlib.Path]) -> pathlib.Path:
    # PUT YOUR CODE HERE
    work_dir = pathlib.Path(workdir)
    if not work_dir.is_dir:
        raise Exception(f"{work_dir} not funded")

    git_dir = os.environ("GIT_DIR") or ".git"
    path = work_dir / git_dir

    try:
        path.mkdir(parents=True), (path / "refs" / "tags").mkdir(parents=True), (
            path / "refs" / "heads"
        ).mkdir(parents=True), (path / "objects").mkdir(parents=True),
    except:
        print("EXIST")
    with open(path / "HEAD", "w") as head, open(path / "config", "w") as config, open(
        path / "despription"
    ) as description:
        head.write("ref: refs/heads/master\n")
        config.write(
            "[core]\n\trepositoryformatversion = 0\n\tfilemode = true\n\tbare = false\n\tlogallrefupdates = false\n"
        )
        description.write("Unnamed pyvcs repository")
    return path
