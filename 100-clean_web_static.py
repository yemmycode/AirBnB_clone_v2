#!/usr/bin/python3
"""
Fabric script methods:
do_pack: creates an archive from web_static/ files
do_deploy: deploys the archive to web servers
deploy: runs do_pack and do_deploy
do_clean: removes outdated archives
"""
from fabric.api import local, env, put, run, cd
from time import strftime
import os

env.hosts = ['35.237.202.79', '34.204.185.51']

def do_pack():
    """Generate a .tgz archive of the web_static/ folder"""
    timenow = strftime("%Y%M%d%H%M%S")
    try:
        local("mkdir -p versions")
        archive_name = "versions/web_static_{}.tgz".format(timenow)
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
        archive_name = os.path.basename(archive_path)
        archive_no_ext = os.path.splitext(archive_name)[0]
        release_dir = "/data/web_static/releases/{}/".format(archive_no_ext)
        current_symlink = "/data/web_static/current"
        
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(release_dir))
        run("tar -xzf /tmp/{} -C {}".format(archive_name, release_dir))
        run("rm /tmp/{}".format(archive_name))
        run("mv {}web_static/* {}".format(release_dir, release_dir))
        run("rm -rf {}web_static".format(release_dir))
        run("rm -rf {}".format(current_symlink))
        run("ln -s {} {}".format(release_dir, current_symlink))
        return True
    except Exception:
        return False

def deploy():
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

def do_clean(number=0):
    """
    Delete out-of-date archives
    """
    number = max(int(number), 1)
    
    local("cd versions && ls -t | tail -n +{} | xargs rm -f".format(number + 1))
    run("cd /data/web_static/releases && ls -t | tail -n +{} | xargs rm -rf".format(number + 1))

