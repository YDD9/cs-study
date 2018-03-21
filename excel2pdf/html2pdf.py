# for PYTHON3 ONLY

from weasyprint import HTML
HTML('./test_files/sheet001.html').write_pdf('/tmp/test.pdf')


# for PYTHON2 use html2pdf command line....