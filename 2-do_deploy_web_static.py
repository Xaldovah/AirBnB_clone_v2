#!/usr/bin/python3
"""
Fabric script for deploying a web_static archive to web servers.
"""

from fabric.api import env, put, run, local
from os.path import exists, isfile, splitext, basename
from datetime import datetime

# Define the hosts (your web servers)
env.hosts = ['52.3.254.195', '54.197.42.179']


def do_deploy(archive_path):
    """Deploy a web_static archive to the web server(s)."""
    if not exists(archive_path) or not isfile(archive_path):
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
