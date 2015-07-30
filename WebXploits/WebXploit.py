import os
import sys
import argparse
import requests
"""For appending the directory path"""
abs_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(abs_path+'/')

from rand.random import Random
from cookies.cookies import Cookies
from headers.headers import Headers

__author__ = 'Anirudh Anand <anirudh.anand@owasp.org>'


class WebXploit():
    """ """
    def __init__(self):
        self.cookies = Cookies()
        self.headers = Headers()
        self.random = Random()

    def launch(self):
        os.system("toilet -F metal WebXploit - Recon")

    def get_headers(self, target):
        self.headers.execute_all_func(target)

    def get_cookies(self, target):
        self.cookies.execute_all_func(target)

    def execute_random_vulns(self, target):
        self.random.execute_all_func(target)


def main():
    webxpoit = WebXploit()

    parser = argparse.ArgumentParser(description=
                                     'Do a basic Recon for Web challenges')
    parser.add_argument('-u', '-url', type=str, help='Target URL to Recon')
    parser.add_argument('-o', '-out', type=str, help='Filename to save output')
    args = parser.parse_args()

    webxpoit.launch()
    webxpoit.get_headers(args.u)
    webxpoit.get_cookies(args.u)
    webxpoit.execute_random_vulns(args.u)

if __name__ == '__main__':
    main()