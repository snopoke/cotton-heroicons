import itertools
from pathlib import Path

import requests
from bs4 import BeautifulSoup


def get_icons(variant):
    response = requests.get(f"https://heroicons.com/{variant}")
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")

    buttons = soup.find_all("button")
    names = {}
    for button in buttons:
        name = button.get("aria-controls")
        if not name:
            continue

        svg = button.find("svg")
        if svg:
            svg["class"] = "{{ class }}"
            svg["style"] = "{{ styles }}"
            names[name] = svg
    return names


base = Path(__file__).parent
templates = base.parent / "django_heroicons" / "templates" / "cotton" / "heroicon"

if __name__ == "__main__":
    variants = {}
    variant_names = ["outline", "solid", "mini", "micro"]
    for variant in variant_names:
        variants[variant] = get_icons(variant)

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
