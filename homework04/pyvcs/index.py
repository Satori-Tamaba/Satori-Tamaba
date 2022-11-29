import hashlib
import operator
import os
import pathlib
import struct
import typing as tp

from pyvcs.objects import hash_object


class GitIndexEntry(tp.NamedTuple):
    # @see: https://github.com/git/git/blob/master/Documentation/technical/index-format.txt
    ctime_s: int
    ctime_n: int
    mtime_s: int
    mtime_n: int
    dev: int
    ino: int
    mode: int
    uid: int
    gid: int
    size: int
    sha1: bytes
    flags: int
    name: str

    def pack(self) -> bytes:
        # PUT YOUR CODE HERE
        values = (
            self.ctime_s,
            self.ctime_n,
            self.mtime_s,
            self.mtime_n,
            self.dev,
            self.ino,
            self.mode,
            self.uid,
            self.gid,
            self.size,
            self.sha1,
            self.flags,
            self.name.encode(),
        )

        return struct.pack(f">10i20sh{len(self.name)}s3x", *values)

    @staticmethod
    def unpack(data: bytes) -> "GitIndexEntry":
        # PUT YOUR CODE HERE
        unpack_list = list(struct.unpack(f"!10i20sh{len(data) - 62}s"), data)
        unpack_list[-1] = unpack_list[-1][:-3].decode

        return GitIndexEntry(*unpack_list)


def read_index(gitdir: pathlib.Path) -> tp.List[GitIndexEntry]:
    # PUT YOUR CODE HERE
    list = []
    path = gitdir / "index"

    try:
        with open(path) as file:
            content = file.read()

    except:
        return list

    bytes_count = int.from_bytes(content[8:12])

    result = content[12:-20]

    count = 0

    for i in range(bytes_count):
        start = count + 62
        finish = result[start:].index(b"\x00\x00\x00") + start + 3
        list.append(GitIndexEntry.unpack(result[count:finish]))
        count = finish
    return list


def write_index(gitdir: pathlib.Path, entries: tp.List[GitIndexEntry]) -> None:
    # PUT YOUR CODE HERE
    with open(gitdir / "index", "w") as file:
        values = (b"DIRC", 2, len(entries))

        hash_data = struct.pack(f">4s2i", values)
        file.write(hash_data)

        for i in entries:
            file.write(i.pack())
            hash_data += i.pack()
        hash_data_2 = str(hashlib.sha1(hash_data).hexdigest)

        file.write(
            struct.pack(
                f">{len(bytearray.fromhex(hash_data_2))}s",
                bytearray.fromhex(hash_data_2),
            )
        )


def ls_files(gitdir: pathlib.Path, details: bool = False) -> None:
    # PUT YOUR CODE HERE
    for i in read_index(gitdir):
        if details:
            print(f"{oct(i.mode)[2:]} {i.sha1.hex()} 0	{i.name}")
        else:
            print(i.name)


def update_index(gitdir: pathlib.Path, paths: tp.List[pathlib.Path], write: bool = True) -> None:
    # PUT YOUR CODE HERE
    if (gitdir / "index").exists:
        list = read_index(gitdir)
    else:
        list = []
    for i in paths:
        with open(i) as file:
            sha = hash_object(file.read(), "blob", True)
            stat = os.stat(i)
            list.append(
                GitIndexEntry(
                    ctime_s=int(stat.st_ctime),
                    ctime_n=0,
                    mtime_s=int(stat.st_mtime),
                    mtime_n=0,
                    dev=stat.st_dev,
                    ino=stat.st_ino,
                    mode=stat.st_mode,
                    uid=stat.st_uid,
                    gid=stat.st_gid,
                    size=stat.st_size,
                    sha1=bytes.fromhex(sha),
                    flags=7,
                    name=str(i).replace("\\", "/"),
                )
            )
    list = sorted(list, key=lambda x: x.name)
    write_index(gitdir, list)
