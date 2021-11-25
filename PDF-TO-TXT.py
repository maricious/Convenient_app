# プログラム1｜ライブラリ設定
import sys
from pathlib import Path
from subprocess import call
import tkinter as tk
import tkinter.filedialog as fd


# プログラム2｜PDFテキストを格納するリスト作成
item_list = []

# プログラム3｜開くPDFファイルをダイアログから選択
root = tk.Tk()
root.withdraw()

filename = fd.askopenfilename(
    title="Choose a file",
    filetypes=[("PDF", ".pdf")]
)

# プログラム4｜pdf2txt.pyを指定
py_path = Path(sys.exec_prefix) / "Scripts" / "pdf2txt.py"

# プログラム5｜出力先をダイアログから選択
file = fd.asksaveasfilename(
    initialfile="data",
    defaultextension=".txt",
    title="Choose a file",
    filetypes=[("TEXT", ".txt")]
)

# プログラム6｜テキストファイルを出力
call(["py", str(py_path), "-o" + str(file), "-p 1", filename])
