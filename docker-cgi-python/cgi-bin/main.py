#!/usr/bin/python3

import cgi, cgitb
import os
import subprocess


print("Content-type: text/html")
print("\n")
print("<html>")
print('This cgi script written by python.\n')
print("</html>")

form = cgi.FieldStorage()

if "textcontent" not in form:
    print("Can't find text content")
    f = open("/production/www/cgi-bin/links.txt", "w+")
    f.write("EMPTY")
    f.close()

else:
    print("<p>link:", form["textcontent"].value)
    f = open("/production/www/cgi-bin/links.txt", "w+")
    f.write(form["textcontent"].value)
    f.close()

    print("Running sub process")
    # os.system("python3 tidaldl.py")
    subprocess.call("python3 tidaldl.py", shell=True)
