import itertools
import subprocess
import tempfile
from pathlib import Path

from bs4 import BeautifulSoup

VARIANT_PATHS = {
    "outline": "optimized/24/outline",
    "solid": "optimized/24/solid",
    "mini": "optimized/20/solid",
    "micro": "optimized/16/solid",
}


def get_icons(variant, repo_dir):
    svg_dir = Path(repo_dir) / VARIANT_PATHS[variant]
    icons = {}
    for svg_file in sorted(svg_dir.glob("*.svg")):
        soup = BeautifulSoup(svg_file.read_text(), "html.parser")
        svg = soup.find("svg")
        if svg:
            svg["class"] = "{{ class }}"
            svg["style"] = "{{ styles }}"
            icons[svg_file.stem] = svg
    return icons


base = Path(__file__).parent
templates = base.parent / "cotton_heroicons" / "templates" / "cotton" / "heroicon"

if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmpdir:
        subprocess.run(
            ["git", "clone", "--depth", "1",
             "https://github.com/tailwindlabs/heroicons.git", tmpdir],
            check=True,
        )

        variants = {}
        variant_names = ["outline", "solid", "mini", "micro"]
        for variant in variant_names:
            variants[variant] = get_icons(variant, tmpdir)

    template = (base / "icon_template.html").read_text()
    all_names = set(
        itertools.chain.from_iterable([list(variant) for variant in variants.values()])
    )
    for name in all_names:
        local_template = str(template)
        for variant, icons in variants.items():
            icon = icons.get(name)
            if icon:
                local_template = local_template.replace(
                    f"__{variant.upper()}__", str(icon)
                )
        out = templates / f"{name.replace('-', '_')}.html"
        out.write_text(local_template)
