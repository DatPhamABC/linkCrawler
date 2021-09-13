# linkCrawler
Hướng dẫn cài đặt:

## 1. Cài đặt python (phiên bản 3.0 hoặc hơn):
 - Tải và cài đặt theo hướng dẫn tại: https://www.python.org/downloads/

## 2. Cài đặt Miniconda (không bắt buộc):
 - Tải và cài đặt Miniconda theo hướng dẫn tại: https://docs.conda.io/en/latest/miniconda.html

## 3. Tạo môi trường (virtual environment - venv):
###  3.1. Không cài đặt Miniconda:
  - Sau khi đã cài đặt python, mở command prompt tại folder muốn chứa môi trường và chạy:
	python -m venv [ten moi truong]
  - Kích hoạt môi trường:
	[ten moi truong]\Scripts\activate.bat (hoặc chạy file activate.bat trong folder của môi trường)
  - Cài đặt môi trường theo file requirements.txt: dẫn đến folder có chứa file requirements.txt và chạy:
	pip install -r requirement.txt

###  3.2. Có cài đặt Miniconda:
  - Mở anaconda prompt và chạy:
	conda create --name [ten moi truong]
  - Kích hoạt môi trường:
	conda activate [ten moi truong]
  - Cài đặt môi trường theo file requirements.txt:
	pip install -r requirement.txt

## 4. Cài đặt MongoDB:
 - Tải và cài đặt MongoDB theo hướng dẫn tại: https://docs.mongodb.com/manual/installation/

## 5. Cài đặt và chạy source code:
 - Pull từ github và đặt source code trong folder song song với folder của venv (nếu không có anaconda) hoặc đặt source code trong folder tùy ý (nếu có anaconda)
 - Mở command prompt hoặc anaconda prompt, dẫn đến folder chứa file multiSpider.py (spiderRun.py) và chạy:
	python multiSpider.py
  hoặc python spiderRun.py
