import argparse, json, os, socket, urllib2
from subprocess import Popen,PIPE,STDOUT

parser = argparse.ArgumentParser(description='Shindenshin: A simple python script to send notifications to your mobile device from *nix shell')
parser.add_argument('-c', '--command', help='command that needs to be run', required=True)
parser.add_argument('-o', '--output', help='send the commands output as part of notification', action='store_true')
args = parser.parse_args()

"""
sends notification to Microsoft Flow Http endpoints
"""
def send_notification(json_input):
    try:
        with open(os.path.expanduser("~/.flow_urls"), 'r') as flow_urls:
            for flow_url in flow_urls:
                req = urllib2.Request(flow_url)
                req.add_header('Content-Type', 'application/json')
                response = urllib2.urlopen(req, json.dumps(json_input))
                print response.read()
                response.close()
    except IOError:
        print "unable to read the .flow_urls file in home directory" 

"""
Executes the user shell command and returns the stdout/stderr and return code
"""
def execute_command(cmd, output=False):
    newProc = Popen([cmd], stderr=PIPE, stdout=PIPE, shell=True)
    if output:
        newProcStdOut, newProcStdErr = newProc.communicate()
    else:
        newProcStdOut, newProcStdErr = '', ''
    if newProc.returncode == 0:
        return [newProcStdOut, newProc.returncode]
    else:
        return [newProcStdErr, newProc.returncode]

"""
Builds the json object from stdout and return code
"""
def generate_json(procCommand, procOutput, procReturncode):
    data = {}
    data['command'] = procCommand
    data['output'] = procOutput
    data['exit_code'] = procReturncode
    data['hostname'] = socket.gethostname()
    return data

send_notification(
        generate_json(
            args.command, 
            *execute_command(args.command, args.output)))
