#!C:\Users\KELECHI\PycharmProjects\reservationsystem\transportreserve\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'xhtml2pdf==0.2b1','console_scripts','pisa'
__requires__ = 'xhtml2pdf==0.2b1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('xhtml2pdf==0.2b1', 'console_scripts', 'pisa')()
    )
