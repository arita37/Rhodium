# Copyright 2015-2016 David Hadka
#
# This file is part of Rhodium, a Python module for robust decision making and
# exploratory modeling.
#
# Rhodium is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Rhodium is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Rhodium.  If not, see <http://www.gnu.org/licenses/>.
from __future__ import absolute_import, division, print_function

import matplotlib.pyplot as plt
from platypus.config import PlatypusConfig

class _RhodiumConfig(object):
    
    def __init__(self):
        super(_RhodiumConfig, self).__init__()
        self.default_cmap = plt.get_cmap("rainbow")
     
    @property
    def default_evaluator(self):
        return PlatypusConfig.default_evaluator
     
    @default_evaluator.setter
    def default_evaluator(self, value):
        PlatypusConfig.default_evaluator = value
        
RhodiumConfig = _RhodiumConfig()
