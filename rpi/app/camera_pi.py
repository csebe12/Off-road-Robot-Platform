import io
import time
import picamera
from base_camera import BaseCamera


class Camera(BaseCamera):
    @staticmethod
    def frames():
        with picamera.PiCamera() as camera:
            camera.resolution = (1280, 720)
            camera.framerate = 30
            camera.rotation = 180
            camera.led = False
            # let camera warm up
            time.sleep(2)
            print('\033[91m' + "Resolution ", str(camera.resolution) + '\033[0m')
            print('\033[91m' + "Framerate ", str(camera.framerate) + '\033[0m')

            stream = io.BytesIO()
            for _ in camera.capture_continuous(stream, 'jpeg',
                                                 use_video_port=True):
                # return current frame
                stream.seek(0)
                yield stream.read()

                # reset stream for next frame
                stream.seek(0)
                stream.truncate()
