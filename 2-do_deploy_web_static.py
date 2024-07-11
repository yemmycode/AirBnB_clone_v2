#!/usr/bin/python3
"""
Fabric script method do_deploy
deploys an archive to web servers
"""
from fabric.api import env, put, run
import os

env.hosts = ['35.237.202.79', '34.204.185.51']

def do_deploy(archive_path):
    """
    Deploys the archive to the web server
    """
    if not os.path.isfile(archive_path):
        return False
    try:
        filename = os.path.basename(archive_path)
        no_ext = os.path.splitext(filename)[0]
        release_path = f"/data/web_static/releases/{no_ext}/"
        symlink = "/data/web_static/current"
        
        put(archive_path, "/tmp/")
        run(f"mkdir -p {release_path}")
        run(f"tar -xzf /tmp/{filename} -C {release_path}")
        run(f"rm /tmp/{filename}")
        run(f"mv {release_path}web_static/* {release_path}")
        run(f"rm -rf {release_path}web_static")
        run(f"rm -rf {symlink}")
        run(f"ln -s {release_path} {symlink}")
        
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
