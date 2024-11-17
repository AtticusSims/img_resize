# Image Resizer Script / 画像リサイズスクリプト

[English](#english) | [日本語](#japanese)

# <a name="english"></a>English

This Python script resizes images in a folder so that their shortest side is 1024 pixels while maintaining aspect ratio. It supports various image formats including JPEG, PNG, BMP, TIFF, and HEIF/HEIC (iPhone photos).

## Prerequisites

1. Python 3.6 or higher installed on your system
2. pip (Python package installer)

### Installing Python

#### Windows:
1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run the installer
3. **Important**: Check "Add Python to PATH" during installation
4. Verify installation by opening Command Prompt and typing:
   ```bash
   python --version
   ```

#### Mac:
1. Install Homebrew if you haven't already:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. Install Python using Homebrew:
   ```bash
   brew install python
   ```
3. Verify installation by opening Terminal and typing:
   ```bash
   python3 --version
   ```

## Installation

1. First, create a new folder for the project and copy `resize_to_side.py` into it.

2. Install the required Python packages:

   #### Windows:
   Open Command Prompt and run:
   ```bash
   pip install Pillow pillow-heif
   ```

   #### Mac:
   Open Terminal and run:
   ```bash
   pip3 install Pillow pillow-heif
   ```

## Usage

1. Open Terminal (Mac) or Command Prompt (Windows)

2. Navigate to the folder containing the script:

   #### Windows:
   ```bash
   cd C:\path\to\script\folder
   ```

   #### Mac:
   ```bash
   cd /path/to/script/folder
   ```

3. Run the script:

   #### Windows:
   ```bash
   python resize_to_side.py
   ```

   #### Mac:
   ```bash
   python3 resize_to_side.py
   ```

4. When prompted, enter the full path to the folder containing your images:

   #### Windows example:
   ```
   Enter the path to the folder containing images: C:\Users\YourName\Pictures\MyPhotos
   ```

   #### Mac example:
   ```
   Enter the path to the folder containing images: /Users/YourName/Pictures/MyPhotos
   ```

5. The script will:
   - Create a new folder with '_resized' added to the original folder name
   - Process all supported images in the input folder
   - Save resized versions to the new folder
   - Print progress messages for each processed image

## Supported Image Formats

- JPEG (.jpg, .jpeg)
- PNG (.png)
- BMP (.bmp)
- TIFF (.tiff)
- HEIF/HEIC (.heif, .heic) - These will be converted to JPEG

## Notes

- Original images are not modified; resized versions are saved to a new folder
- HEIF/HEIC images (iPhone photos) are automatically converted to JPEG format
- Images are resized so their shortest side is exactly 1024 pixels
- Aspect ratio is always maintained
- Output images are saved with 95% quality for optimal file size and visual quality

## Troubleshooting

If you encounter errors:

1. Ensure all required packages are installed:
   - Windows: `pip list`
   - Mac: `pip3 list`

2. Check that Python is properly installed:
   - Windows: `python --version`
   - Mac: `python3 --version`

3. If you get "command not found":
   - Windows: Ensure Python is added to PATH
   - Mac: Try using `python3` instead of `python`

4. Check that the input folder path is correct:
   - Windows: Use backslashes (\\) or forward slashes (/)
   - Mac: Use forward slashes (/)

5. Verify you have write permissions in the parent folder
6. For HEIF/HEIC images, ensure pillow-heif is properly installed

## Example

#### Windows:
Input folder:
```
C:\Photos\Vacation
```
Output folder:
```
C:\Photos\Vacation_resized
```

#### Mac:
Input folder:
```
/Users/YourName/Photos/Vacation
```
Output folder:
```
/Users/YourName/Photos/Vacation_resized
```

---

# <a name="japanese"></a>日本語

このPythonスクリプトは、フォルダ内の画像の短辺を1024ピクセルにリサイズします。アスペクト比を維持したまま、JPEG、PNG、BMP、TIFF、HEIF/HEIC（iPhoneの写真）などの様々な画像形式に対応しています。

## 必要条件

1. Python 3.6以上がインストールされていること
2. pip（Pythonパッケージインストーラー）

### Pythonのインストール

#### Windows:
1. [python.org](https://www.python.org/downloads/)からPythonをダウンロード
2. インストーラーを実行
3. **重要**: インストール時に「Add Python to PATH」にチェックを入れる
4. コマンドプロンプトを開き、以下のコマンドで確認:
   ```bash
   python --version
   ```

#### Mac:
1. Homebrewがまだの場合、インストール:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. Homebrewを使用してPythonをインストール:
   ```bash
   brew install python
   ```
3. ターミナルを開き、以下のコマンドで確認:
   ```bash
   python3 --version
   ```

## インストール

1. 新しいフォルダを作成し、`resize_to_side.py`をそこにコピー

2. 必要なPythonパッケージをインストール:

   #### Windows:
   コマンドプロンプトを開き、実行:
   ```bash
   pip install Pillow pillow-heif
   ```

   #### Mac:
   ターミナルを開き、実行:
   ```bash
   pip3 install Pillow pillow-heif
   ```

## 使用方法

1. ターミナル（Mac）またはコマンドプロンプト（Windows）を開く

2. スクリプトのあるフォルダに移動:

   #### Windows:
   ```bash
   cd C:\path\to\script\folder
   ```

   #### Mac:
   ```bash
   cd /path/to/script/folder
   ```

3. スクリプトを実行:

   #### Windows:
   ```bash
   python resize_to_side.py
   ```

   #### Mac:
   ```bash
   python3 resize_to_side.py
   ```

4. 画像フォルダのパスを入力:

   #### Windows例:
   ```
   Enter the path to the folder containing images: C:\Users\YourName\Pictures\MyPhotos
   ```

   #### Mac例:
   ```
   Enter the path to the folder containing images: /Users/YourName/Pictures/MyPhotos
   ```

5. スクリプトの動作:
   - 元のフォルダ名に'_resized'を追加した新しいフォルダを作成
   - 入力フォルダ内のサポートされている画像を処理
   - リサイズされた画像を新しいフォルダに保存
   - 処理状況をメッセージで表示

## 対応画像形式

- JPEG (.jpg, .jpeg)
- PNG (.png)
- BMP (.bmp)
- TIFF (.tiff)
- HEIF/HEIC (.heif, .heic) - JPEGに変換されます

## 注意事項

- 元の画像は変更されません。リサイズされた画像は新しいフォルダに保存
- HEIF/HEIC画像（iPhone写真）は自動的にJPEG形式に変換
- 画像の短辺が1024ピクセルになるようにリサイズ
- アスペクト比は常に維持
- 出力画像は95%の品質で保存（最適なファイルサイズと画質のバランス）

## トラブルシューティング

エラーが発生した場合:

1. 必要なパッケージがインストールされているか確認:
   - Windows: `pip list`
   - Mac: `pip3 list`

2. Pythonが正しくインストールされているか確認:
   - Windows: `python --version`
   - Mac: `python3 --version`

3. 「command not found」エラーの場合:
   - Windows: PythonがPATHに追加されているか確認
   - Mac: `python`の代わりに`python3`を使用

4. 入力フォルダのパスが正しいか確認:
   - Windows: バックスラッシュ(\\)または前方スラッシュ(/)を使用
   - Mac: 前方スラッシュ(/)を使用

5. 親フォルダへの書き込み権限があるか確認
6. HEIF/HEIC画像の場合、pillow-heifが正しくインストールされているか確認

## 例

#### Windows:
入力フォルダ:
```
C:\Photos\Vacation
```
出力フォルダ:
```
C:\Photos\Vacation_resized
```

#### Mac:
入力フォルダ:
```
/Users/YourName/Photos/Vacation
```
出力フォルダ:
```
/Users/YourName/Photos/Vacation_resized
```
