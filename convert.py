import json
import os
import datetime
from pathlib import Path
import subprocess

TEMPLATE = """---
title: "{title}"
date: {date}
draft: false
tags: {tags}
---

{content}
"""


def main():
    cwd = Path(".")
    tils = cwd / "tils"
    tils.mkdir(parents=True, exist_ok=True)
    for fpath in cwd.glob("*/*.md"):
        if fpath.parent == Path("tils"):
            continue
        with fpath.open() as file:
            bdate = subprocess.check_output(
                ["git", "log", "-1", "--pretty=format:%ci", str(fpath)]
            ).decode()
            date = datetime.datetime.strptime(bdate, "%Y-%m-%d %H:%M:%S %z")
            # 2021-03-23T15:01:17+07:00
            naive_date_s = date.strftime("%Y-%m-%dT%H:%M:%S")
            _timezone = date.strftime("%z")
            timezone = f"{_timezone[:3]}:{_timezone[3:]}"
            date_s = f"{naive_date_s}{timezone}"
            title = fpath.stem.replace("-", " ").title()
            content = file.read()
            content = (
                content.replace("## Issue", "## Question")
                .replace("## Qustion", "## Question")
                .replace("## Solution", "## Answer")
                .replace("## Resolution", "## Answer")
            )
            new_content = TEMPLATE.format(
                title=title,
                date=date_s,
                tags=json.dumps([str(fpath.parent)]),
                content=content,
            )
            with open(tils / fpath.name, "w") as new_file:
                new_file.write(new_content)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
