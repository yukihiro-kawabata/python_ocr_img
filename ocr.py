try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from glob import glob
import os

def save_file_at_new_dir(new_dir_path, new_filename, new_file_content, mode='w'):
    os.makedirs(new_dir_path, exist_ok=True)
    with open(os.path.join(new_dir_path, new_filename), mode) as f:
        f.write(new_file_content)

RESULT_DIR_PATH = './storage/after/'

files = glob('storage/before/*.png')
files_count = len(files)

for i, img in enumerate(files):

    # ファイル名を取得（拡張子なし）
    file_name = os.path.splitext(os.path.basename(img))[0]
    
    # 日本語で文字出力
    jp_result = pytesseract.image_to_string(Image.open(img), lang='jpn')
    print(jp_result)

    # 抽出した文字をテキストで保存
    save_file_at_new_dir(RESULT_DIR_PATH, file_name + '.txt', jp_result)

    # ボックス(座標位置付き)出力
    # print(pytesseract.image_to_boxes(Image.open(img), lang='jpn'))

    # OSD(Orientation and script detection)
    # print(pytesseract.image_to_osd(Image.open(img), lang='jpn'))

    # HOCR形式出力
    # print(pytesseract.image_to_pdf_or_hocr(img, extension='hocr'))
