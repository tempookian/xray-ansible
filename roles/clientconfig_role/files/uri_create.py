#!/usr/bin/env python3

import sys
import base64
import pathlib


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        content = f.read()

    content = content.replace("'", '"')
    content = content.replace(', "', ',"')
    content = content.replace(": ", ":")

    uri = f"vmess://{base64.b64encode(content.encode()).decode()}"

    write_path = pathlib.Path("/tmp/") / f"{sys.argv[2]}_client_configs.txt"

    if not write_path.parent.exists():
        raise FileNotFoundError(f"Path {write_path.parent} does not exist")

    with open(write_path, "a") as f:
        f.write(uri + "\n")
