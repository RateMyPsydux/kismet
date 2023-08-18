import sys
import time
import KismetCaptureRtl433
import os

def main():
    rtl = KismetCaptureRtl433.KismetRtl433()
    if os.path.exists("/tmp/my_pipe"):
        os.remove("/tmp/my_pipe")
    rtl.run()

