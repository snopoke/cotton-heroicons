from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

base = Path(__file__).parent
templates = base.parent / "cotton_heroicons" / "templates" / "cotton" / "heroicon"
index_path = base.parent / "example-project" / "example" / "templates" / "index.html"
index_template = base / "index_template.html"

if __name__ == "__main__":
    variants = {}
    variant_names = ["outline", "solid", "mini", "micro"]

    icons = []
    # loop over all files in 'templates' directory and get HTML files (strip extension)
    for file in templates.iterdir():
        if file.is_file() and file.suffix == '.html':
            icons.append(file.stem.replace("_", "-"))

    env = Environment(
        loader=FileSystemLoader(base),
        autoescape=select_autoescape(),
        block_start_string="<%",
        block_end_string="%>",
        variable_start_string="<<",
        variable_end_string=">>",
    )
    template = env.get_template("index_template.html")
    with open(index_path, "w") as f:
        variant_sizes = {
            "outline": "1.5rem",
            "solid": "1.5rem",
            "mini": "1.25rem",
            "micro": "1rem",
        }
        f.write(template.render(
            icons=icons,
            variants=["outline", "solid", "mini", "micro"],
            variant_sizes=variant_sizes,
        ))
