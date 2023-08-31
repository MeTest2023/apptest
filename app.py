from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

cameras = [
 "https://storage.googleapis.com/gtv-videos-bucket/sample/TearsOfSteel.mp4",
 "https://storage.googleapis.com/gtv-videos-bucket/sample/ForBiggerMeltdowns.mp4", 
...
  ]


def find_camera(list_id):
    return cameras[int(list_id)]


def gen_frames(camera_id):
    cam = find_camera(camera_id)
    cap = cv2.VideoCapture(cam)

    while True:

        
        success, frame = cap.read() 
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed/<string:list_id>/', methods=["GET"])
def video_feed(list_id):
    return Response(gen_frames(list_id),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/', methods=["GET"])
def index():
    return render_template(camera_list=len(cameras), camera=cameras)


if __name__ == '__main__':
    app.run()


# from flask import Flask, render_template, Response
# import cv2
# import threading

# app = Flask(__name__)

# class VideoStream:
#     def __init__(self, video_url):
#         self.video_url = video_url
#         self.cap = cv2.VideoCapture(self.video_url)
#         self.frame = None
#         self.running = True
#         self.thread = threading.Thread(target=self.update_frame)
#         self.thread.daemon = True
#         self.thread.start()

#     def update_frame(self):
#         while self.running:
#             ret, self.frame = self.cap.read()

#     def get_frame(self):
#         ret, buffer = cv2.imencode('.jpg', self.frame)
#         return buffer.tobytes()

# # List of video URLs
# video_urls = [
#     "https://storage.googleapis.com/gtv-videos-bucket/sample/TearsOfSteel.mp4",
#     "https://storage.googleapis.com/gtv-videos-bucket/sample/TearsOfSteel.mp4",
# ]

# video_streams = [VideoStream(url) for url in video_urls]  # Create streams from URLs

# @app.route('/')
# def index():
#     return render_template('index.html', video_urls=video_urls)

# def generate_frames(stream_idx):
#     while video_streams[stream_idx].running:
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + video_streams[stream_idx].get_frame() + b'\r\n')

# @app.route('/video_feed/<int:stream_idx>')
# def video_feed(stream_idx):
#     return Response(generate_frames(stream_idx),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')


# if __name__ == '__main__':
#     app.run()



# from flask import Flask,render_template,Response
# import cv2

# app=Flask(__name__)


# def generate_frames():
#     camera=cv2.VideoCapture(0)
#     while True:
#         success,frame=camera.read()
#         if not success:
#             break
#         else:
#             ret,buffer=cv2.imencode('.jpg',frame)
#             frame=buffer.tobytes()

#         yield(b'--frame\r\n'
#               b'Content-Type: image/jpeg\r\n\r\n'+frame+b'\r\n')


# @app.route('/cam/1')
# def video():
#     return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

# if __name__=="__main__":
#     app.run()







# from flask import Flask, render_template, Response
# import cv2

# app = Flask(__name__)

# def get_camera_list():
#     camera_list = [
#         'https://storage.googleapis.com/gtv-videos-bucket/sample/SubaruOutbackOnStreetAndDirt.mp4',
#         'https://storage.googleapis.com/gtv-videos-bucket/sample/ForBiggerMeltdowns.mp4',
#         'https://storage.googleapis.com/gtv-videos-bucket/sample/ForBiggerMeltdowns.mp4'
#     ]
#     for i in range(10):
#         cap = cv2.VideoCapture(i)
#         if cap.isOpened():
#             camera_list.append(f'Camera {i}')
#             cap.release()
#     return camera_list

# def generate_frames(camera_index):
#     cap = cv2.VideoCapture(camera_index)
#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             break

#         ret, buffer = cv2.imencode('.jpg', frame)
#         frame = buffer.tobytes()

#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

#     cap.release()


# @app.route('/')
# def index():
#     camera_list = get_camera_list()
#     return render_template('index.html', camera_list=camera_list)


# @app.route('/video_feed/<int:camera_index>')
# def video_feed(camera_index):
#     return Response(generate_frames(camera_index),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')


# if __name__ == '__main__':
#     app.run()
