#!/usr/bin/python3
"""
Fabric script with methods for:
do_pack: creating a .tgz archive from web_static/ files
do_deploy: deploying the archive to web servers
deploy: executing do_pack followed by do_deploy
"""
from fabric.api import local, env, put, run
from time import strftime
import os

env.hosts = ['35.237.202.79', '34.204.185.51']

def do_pack():
    """Generate a .tgz archive of the web_static/ folder"""
    current_time = strftime("%Y%M%d%H%M%S")
    try:
        local("mkdir -p versions")
        archive_name = "versions/web_static_{}.tgz".format(current_time)
        local("tar -cvzf {} web_static/".format(archive_name))
        return archive_name
    except Exception:
        return None

def do_deploy(archive_path):
    """
    Deploy the archive to web servers
    """
    if not os.path.isfile(archive_path):
        return False
    try:
        archive_name = archive_path.split("/")[-1]
        archive_no_ext = archive_name.split(".")[0]
        release_path = "/data/web_static/releases/{}/".format(archive_no_ext)
        symlink_path = "/data/web_static/current"
        
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(release_path))
        run("tar -xzf /tmp/{} -C {}".format(archive_name, release_path))
        run("rm /tmp/{}".format(archive_name))
        run("mv {}web_static/* {}".format(release_path, release_path))
        run("rm -rf {}web_static".format(release_path))
        run("rm -rf {}".format(symlink_path))
        run("ln -s {} {}".format(release_path, symlink_path))
        return True
    except Exception:
        return False

def deploy():
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
