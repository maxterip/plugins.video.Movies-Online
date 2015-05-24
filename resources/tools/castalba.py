# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Movies-Online Regex de castalba
# Version 0.1 (17.10.2014)
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Gracias a la librería plugintools de Jesús (www.mimediacenter.info)


import os
import sys
import urllib
import urllib2
import re
import shutil
import zipfile
import time

import xbmc
import xbmcgui
import xbmcaddon
import xbmcplugin

import plugintools
import json


home = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.Movies-Online', ''))
tools = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.Movies-Online/resources/tools', ''))
addons = xbmc.translatePath(os.path.join('special://home/addons/', ''))
resources = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.Movies-Online/resources', ''))
art = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.Movies-Online/art', ''))
tmp = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.Movies-Online/tmp', ''))
playlists = xbmc.translatePath(os.path.join('special://home/addons/playlists', ''))

icon = art + 'icon.png'
fanart = 'fanart.jpg'



# En construcción!
def castalba(params):
    plugintools.log("[Movies-Online 0.0.1].castalba "+repr(params))

    url = params.get("url")
    plugintools.play_resolved_url(url)
