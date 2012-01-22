import subprocess

print 'subprocess demo: reading output of child process'
proc = subprocess.Popen('echo "Hello,World"',shell=True, stdout=subprocess.PIPE)
cout = proc.communicate()[0]
print cout


print 'subprocess demo: writing to the input of a pipe'
proc = subprocess.Popen('cat -', shell=True, stdin=subprocess.PIPE)
proc.communicate('Hello, World')

print

print 'subprocess replacement of popen2, reading and writing through pipes'
proc = subprocess.Popen('cat -', shell=True, stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE)

cout = proc.communicate("""
We were so poor we couldn't afford a watchdog.  If we heard a noise at night,
we'd bark ourselves.
		-- Crazy Jimmy
""")[0]

print cout

print 'subprocess replacement of popen3, handling stdin, stdout and stderr'
proc = subprocess.Popen('cat -;echo "This will be an Error Message" 1>&2',
                        shell=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE
                       )
cout, cerr = proc.communicate('This is the Input Message')

print cout
print cerr
