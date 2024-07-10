#!/usr/bin/python3
"""Fabric script that generates a .tgz archive
from the contents of the web_static folder"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""

    # Create the versions folder if it doesn't exist
    if not os.path.exists("versions"):
        local("mkdir -p versions")

    # Generate the name of the archive
    time_format = "%Y%m%d%H%M%S"
    archive_name = f"web_static_{datetime.utcnow().strftime(time_format)}.tgz"

    # Compress the contents of the web_static folder
    command = "tar -cvzf versions/{} web_static".format(archive_name)
    result = local(command)

    # Check if the archive was created successfully
    if result.failed:
        return None
    else:
        return "versions/{}".format(archive_name)


if __name__ == "__main__":
    result = do_pack()
    if result:
        print(f"web_static packed: {result} -> {os.path.getsize(result)}Bytes")
    else:
        print("Packing web_static failed.")
