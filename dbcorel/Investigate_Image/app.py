import os

from uuid import uuid4

from flask import Flask, request, render_template, send_from_directory

from readXML import readXML

from student import SinhVien

from get_face_top_100 import findTop100, findImageInTree, findImageInTree_DBCOREL

import time

sinhviens = []

sinhviens = readXML()

app = Flask(__name__)
# app = Flask(__name__, static_folder="images")

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    # target = os.path.join(APP_ROOT, 'static/')
    print(target)
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        destination = "/".join([target, filename])
        print ("Accept incoming file:", filename)
        print ("Save it to:", destination)
        upload.save(destination)

        # start = time.time()
        # lstImg = findTop100(destination)
        # end = time.time()
        # timeLinearSearch = end - start

        # start = time.time()
        # lstImg = findImageInTree(destination)
        # end = time.time()
        # timeTreeSearch = end - start

        start = time.time()
        lstImg = findImageInTree_DBCOREL(destination)
        end = time.time()
        timeLinearSearch = end - start

        start = time.time()
        lstImg = findImageInTree_DBCOREL(destination)
        end = time.time()
        timeTreeSearch = end - start

        image_names = []
        lstMSSV = []
        # for i in range(0, len(lstImg)):
        #     lstMSSV.append(sinhviens[int(lstImg[i])].getMaHSSV())
        # print lstMSSV
        for image in lstImg:
            image_names.append(str(image) + ".jpg")
        
        amount = len(lstImg)

    # return send_from_directory("images", filename, as_attachment=True)
    #return render_template("complete.html", image_name=filename)
    # image_names = os.listdir('./images')
    return render_template("gallery.html", image_names=image_names, amount=amount, lstMSSV=lstMSSV, timeTreeSearch=timeTreeSearch, timeLinearSearch=timeLinearSearch)

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("data", filename)

@app.route('/infostudent/<index>', methods=['GET','POST'])
def result(index):
    index = index.split('.')[0]
    sv = sinhviens[int(index)]
    return render_template("info.html", sv=sv)



if __name__ == "__main__":
    app.run(debug=True)
