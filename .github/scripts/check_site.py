"""Check local page and asset targets in a generated Jekyll site."""

import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit


class References(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        key = "href" if tag in {"a", "link"} else "src"
        if tag in {"a", "link", "img", "script", "iframe", "source"}:
            if attrs.get(key):
                self.urls.append(attrs[key])


def main():
    root = Path(sys.argv[1]).resolve()
    origin = sys.argv[2].rstrip("/")
    host = urlsplit(origin).netloc
    pages = sorted(root.rglob("*.html"))
    if not (root / "index.html").is_file():
        raise SystemExit("Missing generated home page")

    broken = set()
    checked = set()
    for page in pages:
        parser = References()
        parser.feed(page.read_text(encoding="utf-8"))
        path = "/" + page.relative_to(root).as_posix()
        if path.endswith("index.html"):
            path = path[:-len("index.html")]
        for reference in parser.urls:
            target = urlsplit(urljoin(origin + path, reference))
            if target.scheme not in {"http", "https"} or target.netloc != host:
                continue
            local = (root / unquote(target.path).lstrip("/")).resolve()
            if not local.is_relative_to(root):
                broken.add((path, reference))
                continue
            if local.is_dir():
                local /= "index.html"
            checked.add(target.path)
            if not local.is_file():
                broken.add((path, reference))

    for source, target in sorted(broken):
        print(f"Broken link: {source} -> {target}")
    print(f"Checked {len(pages)} HTML pages and {len(checked)} internal targets.")
    return bool(broken)


if __name__ == "__main__":
    sys.exit(main())
