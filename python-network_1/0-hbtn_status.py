"""Python script that fetches https://alu-intranet.hbtn.io/status
"""
import urllib.request
"""This function is used for importing the request fuction from the uniform resource libary
"""

with urllib.request.urlopen('https://alu-intranet.hbtn.io/status') as response:
    html = response.read()
