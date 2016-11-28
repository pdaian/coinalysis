import subprocess, threading

class Command(object):
    # http://stackoverflow.com/questions/1191374/using-module-subprocess-with-timeout
    def __init__(self, cmd):
        self.cmd = cmd
        self.process = None
        self.stdout = ""

    def run(self, timeout):
        def target():
            print 'Thread started'
            self.process = subprocess.Popen(self.cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            stdout = []
            while True:
                line = self.process.stdout.readline()
                stdout.append(line)
                print line,
                if line == '' and self.process.poll() != None:
                    break
            self.stdout = ''.join(stdout)

        thread = threading.Thread(target=target)
        thread.start()

        thread.join(timeout)
        if thread.is_alive():
            print 'Terminating process'
            self.process.terminate()
            thread.join()
        print self.process.returncode


