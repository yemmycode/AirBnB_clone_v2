#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive
from the contents of the web_static folder of
AirBnB Clone repo, using the function do_pack
"""
from fabric.api import local
from time import strftime


def do_pack():
    """Generate a .tgz archive"""
    timestamp = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        archive_name = "versions/web_static_{}.tgz".format(timestamp)
        local("tar -cvzf {} web_static/".format(archive_name))
        return archive_name
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
