from pathlib import Path


lists = ["youtube", "reddit", "instagram"]
special_comments = {
	"Title": "ublock-distractions",
	"Expires": "12 hours",
	"Homepage": "https://github.com/tgrants/ublock-distractions",
	"Description": "Block algorithmic feeds and distractions. Compatible with uBlock Origin."
}


def comment(flist):
	result = ""
	for key, value in special_comments.items():
		result += f"! {key}: {value}\n"
	return result + "\n" + flist


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
		content = fo.write(comment(content))

out_path = Path("build/all.txt")
with out_path.open("w") as fo:
	content = fo.write(comment(all))
