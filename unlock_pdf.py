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
                print(f"Failed to decrypt {input_path}.")
                return  # パスワードが間違っている場合は次のファイルに進む
        
        # 新しいPDFファイルとして保存
        writer = PyPDF2.PdfWriter()
        for page in reader.pages:
            writer.add_page(page)
        
        with open(output_path, "wb") as outfile:
            writer.write(outfile)
        print(f"Unlocked {input_path} saved to {output_path}")

def unlock_all_pdfs(lock_dir, unlock_dir, password):
    # lock_dir内のすべてのPDFファイルを見つける
    for file in os.listdir(lock_dir):
        if file.endswith(".pdf"):
            input_path = os.path.join(lock_dir, file)
            unlock_pdf(input_path, unlock_dir, password)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python unlock_pdf.py lock_dir unlock_dir password")
    else:
        lock_dir = sys.argv[1]
        unlock_dir = sys.argv[2]
        password = sys.argv[3]
        unlock_all_pdfs(lock_dir, unlock_dir, password)
