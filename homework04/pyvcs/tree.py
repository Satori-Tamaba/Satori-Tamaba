import os
import pathlib
import stat
import time
import typing as tp

from pyvcs.index import GitIndexEntry, read_index
from pyvcs.objects import hash_object
from pyvcs.refs import get_ref, is_detached, resolve_head, update_ref


def write_tree(
    gitdir: pathlib.Path, index: tp.List[GitIndexEntry], dirname: str = ""
) -> str:
    # PUT YOUR CODE HERE
    result = b""
    for file in index:
        if "/" in file.name:
            result += b"40000 "
            dir_tittle = file.name[: file.name.find("/")]
            result += dir_tittle.encode() + b"\0"
            next_files = oct(file.mode)[2:].encode() + b" "
            next_files += file.name[file.name.find("/") + 1 :].encode() + b"\0"
            next_files += file.sha1
            sha = hash_object(next_files, fmt="tree", write=True)
            result += bytes.fromhex(sha)
        else:
            result += oct(file.mode)[2:].encode() + b" "
            result += file.name.encode() + b"\0"
            result += file.sha1
    return hash_object(result, fmt="tree", write=True)


def commit_tree(
    gitdir: pathlib.Path,
    tree: str,
    message: str,
    parent: tp.Optional[str] = None,
    author: tp.Optional[str] = None,
) -> str:
    # PUT YOUR CODE HERE
    if author is None:
        author = f'{os.environ["GIT_AUTHOR_NAME"] <{os.environ["GIT_AUTHOR_EMAIL"]}}'
    timestamp = int(time.mktime(time.localtime()))
    if time.timezone < 0:
        time_value = "+"
    else:
        time_value = "-"
    hours = abs(time.timezone // 3600)
    if hours < 10:
        hours_value = "0" + str(hours)
    else:
        hours_value = hours
    seconds = abs((time.timezone // 60) % 60)
    if seconds < 10:
        secs_value = "0" + str(seconds)
    else:
        secs_value = seconds
    commit = f"tree {tree}\n"
    time_owner = f"{timestamp} {time_value}{hours_value}{secs_value}"
    if parent:
        commit += f"parent {parent}\n"
    commit += (
        f"author {author} {time_owner}\ncommitter {author} {time_owner}\n{message}\n"
    )
    hash = hash_object(commit.encode("ascii"), "commit", True)
    return hash
