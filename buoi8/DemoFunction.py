danh_sach = [1,2,3,4,5,6,7,8,9,10]

danh_sach_chan = list(filter(lambda a:a%2==0, danh_sach))

print(danh_sach_chan)

danh_sach_nhan_doi = list(map(lambda a:a*2,danh_sach))

print(danh_sach_nhan_doi)
#Toi muon chinh sua mot thong tin
