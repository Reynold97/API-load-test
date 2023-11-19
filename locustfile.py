from locust import HttpUser, task, between
import os

class MyUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def swapp_face(self):
        model_file_path = os.path.join(os.getcwd(), "samurai.png")
        face_file_path = os.path.join(os.getcwd(), "Reynold_Oramas.jpg")

        with open(model_file_path, 'rb') as model, open(face_file_path, 'rb') as face:
            files = {
                'model': ('samurai.png', model, 'image/png'),
                'face': ('Reynold_Oramas.jpg', face, 'image/jpeg'),
            }
            data = {
                'watermark': (None, 'false'),
                'vignette': (None, 'false')
            }

            self.client.post("swap_face", files=files, data = data)
