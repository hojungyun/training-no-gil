# Test with optional GIL

## 1. Install python 3.13.1 and 3.13.1t using pyenv

```shell
pyenv install --list | grep 3\.13
pyenv install 3.13.1
pyenv install 3.13.1t
pyenv versions
ls -l ~/.pyenv/versions
```

## 2. Run the scripts

### From terminal 1:

```shell
cd <project_dir>
poetry install
poetry run python cpu_usage.py
```

### From terminal 2:

```shell
cd <project_dir>
~/.pyenv/versions/3.13.1/bin/python main.py
~/.pyenv/versions/3.13.1t/bin/python main.py
```

# Reference
https://medium.com/@r_bilan/python-3-13-without-the-gil-a-game-changer-for-concurrency-5e035500f0da