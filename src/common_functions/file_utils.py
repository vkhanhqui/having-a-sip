import json
from os import listdir, makedirs
from os.path import exists, isfile, join
from typing import List, Union


def create_dir(
    dirname: str
) -> None:
    '''Create a new directory if not existed.

    :param dirname: The relative path or absolute path
        you want your directory in.

    Example::

        # Example generated from non-compiling source. May contain errors.
        from common_functions import file_utils

        dirname: str = "root_dir/example_dir"
        file_utils.create_dir(
            dirname=dirname
        )
        # example_dir is created at the root_dir path
    '''
    is_existed = exists(dirname)
    if not is_existed:
        makedirs(dirname)


def parse_bytes_to_str(
    any_bytes: bytes
) -> str:
    '''Parse bytes to str.

    :param any_bytes: The bytes you want to parse.

    Example::

        # Example generated from non-compiling source. May contain errors.
        from common_functions import file_utils

        any_bytes: bytes = b"example_bytes"
        file_utils.parse_bytes_to_str(
            any_bytes=any_bytes
        )
        >>> "example_bytes"
    '''
    resp = any_bytes.decode("utf-8")
    return resp


def dump_file(
    filename: str,
    content: Union[str, bytes, list, dict],
) -> None:
    '''Dump the content to a new file.

    :param filename: The relative path or absolute path
        you want your file in.
    :param content: The dumped content.

    Example::

        # Example generated from non-compiling source. May contain errors.
        from common_functions import file_utils

        filename: str = "root_path/new_file.txt"
        content: str = "example content"
        file_utils.dump_file(
            filename=filename,
            content=content,
        )
    '''
    dumped_content = content
    if isinstance(dumped_content, bytes):
        dumped_content = parse_bytes_to_str(dumped_content)
    with open(filename, "w") as f:
        if isinstance(dumped_content, (list, dict)):
            dumped_content = json.dumps(content, indent=4)
            f.write(dumped_content)
        else:
            f.write(dumped_content)


def read_file(
    filename: str,
    is_json: bool = False,
) -> Union[str, List[dict], dict]:
    '''Read a file.

    :param filename: The relative path or absolute path your file in.
    :param is_json: Whether your file is json or not. Default False.

    Example::

        # Example generated from non-compiling source. May contain errors.
        from common_functions import file_utils

        filename: str = "root_path/new_file.txt"
        file_utils.read_file(
            filename=filename,
        )
        >>> "example response"
    '''
    response_file = ""
    with open(filename, "r") as f:
        if is_json:
            response_file = json.loads(read_file(filename))
        else:
            response_file = f.read()
    return response_file


def get_filenames(
    dirname: str,
) -> List[str]:
    '''Read all filenames in a directory.

    :param dirname: The relative path or absolute path your directory in.

    Example::

        # Example generated from non-compiling source. May contain errors.
        from common_functions import file_utils

        dirname: str = "root_path/your_directory"
        file_utils.get_filenames(
            dirname=dirname,
        )
        >>> ["example_filename_1.txt", "example_filename_2.html"]
    '''
    filenames = [
        f for f
        in listdir(dirname)
        if isfile(join(dirname, f))
    ]
    return filenames


def read_files(
    dirname: str,
) -> List[tuple]:
    '''Read all files in a directory.

    :param dirname: The relative path or absolute path your directory in.

    Example::

        # Example generated from non-compiling source. May contain errors.
        from common_functions import file_utils

        dirname: str = "root_path/your_directory"
        file_utils.read_files(
            dirname=dirname,
        )
        >>> [("filename", "file_content")]
    '''
    filenames = get_filenames(
        dirname=dirname
    )
    resp = []
    for filename in filenames:
        file = read_file(
            filename=f"{dirname}/{filename}"
        )
        resp.append((filename, file))
    return resp
