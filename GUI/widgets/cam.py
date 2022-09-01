import cv2 as cv


class Camera:
    def __init__(self, *args, **kwargs):
        try:
            if not 'cam_source' in kwargs:
                self.camera = cv.VideoCapture(0, cv.CAP_V4L)
            else:
                cam_source = kwargs['cam_source']
                self.camera = cv.VideoCapture(cam_source, cv.CAP_V4L)
                if not self.camera.isOpened():
                    raise ValueError("Unable to open video source", cam_source)
        except Exception as exc:
            raise exc

    def __del__(self):
        if self.camera.isOpened():
            self.camera.release()

    def get_origin_frames(self):
        if self.camera.isOpened():
            ret, frame = self.camera.read()
            if ret:
                return frame

