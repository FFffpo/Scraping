from PIL import Image
import numpy as np
import pytesseract
from pytesseract import Output


def cleanFile(filePath, threshold):
    image = Image.open(filePath)
    image = image.point(lambda x: 0 if x < threshold else 255)
    return image


def getConfidence(image):
    data = pytesseract.image_to_data(
        image, lang='chi_sim', output_type=Output.DICT)
    # 读中文，加上lang='chi_sim'
    text = data['text']
    confidences = []
    numChars = []

    for i in range(len(text)):
        if int(data['conf'][i]) > -1:
            confidences.append(data['conf'][i])
            numChars.append(len(text[i]))

    return np.average(confidences, weights=numChars), sum(numChars)


filePath = 'C:\\Users\\jzwdq\\Desktop\\1.png'

start = 40
step = 5
end = 90

for threshold in range(start, end, step):
    image = cleanFile(filePath, threshold)
    image.save('C:\\Users\\jzwdq\\Desktop\\'+str(threshold)+'.png')
    scores = getConfidence(image)
    print("threshold: "+str(threshold)+",confidence: " +
          str(scores[0])+"numChars "+str(scores[1]))
