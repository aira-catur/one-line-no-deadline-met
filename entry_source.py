import os
from pathlib import Path

FINAL_EXCUSE = "I swear I submitted it in my dream last night, and honestly I'm as disappointed as you are that my subconscious doesn't do attachments."


def emit(line: str) -> None:
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target_dir.mkdir(parents=True, exist_ok=True)
    (target_dir / "entry.txt").write_text(line, encoding="utf-8")


if __name__ == "__main__":
    emit(FINAL_EXCUSE)
