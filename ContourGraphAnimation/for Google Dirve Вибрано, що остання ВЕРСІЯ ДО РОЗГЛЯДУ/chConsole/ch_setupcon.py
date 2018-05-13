# -*- coding: utf-8 -*-
'''
Created on 27.10.2011

@author: iCheterX
'''

import sys
import locale
import codecs

def current_encode_console(printable=False):
    ur'''usage: Повертає або виводить кодування середовища, локалі та \
стандартного потоку виводу.
  args:
  printable - задає роботу методу. False - повертає tuple кодувань у вигляді \
(sys_enc, locale_enc, stdout_enc), True - друкує той самий tuple.
--------------------------------------------------------------------------
Author: Anton Cheterbok
Version: 0.1.0
Date: 2011-10-27
'''      
    sys_enc = sys.getdefaultencoding()
    locale_enc = locale.getpreferredencoding()
    stdout_enc = sys.stdout.encoding
    
    if printable:
        print('sys_encoding: {0}\nlocale_encoding: {1}\nstdout_encoding: {2}' \
              .format(sys_enc, locale_enc, stdout_enc))
    else:
        return (sys_enc, locale_enc, stdout_enc)
    

def setup_console(sys_enc='utf-8'):
    ur'''usage: Встановлює кодування виводу.
  args:
  sys_enc - кодування за промовчанням, яке приймається у випадку, якщо 
кодування локальних налаштувань операційної системи не було отримано.
--------------------------------------------------------------------------
  Author: Anton Cheterbok
  Version: 0.1.0
  Date: 2011-10-27
'''
    # Встановлення за промовчанням локалі згідно змінної середовища
    # LC_ALL.
    locale.setlocale(locale.LC_ALL, '')
    # Закладається поточне кодування локалі.
    encoding = locale.getlocale()[1]
    # Якщо кодування не було визначено, то приймається значення sys_enc.
    if not encoding: encoding = sys_enc
    # Перезавантажується середовище із новими налаштуваннями.
    reload(sys)
    # Кодування для середовища.
    sys.setdefaultencoding(encoding)

    # Перевизначаються стандартні потоки виводу, якщо вони не
    # перенаправлені.
    if sys.stdout.isatty() and sys.stdout.encoding != encoding:
        sys.stdout = codecs.getwriter(encoding)(sys.stdout, errors='replace')
    
    if sys.stderr.isatty() and sys.stderr.encoding != encoding:
        sys.stderr = codecs.getwriter(encoding)(sys.stderr, errors='replace')

def er_input(text):
    ur'''usage: Дозволяє вводити raw-текст у кодуванні, в якому перебуває \
потік виводу.
--------------------------------------------------------------------------
  Author: Anton Cheterbok
  Version: 0.1.0
  Date: 2011-10-27
'''
    return raw_input(text).decode(sys.stdout.encoding)

if __name__ == '__main__':
    current_encode_console(True)
    setup_console()
    current_encode_console(True)
    print(er_input(u'Чумацький шлях - одна із Галактик Всесвіту.'))