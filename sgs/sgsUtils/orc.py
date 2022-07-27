import ddddocr

#识别图像中的数字
def getNumber(img):
    ocr = ddddocr.DdddOcr()
    with open(img, 'rb') as f:
        img_bytes = f.read()
    res = ocr.classification(img_bytes)
    return res
