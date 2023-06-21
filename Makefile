# install
install:
	pip3 install -r requirements.txt


pre-commit:
	pre-commit run


# 預設目標
.DEFAULT_GOAL := install
