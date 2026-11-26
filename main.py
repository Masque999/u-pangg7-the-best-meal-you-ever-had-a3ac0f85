LINE = "The best meal I ever had was a street taco at 2 a.m., eaten standing up, juice running down my arm, and I have chased that exact happiness in every restaurant since."

# The entry must be exactly one sentence of at most 200 characters.
assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
assert "\n" not in LINE

import os

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)

assert LINE == LINE.strip(), "line must not have leading or trailing whitespace"

with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)

# Read back and verify: a silent bad write must fail loudly, not ship an empty file.
with open(os.path.join(out_dir, "entry.txt"), encoding="utf-8") as f:
    written = f.read()
assert written == LINE, "entry.txt content does not match LINE"
