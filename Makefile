.PHONY: build

build:
	pyinstaller --noconfirm --onefile --console  "./convert.py"