import sys
import os
import PyPDF2

def unlock_pdf(input_path, output_dir, password):
    # 入力ファイル名を取得し、同じ名前で出力ディレクトリに保存
    output_path = os.path.join(output_dir, os.path.basename(input_path))

    # 入力PDFファイルを読み込む
    with open(input_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        
        # PDFのロックを解除
        if reader.is_encrypted:
            if reader.decrypt(password) == 0:
                raise ValueError("Incorrect password or unable to decrypt PDF.")
        
        # 新しいPDFファイルとして保存
        writer = PyPDF2.PdfWriter()
        for page in reader.pages:
            writer.add_page(page)
        
        with open(output_path, "wb") as outfile:
            writer.write(outfile)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python unlock_pdf.py input_path output_dir password")
    else:
        input_path = sys.argv[1]
        output_dir = sys.argv[2]
        password = sys.argv[3]
        unlock_pdf(input_path, output_dir, password)
