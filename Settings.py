#
# Settings.py -- Simple class to manage stateful user preferences.
#
#[ Eric Jeschke (eric@naoj.org) --
#  Last edit: Wed Jan 16 13:55:13 HST 2013
#]
#
# Copyright (c) 2011-2012, Eric R. Jeschke.  All rights reserved.
# This is open-source software licensed under a BSD license.
# Please see the file LICENSE.txt for details.
#
import os
import pickle
   
import Bunch

class Settings(object):
    def __init__(self, basefolder="/tmp", create_folders=True):
        self.folder = basefolder
        self.create = create_folders
        self.settings = Bunch.Bunch(caseless=True)

    def setDefaults(self, category, **kwdargs):
        for key, val in kwdargs.items():
            self.settings[category].setdefault(key, val)

    def getSettings(self, category):
        return self.settings[category]
    
    def createCategory(self, category):
        if not self.settings.has_key(category):
            self.settings[category] = Bunch.Bunch(caseless=True)
        return self.settings[category]

    def load(self, category, filename):
        category = category.lower()
        path = os.path.join(self.folder, category, filename)
        buf = None
        with open(path, 'r') as in_f:
            d = pickle.load(in_f)
        self.settings[category] = Bunch.Bunch(caseless=True)
        self.settings[category].update(d)
        #print "%s settings are: %s" % (category, str(self.settings[category]))
        return self.settings[category]
        
    def save(self, category, filename):
        category = category.lower()
        folder = os.path.join(self.folder, category)
        if (not os.path.exists(folder)) and self.create:
            os.mkdir(folder)
        path = os.path.join(folder, filename)
        d = {}
        d.update(self.settings[category])
        with open(path, 'w') as out_f:
            pickle.dump(d, out_f)

    def get_baseFolder(self):
        return self.folder
    
#END
