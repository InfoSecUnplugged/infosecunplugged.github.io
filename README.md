# Info Sec. Unplugged website

Build the environment with:

```bash
poetry install --with dev
```

Add packages:

```bash
poetry add python-slugify==8.0.4
poetry add --dev tomlkit
```

Build the website:

```bash
poetry run ./build.py
```
