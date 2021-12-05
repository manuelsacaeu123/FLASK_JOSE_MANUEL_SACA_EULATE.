from flask import request, jsonfy,send_file
import server
from  controller import car_controller
import os

@server.app.route('/download/<filename>')
def download_file(filename):
     file_path = server.app.config['UPLOAD_FOLDER']+filename
     return send_file(file_path, as_attachment=True)
