#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo.
"""

from fabric.api import local, env
from datetime import datetime
import os

env.hosts = ['localhost']


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
