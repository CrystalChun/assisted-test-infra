#!/usr/bin/python3

import argparse
import logging
import os
from http.server import HTTPServer, CGIHTTPRequestHandler

parser = argparse.ArgumentParser()
parser.add_argument('--dir', type=str, help='Directory location of script relative to assisted-test-infra base directory', required=False, default="build/ipxe_server")
parser.add_argument('--ip', type=str, help='Server IP', required=False, default="192.168.122.1")
parser.add_argument('--ipxe-file-name', type=str, help='Name of the ipxe file', required=False, default="pxe")
parser.add_argument('--port', type=int, help='Port to host this server with', required=False, default=8500)
args = parser.parse_args()
# Make sure the server is created at current directory
dirpath=f"{os.getcwd()}/{args.dir}"
logging.info("path %s", dirpath)
os.chdir(dirpath)

# Create server object listening the port 80
server_object = HTTPServer(server_address=(args.ip, args.port), RequestHandlerClass=CGIHTTPRequestHandler)
# Start the web server
server_object.serve_forever()
#server_object.handle_one_request()