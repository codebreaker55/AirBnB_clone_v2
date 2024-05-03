#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive from the contents,
of the web_static folder of your AirBnB Clone repo, using the function do_pack
"""

from datetime import datetime
from fabric.api import *


def do_pack():
    """
    All files in the folder web_static must be added to the final archive
    All archives must be stored in the folder versions,
    (function should create this folder if it doesn’t exist).
    The name of the archive created must be,
    web_static_<year><month><day><hour><minute><second>.tgz
    The function do_pack must return the archive path if the archive,
    has been correctly generated. Otherwise, it should return None
    """
    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(archive))
    if create is not None:
        return archive
    else:
        return None
