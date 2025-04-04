pip install \
--platform manylinux2014_aarch64 \
--target=python \
--implementation cp \
--python-version 3.11 \
--only-binary=:all: --upgrade \
-r \
requirements.txt

zip -r sulmoon2yong-ai-modules.zip python