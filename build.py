from pathlib import Path

lists = ["youtube", "reddit"]
all = ""

build_dir = Path("build")
build_dir.mkdir(parents=True, exist_ok=True)

for l in lists:
	in_path = Path("lists") / (l + ".txt")
	with in_path.open("r") as fi:
		content = fi.read()
	all += content
	out_path = Path("build") / (l + ".txt")
	with out_path.open("w") as fo:
		content = fo.write(content)

out_path = Path("build/all.txt")
with out_path.open("w") as fo:
	content = fo.write(all)
