# This file is part of the Frescobaldi project, http://www.frescobaldi.org/
#
# Copyright (c) 2008, 2009, 2010 by Wilbert Berendsen
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
# See http://www.gnu.org/licenses/ for more information.

from __future__ import unicode_literals

""" Routines dealing with LilyPond fonts """

import os, ly, xml.dom.minidom

class SvgFontInfo(object):
    """
    Can load a SVG font and provide information about the glyphs and
    their unicode values.
    """
    def __init__(self, filename):
        self.name2unicode = {}
        doc = xml.dom.minidom.parse(filename)
        glyphs = doc.getElementsByTagName('glyph')
        for g in glyphs:
            name = g.attributes["glyph-name"].value
            code = g.attributes["unicode"].value
            self.name2unicode[name] = code
        doc.unlink()
        
    def glyph(self, glyphName):
        return self.name2unicode.get(glyphName, '')
        
    def glyphs(self):
        return self.name2unicode.keys()

