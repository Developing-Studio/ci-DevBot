![Python-Versions](https://img.shields.io/badge/python-3.8.7-blue?style=flat-square)
![Discord.py-Version](https://img.shields.io/badge/discord.py-1.6.0-blue?style=flat-square)
# DevBot
DevBot - A Bot for DevHub Server which is now open source for it's community!

<img alt="DevBot" align="right" src="mini.png" width=40%/>

## About
[DevHub](https://dsc.gg/leafyserver) is a discord server for developers and DevBot is our personal discord bot! We are also developers of [leafy](https://dsc.gg/leafy) - a multipurpose public discord bot.

#### Sample layout of `.env` file
```bash
TOKEN=token_here
logs = url_here
```

# Contributing Guidelines

## These are few needed things for contributing to Leafy

You should use pre-commit.

```bash
python3 -m pip install pre-commit  # required only once
pre-commit install
```

That's it! The plugin will run every time you commit any changes. If there are any errors found during the run, fix them and commit those changes. You can even run the plugin manually on all files:

```bash
pre-commit run --all-files --show-diff-on-failure
```
* Note - Use `.env` or `.venv` instead of `env` or `venv` ( virtual environments ). It is to prevent pre-commit from scanning them.