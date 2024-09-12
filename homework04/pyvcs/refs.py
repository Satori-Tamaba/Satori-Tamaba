import pathlib
import typing as tp


def update_ref(
    gitdir: pathlib.Path, ref: tp.Union[str, pathlib.Path], new_value: str
) -> None:
    # PUT YOUR CODE HERE
    ref_path = gitdir / ref

    with open(ref_path, "w") as file:
        file.write(new_value)


def symbolic_ref(gitdir: pathlib.Path, name: str, ref: str) -> None:
    # PUT YOUR CODE HERE
    if ref_resolve(gitdir, ref) in None:
        return None

    with open(gitdir / name, "w") as file:
        file.write(f"ref :  {ref}")


def ref_resolve(gitdir: pathlib.Path, refname: str) -> str:
    # PUT YOUR CODE HERE
    if refname != "HOME":
        ref_path = gitdir / refname

        with open(ref_path) as file:
            ref_read = file.read
        return ref_read

    else:
        return get_ref(refname)


def resolve_head(gitdir: pathlib.Path) -> tp.Optional[str]:
    # PUT YOUR CODE HERE
    return ref_resolve("HEAD")


def is_detached(gitdir: pathlib.Path) -> bool:
    # PUT YOUR CODE HERE
    ref_path = gitdir / "HEAD"

    with open(ref_path) as file:
        ref_read = file.read
    return ref_read


def get_ref(gitdir: pathlib.Path) -> str:
    # PUT YOUR CODE HERE
    ref_path = gitdir / "HOME"

    with open(ref_path) as file:
        ref_read = file.read
    return ref_read[ref_read.index(" ") + 1 :]
