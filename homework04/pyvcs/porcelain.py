import os
import shutil
import pathlib
import typing as tp

from pyvcs.index import read_index, update_index
from pyvcs.objects import commit_parse, find_object, find_tree_files, read_object
from pyvcs.refs import get_ref, is_detached, resolve_head, update_ref
from pyvcs.tree import commit_tree, write_tree


def add(gitdir: pathlib.Path, paths: tp.List[pathlib.Path]) -> None:
    # PUT YOUR CODE HERE
    update_index(gitdir, paths)


def commit(gitdir: pathlib.Path, message: str, author: tp.Optional[str] = None) -> str:
    # PUT YOUR CODE HERE
    return commit_tree(gitdir=gitdir, tree=write_tree(gitdir, read_index(gitdir)), message=message, author=author)


def checkout(gitdir: pathlib.Path, obj_name: str) -> None:
    # PUT YOUR CODE HERE
    if (gitdir / "refs/heads" / obj_name).exists:
        with open(gitdir / "refs/heads" / obj_name, "w") as file:
            obj_name = file.read()
    indexs = read_index(gitdir)

    for i in indexs:
        if pathlib.Path(i.name).is_file():
            name = i.name.split("/")
            if len(name) > 1:
                shutil.rmtree(name[0])
            else:
                os.chmod(file.name, 0o777)
                os.remove(file.name)
    obj_path = gitdir / "objects" / obj_name[:2] / obj_name[2:]

    with open(obj_path) as file:
        commit = file.read()
    for tree in find_tree_files(commit_parse(commit).decode(), gitdir):
        name = tree[0].split("/")

        if len(name) > 1:
            pathlib.Path(name[0]).absolute().mkdir
        with open(tree[0], "w") as file:
            tittle, content = read_object(tree[1], gitdir)
            file.write(content.decode())
