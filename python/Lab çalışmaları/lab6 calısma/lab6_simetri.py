import Image
res = Image.open("OrnekResim.jpg")
print "Tur   :", res.format, "\nBoyut :", res.size, "\nRenk :", res.mode
ters = res.transpose(Image.ROTATE_180)
ters.show()
