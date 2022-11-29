import hashlib
import os
import pathlib
import re
import stat
import typing as tp
import zlib

from pyvcs.refs import update_ref
from pyvcs.repo import repo_find


def hash_object(data: bytes, fmt: str, write: bool = False) -> str:
    # PUT YOUR CODE HERE
    str_encode = f"{fmt}{len(data)}\0".encode() + data
    hash = hashlib.sha1(str_encode).hexdigest
    if write:
        hash_name, hash_info = hash[:2], hash[2:]

        git_dir = repo_find()

        with open(git_dir / "objects" / hash_name / hash_info, "w") as file:
            file.write(zlib.compress(str_encode))
    return hash


def resolve_object(obj_name: str, gitdir: pathlib.Path) -> tp.List[str]:
    # PUT YOUR CODE HERE
    if not 4 <= len(obj_name) <= 40:
        raise Exception(f"{obj_name} is incorrect name")
    objects = []
    git_dir = repo_find
    objects_path = gitdir / "object" / obj_name[:2]

    for obj_path in objects_path.iterdir:
        if obj_path.name.index(obj_name[2:]) == 0:
            objects.append(obj_name[2:] + obj_path.name)
    if len(objects) != 0:
        return objects
    else:
        raise Exception(f"{obj_name} is incorrect name")


def find_object(obj_name: str, gitdir: pathlib.Path) -> tp.Optional[str]:
    # PUT YOUR CODE HERE
    if obj_name[2:] in str(gitdir.parts[-1]):
        return f"{gitdir[-2]}{gitdir[-1]}"
    else:
        return None


def read_object(sha: str, gitdir: pathlib.Path) -> tp.Tuple[str, bytes]:
    # PUT YOUR CODE HERE
    path = gitdir / "objects" / sha[:2] / sha[2:]

    with open(path) as file:
        content = zlib.decompress(file.read)
    i = content.index(b"x\00")
    head = content[:i]
    fmt = head[: head.index(b" ")]
    data = content[i + 1 :]
    return fmt.decode, data


def read_tree(data: bytes) -> tp.List[tp.Tuple[int, str, str]]:
    # PUT YOUR CODE HERE)
    result_arr = []

    while len(data) != 0:
        classification = int(data[: data.index(b" ")].decode())
        data = data[data.index(b" ") + 1 :]
        name = data[: data.index(b"x\00")].decode()
        data = data[data.index("b\x00") + 1 :]
        sha = bytes.hex(data[:20])
        data = data[20:]
        result_arr.append(classification, name, sha)
    return result_arr


def cat_file(obj_name: str, pretty: bool = True) -> None:
    # PUT YOUR CODE HERE
    git_dir = repo_find()


def find_tree_files(tree_sha: str, gitdir: pathlib.Path) -> tp.List[tp.Tuple[str, str]]:
    result_arr = []
    head, data = read_object(tree_sha, gitdir)
    for i in read_tree(data):
        if read_object(i[2], gitdir)[0] == "tree":
            tree = find_tree_files(i[2], gitdir)
            for bl in tree:
                name = i[1] + "/" + bl[0]
                result_arr.append(name, bl[1])
        else:
            result_arr.append(i[1], i[2])
    return result_arr


def commit_parse(raw: bytes, start: int = 0, dct=None) -> int:
    # PUT YOUR CODE HERE
    data = zlib.decompress(raw)
    idx = data.index(b"tree")
    return data[idx + 5, idx + 45]
