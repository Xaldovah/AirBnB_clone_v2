#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to web servers.
"""

from fabric.api import env, local, run
from datetime import datetime
from os.path import exists

# Define the hosts (your web servers)
env.hosts = ['<265468-web-01>', '<265468-web-02>']


def do_pack():
    """Create a compressed .tgz file from web_static folder."""
    try:
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(current_time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(archive_path))
        return archive_path
    except Exception:
        return None


def do_deploy(archive_path):
    """Deploy a web_static archive to the web server(s)."""
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory on the web server(s)
        put(archive_path, '/tmp/')

        # Create directory structure
        archive_filename = basename(archive_path)
        archive_no_ext = splitext(archive_filename)[0]
        release_folder = '/data/web_static/releases/' + archive_no_ext + '/'

        run('mkdir -p {}'.format(release_folder))

        # Uncompress the archive to the release folder
        run('tar -xzf /tmp/{} -C {}'.format(archive_filename, release_folder))

        # Delete the uploaded archive
        run('rm /tmp/{}'.format(archive_filename))

        # Remove the old symbolic link
        current_link = '/data/web_static/current'
        if exists(current_link):
            run('rm -f {}'.format(current_link))

        # Create a new symbolic link
        run('ln -s {} {}'.format(release_folder, current_link))

        return True

    except Exception:
        return False


def deploy():
    """Create and distribute an archive to web servers."""
    archive_path = do_pack()
    if not archive_path:
        return False

    return do_deploy(archive_path)
