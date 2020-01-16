# coding: utf-8
#
# Reference
# https://pypi.org/project/pdfkit/

import datetime as dt
import pdfkit as pk
import os


DELAY_PAGE_COMMON = 'https://www.tokyometro.jp/delay/detail/'
CHIYODA_89 = '/chiyoda_6.shtml'
date = dt.date.today().strftime('%Y%m%d')
source_url = DELAY_PAGE_COMMON + date + CHIYODA_89
OUTPUT_NAME = '遅延証明書 _ 千代田線：遅延証明書 _ 東京メトロ.pdf'
options = {
    'page-size': 'A4',
    'margin-top': '0.1in',
    'margin-right': '0.1in',
    'margin-bottom': '0.1in',
    'margin-left': '0.1in',
    'encoding': "UTF-8",
    'no-outline': None,
    'disable-smart-shrinking': '',
}
# WebページをPDF出力
pk.from_url(source_url, OUTPUT_NAME, options=options)