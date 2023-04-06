import io
import sys

class CaptureOutput:
    def __init__(self):
        self.stdout = None
        self.stderr = None

    def __enter__(self):
        self.stdout = io.StringIO()
        self.stderr = io.StringIO()
        sys.stdout = self.stdout
        sys.stderr = self.stderr
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

    def get_stdout(self):
        return self.stdout.getvalue()

    def get_stderr(self):
        return self.stderr.getvalue()
