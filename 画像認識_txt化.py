# ocr_card.py
import os
from PIL import Image
import pyocr
import pyocr.builders
import tkinter as tk
import tkinter.filedialog as fd

# 1.インストール済みのTesseractのパスを通す
path_tesseract = "C:\\Program Files\\Tesseract-OCR"
if path_tesseract not in os.environ["PATH"].split(os.pathsep):
    os.environ["PATH"] += os.pathsep + path_tesseract

# 2.OCRエンジンの取得
tools = pyocr.get_available_tools()
tool = tools[0]

# 3.開く画像ファイルをダイアログから選択
root = tk.Tk()
root.withdraw()

filename = fd.askopenfilename(
    title="Choose a file",
    filetypes=[("", "*")]
)

# 4.原稿画像の読み込み
img_org = Image.open(filename)

# 5.ＯＣＲ実行
builder = pyocr.builders.TextBuilder()
result = tool.image_to_string(img_org, lang="jpn", builder=builder)

print(result)
print(type(result))

# 6.結果出力
file = fd.asksaveasfilename(
    initialfile="data",
    defaultextension=".txt",
    title="Choose a file",
    initialdir=os.path.join(
        os.path.join(
            os.environ['USERPROFILE']),
        'Desktop'),
    filetypes=[("TEXT", ".txt")]
)

f = open(str(file), 'w', encoding='shift_jis')
f.write(result)
f.close()
