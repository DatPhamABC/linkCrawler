# linkCrawler
Hướng dẫn cài đặt:

## 1. Yêu cầu:
 - Python 3.0 hoặc hơn [python](https://www.python.org/downloads/)
 - Miniconda (không bắt buộc) [miniconda](https://docs.conda.io/en/latest/miniconda.html)
 - [MongoDB](https://docs.mongodb.com/manual/installation/)

## 2. Tạo môi trường (virtual environment - venv):
###  2.1. Không cài đặt Miniconda:
  - Sau khi đã cài đặt python, mở command prompt tại folder muốn chứa môi trường và tạo môi trường (tên môi trường: scrapy):
  	```bash
	python -m venv scrapy
	```
  - Kích hoạt môi trường:
  	```bash
	scrapy\Scripts\activate.bat
	```
  - Cài đặt môi trường theo file requirements.txt: dẫn đến folder có chứa file requirements.txt và chạy:
  	```bash
	pip install -r requirement.txt
	```

###  2.2. Có cài đặt Miniconda:
  - Mở anaconda prompt và chạy:
  	```bash
	conda create --name scrapy
	```
  - Kích hoạt môi trường:
  	```bash
	conda activate scrapy
	```
  - Cài đặt môi trường theo file requirements.txt:
  	```bash
	pip install -r requirement.txt
	```

## 3. Cài đặt và chạy source code:
 - Pull từ github và đặt source code trong folder song song với folder của venv (nếu không có anaconda) hoặc đặt source code trong folder tùy ý (nếu có anaconda)
 - Mở command prompt hoặc anaconda prompt, dẫn đến folder chứa file multiSpider.py và chạy:
 	```bash
	python multiSpider.py
	```
	
## 4. Source code:
### 4.1. multiSpider.py:
 - Tạo nhiều spider chạy song song
 - totalPageCount
 - output: không
 
### 4.2. LinkCrawl.py:
 - class của một spider
 - input: category: trang đầu tiên để bắt đầu lọc
 - output: link của các bài báo có liên quan đến covid
 - Các từ để lọc bài báo được lưu trong const_str

### 4.3. Ghi chú:
 - Dữ liệu được lưu trong MongoDB với hostname localhost và port 27017
 - Mỗi spider mặc định chỉ quét 20 trang
