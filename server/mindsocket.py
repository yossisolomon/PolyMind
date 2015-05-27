import hashlib
from tempfile import mkstemp
import socket
from progressbar import ProgressBar
from threading import Thread
import json
import time


class mindsocket:
    '''demonstration class only
      - coded for clarity, not efficiency
    '''

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

        self.sock_addr = None
        self.is_recording = False


    def connect(self, host, port):
        print 'connecting:'
        # if self.sock_addr == None or self.sock_addr == (host, port):
        #     #
        #     #     self.sock.close()
        #     self.sock.connect((host, port))
        #     self._send('{"format":"Json"}')
        #     self.sock_addr = (host, port)
        # else:
        #     print "retrying connection..."
        #     self.sock.connect((host, port))
        if not self.sock_addr == None:
            self.sock.shutdown(socket.SHUT_RDWR)
            self.sock.close()

        self.sock.connect((host, port))

        progress = ProgressBar()
        for _ in progress(range(10)):
          if sock._is_connected():
              progress.finish()
              print "configuring to JSON output"
              self._send('{"format":"Json"}')
              self.sock_addr = (host, port)
              print("connected!")
              return 0
        print "Couldn't connect!"
        self.sock_addr = None
        return -1



    def _send(self, msg):
        totalsent = 0
        while totalsent < len(msg):
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def _receive(self):
        chunks = []
        bytes_recd = 0
        MSGLEN = 1000 # made up number
        while True:
            chunk = self.sock.recv(min(MSGLEN - bytes_recd, 2048))
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
            #print chunk
            if chunk.endswith('\r'):
                break
            #print chunk

        return ''.join(chunks)

    def _is_connected(self):
        msg = self.recv_msg()
        if "status" in msg:
            return False
        else:
            return True

    def recv_msgs(self,num):
        msgs = []
        for _ in range(num):
            msgs.append(self._receive())
        return msgs

    def recv_msg(self):
        return self.recv_msgs(1)[0]


    def _record(self):
        self.is_recording = True
        self.recording = []
        while self.is_recording:
            self.recording.append(json.loads(self._receive()))

    def start_recording(self):
        self._recording_thread = Thread(target = self._record)
        self._recording_thread.start()

    def stop_recording(self):
        self.is_recording = False
        self._recording_thread.join()
        _, temp_path = mkstemp()
        with open(temp_path, 'w') as outfile:
            json.dump(self.recording, outfile)
        print temp_path


sock = mindsocket()
while sock.connect(host='127.0.0.1', port=13854) == -1:
    pass

#  while True:
#     print sock.recv_msg()
print "recording!"
sock.start_recording()
time.sleep(10)
print "stopping recording!"
print sock.stop_recording()
