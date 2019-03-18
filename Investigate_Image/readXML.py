from xml.dom import minidom
from student import SinhVien
#parse an xml file by name
def readXML():
    sinhviens = []

    mydoc = minidom.parse('dataSV.xml')

    dataSV = mydoc.getElementsByTagName('Data')
    # all item attributes

    svs = mydoc.getElementsByTagName("sinhvien")

    
    for i in range(len(svs) - 1):
        sinhvien = SinhVien()
        sinhvien.setMaHSSV(svs[i].getElementsByTagName("MaHSSV")[0].firstChild.data)
        sinhvien.setHoDem(svs[i].getElementsByTagName("HoDem")[0].firstChild.data )
        sinhvien.setTen(svs[i].getElementsByTagName("Ten")[0].firstChild.data)
        sinhvien.setGioiTinh(svs[i].getElementsByTagName("GioiTinh")[0].firstChild.data)
        sinhvien.setNgaySinh(svs[i].getElementsByTagName("NgaySinh")[0].firstChild.data)
        sinhvien.setKhoaHoc(svs[i].getElementsByTagName("KhoaHoc")[0].firstChild.data)
        sinhviens.append(sinhvien)
        # print(sinhvien.getMaHSSV())
        # print(unicode(sinhvien.getTen()).encode("utf8"))
    print sinhviens
    return sinhviens 

