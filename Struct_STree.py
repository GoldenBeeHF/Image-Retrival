# This Python file uses the following encoding: utf-8
# Task tạo cây STree cải thiện tốc độ tìm kiếm hình ảnh của khóa luận
# Người thực hiện: Trần Lê Văn Đức
# Thời gian thực hiện: đến hết thứ 4, ngày 13 tháng 3 năm 2019
# Yêu cầu làm việc nghiêm túc !!!

# Các bước tạo cây:
# B1: Tạo nút root của cây. Thêm hình (HOG) đầu tiên vào. Cho sức chứa là 20 (quá 20 sẽ tách nút).
# B2: Thêm lần lượt các hình tiếp theo vào. Khi vượt quá 20 sẽ tách nút.
# Cách tách: chọn 2 vector xa nhau nhất tạo thành 2 nút. Đưa các vector còn lại vào 2 nút vừa tạo
# Quy tắc: gần nút nào sẽ gom vào nút đó.
# B3: Sau đó tính vector trung bình của mỗi nút.
# Cách tính: cộng tuyến tính các thành phần của vector sau đó chia trung bình
# Vd: v1 = (x1, x2, ..., xN), v2 = (y1, y2, ..., yN)
# vTB = ((x1 + y1) / 2, (x2 + y2) / 2, ..., (xN + yN) / 2)
# B4: Tạo nút mới với các phần tử là 2 vector trung bình vừa tính. Link 2 vector trung bình với nút con.
# B5: Tiếp tục thêm hình vào cây.
# Cách thêm: mỗi hình đưa vào sẽ so sánh với 2 vector trung bình vừa tạo xem gần vector nào hơn.
# Sau đó sẽ theo đường link và thêm xuống nút lá.
# Khi thêm xuống nút lá phải tiến hành tính lại vector trung bình.
# Cứ tiếp tục thêm đến khi tràn nút lá thì lại tiếp tục tách nút.
# 2 vector trung bình lấy được sẽ được thêm vào root.
# Khi nút root tràn sẽ tách nút root. Tương tự làm tiếp tục.

import struct
import random
import function
lst = []
for i in range(0, 60):
    vector = [
        random.randint(1, 10), 
        random.randint(1, 10), 
        random.randint(1, 10), 
        random.randint(1, 10), 
        random.randint(1, 10)
    ]
    
    a = struct.HOG(vector, i)
    lst.append(a)

tree = struct.STree()
tree.root = struct.Leaf(tree.countId)
tree.countId = tree.countId + 1

for image in lst:
    tree.addImage(image)
print "Root"
for v in tree.root.lstVector:
    print v.getLink(), v.getVector()

for leaf in tree.lstLeaf:
    print "Cluster", leaf.id
    for image in leaf.lstImage:
        print image.getId(), image.getVector()
    print function.computeAvgVector(leaf.lstImage)
