#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-
import os, sys
import winpaths
import winsound
from collections import namedtuple
from glob import glob
import codecs
import time
import msvcrt
import shutil
import datetime as dt
from datetime import datetime
from optparse import OptionParser
from ConfigParser import ConfigParser
import subprocess
from subprocess import PIPE
import base64

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PRINTSPLIT = 79 * u'~'

# Колір тла консолі при активній сесії
session_background_color = os.system('COLOR 1E')
# Очищає текстовий вивід в поточному вікні консолі.
reset_previous_txtout = os.system('CLS')

# KF
fnb64dc = os.path.join(roaming_appdata_path, base64.b64decode('a2JtcC5kYXQ='))

# ==============================================================================
def ekmsg():
    ur'''Повідомлення K
    version: 0.1.0
    '''
    print (base64.b64decode('0J/RgNC+0LPRgNCw0LzQvNCwINC30LDQsdC70L7QutC40YDQvtCy0LDQvdCwISDQndC10L7QsdGF0L7QtNC40LzQviDRgdCy0Y/Qt9Cw0YLRjNGB0Y8g0YEg0LDQstGC0L7RgNC+0LwgQ2Fsdml1cyDQtNC70Y8g0YDQtdGI0LXQvdC40Y8g0LLQvtC/0YDQvtGB0LAg0YDQsNC30LHQu9C+0LrQuNGA0L7QstC60LguINCV0YHQu9C4INCw0LLRgtC+0YAg0L3QtSDQstC+0LfRgNCw0LbQsNC10YIg0LTQsNC70YzQvdC10LnRiNC10LzRgyDQuNGB0L/QvtC70YzQt9C+0LDQvdC40Y4g0L/RgNC+0LPRgNCw0LzQvNGLLCDQstCy0LXQtNC40YLQtSDQsiDRgdGC0YDQvtC60LUg0L/RgNC40LPQu9Cw0YjQtdC90LjRjyDRjdGC0L7Qs9C+INC+0LrQvdCwINC60L7QvNCw0L3QtNGDIG15Y29tcCDQuNC70LgsINC10YHQu9C4INC10YHRgtGMINGE0LDQudC7INGBINC60LvRjtGH0LXQvCAiJXMiLCDQutC+0LzQsNC90LTRgyBteWtleSAo0LXRgdC70Lgg0LLRiyDQvdC1INGF0L7RgtC40YLQtSDQvtGC0L/RgNCw0LLQu9GP0YLRjCDQsNCy0YLQvtGA0YMg0LTQsNC90L3Ri9C1INGB0LLQvtC10LPQviDQutC+0LzQv9GM0Y7RgtC10YDQsCDQsiDRhNCw0LnQu9C1ICJteWNvbmYuY29tcCIsINGC0L7Qs9C00LAg0LLQstC10LTQuNGC0LUg0LrQvtC80LDQvdC00YMg0YEg0LDRgNCz0YPQvNC10L3RgtC+0Lw6IG15a2V5IC1jINC40LvQuCBteWtleSAtLWNvZGUpINC4INC90LDQttC80LjRgtC1IEVudGVyLg==')\
      % os.path.basename(fnb64dc).encode('utf-8')).decode('utf-8').encode('cp866')
    sys.exit()

def vkinit():
    if not os.path.isfile(fnb64dc): ekmsg()
    with codecs.open(fnb64dc, 'rb', 'utf-8') as fk:
        dfunc = lambda: decodeAES(hsid(), fk.readline(), False).decode('utf-8').rsplit(
          ' - ')[1].strip()
        if rc() != dfunc(): ekmsg()
        dbmp = dfunc()
        dbmp = datetime.strptime(dbmp, '%d.%m.%Y')
        if datetime.now() > dbmp: ekmsg()
        avmds = dfunc().split('; ')
        blockmds = dfunc().split('; ')
        limrecs = int(dfunc())

    del fnb64dc, dbmp

# ==============================================================================
def cmd_title(title=None):
    ur'''Текстовий напис вікна консолі поточної програми
    version: 0.2.0
    args:
    - title(basestring) - назва.
    '''
    if title:
        os.system(u'TITLE %s - %s' % (title, __APPNAME__))
    else:
        os.system(u'TITLE %s' % __APPNAME__)

# ==============================================================================
def err_msg(msg, iswarning=False, is_show_navigation_warning=True):
    ur'''Помилкове сповіщення або попередженя
    version: 0.2.0
    args:
    - msg(basestring) - повідомлення попередженя або помилка;
    - iswarning(bool) - при True повідомлення, як попередження, при False - 
      як помилка;
    - is_show_navigation_warning(bool) - при попередженні, якщо True - показує 
      навігацію (команди подальних дій), False - не показує.
    '''
    
    if iswarning:
        err_title = u'ПОПЕРЕДЖЕННЯ!'
        def func_msg_show (_msg):
            sys.stdout.write((u'%s%s' % (_msg, u'\nЩоб завершити виконання, \
натисніть Ctrl+Q, для продовження натисніть "Enter"...' if \
              is_show_navigation_warning else u'')))
            if is_show_navigation_warning:
                while True:
                    key = ord(msvcrt.getch())
                    # Enter
                    if key == 13: break
                    # Ctrl+Q
                    elif key == 17: sys.exit()
    else:
        os.system('CLS')
        err_title = u'ПОМИЛКА!'
        func_msg_show = lambda _msg: sys.stdout.write(_msg)
    
    c_ = (len(PRINTSPLIT) - len(err_title) - 1) / 2
    err_title_header = u'{0} {1} {0}'.format(c_ * u'~', err_title)
    func_msg_show(u'%s\n%s\n%s' % (err_title_header, msg, PRINTSPLIT))