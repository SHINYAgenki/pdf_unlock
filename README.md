# PDF Unlock Script

このスクリプトは、指定されたディレクトリ内のロックされたPDFファイルを自動的に解除し、解除されたファイルを別のディレクトリに保存するツールです。

## Prerequisites

このスクリプトを使用する前に、以下のソフトウェアがインストールされていることを確認してください:

- Python3
- PyPDF2 ライブラリ

PyPDF2は以下のいずれかのコマンドでインストールできます:

```
pip3 install PyPDF2
```
または
```
pip install PyPDF2
```

## Directory Structure

以下に、プロジェクトのディレクトリ構成を示します
```
/project-root # プロジェクトのルートディレクトリ
├── lockPDF # ここにアンロックしたいPDFを入れる
├── unlockPDF # 解除されたPDFファイルが保存されるディレクトリ
├── unlock_pdf.py # メインスクリプトファイル
└── README.md # プロジェクトの説明、使い方が記載されたドキュメント
```

lockPDFとunlockPDFは各自で作成してください

## 実行例

以下のように実行できます。

```
python3 unlock_pdf.py lockPDF unlockPDF <password>
```

パスワードは開きたいPDFファイルを引数で入れる









