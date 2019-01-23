import io
import picamera
import codecs
import logging
import socketserver
from threading import Condition
from http import server


class StreamingOutput(object):
    def __init__(self):
        self.frame = None
        # BytesIO is a simple stream of in-memory bytes
        self.buffer = io.BytesIO()
        self.condition = Condition()

    def write(self, buf):
        # b'' - binary mode####
        if buf.startswith(b'\xff\xd8'):
            # New frame, copy the existing buffer's content and notify all
            # clients it's available
            # resize stream to bytes
            self.buffer.truncate()
            with self.condition:
                # .getvalue() - return contents of the buffer
                self.frame = self.buffer.getvalue()
                self.condition.notify_all()
            # hide stream content from page
            self.buffer.seek(0)
        # writes unicode string to the stream and return the the number of characters written
        return self.buffer.write(buf)


class StreamingHandler(server.BaseHTTPRequestHandler):
    def get_page_text_from_file(self):
        f = codecs.open('page.html', "r")
        return f.read()

    def do_GET(self):
        if self.path == '/':
            self.send_response(301)
            self.send_header('Location', '/index.html')
            self.end_headers()
        elif self.path == '/index.html':
            content = self.get_page_text_from_file()
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(content))
            self.end_headers()
            self.wfile.write(content)
        elif self.path == '/stream.mjpg':
            self.send_response(200)
            self.send_header('Age', 0)
            self.send_header('Cache-Control', 'no-cache, private')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')
            self.end_headers()
            try:
                while True:
                    with output.condition:
                        output.condition.wait()
                        frame = output.frame
                    self.wfile.write(b'--FRAME\r\n')
                    self.send_header('Content-Type', 'image/jpeg')
                    self.send_header('Content-Length', len(frame))
                    self.end_headers()
                    self.wfile.write(frame)
                    self.wfile.write(b'\r\n')
            except Exception as e:
                logging.warning(
                    'Removed streaming client %s: %s',
                    self.client_address, str(e))
        else:
            self.send_error(404)
            self.end_headers()


class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):
    allow_reuse_address = True
    daemon_threads = True


with picamera.PiCamera(resolution='640x480', framerate=24) as camera:
    output = StreamingOutput()
    camera.start_recording(output, format='mjpeg')
    try:
        address = ('', 8080)
        server = StreamingServer(address, StreamingHandler)
        server.serve_forever()
    finally:
        camera.stop_recording()
