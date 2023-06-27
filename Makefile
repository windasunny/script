# install
install:
	pip3 install -r requirements.txt

commit
	codegpt commit

commit-pre
	codegpt commit --preview

pre-commit:
	pre-commit run


# 預設目標
.DEFAULT_GOAL := install
