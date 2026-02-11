# cotton-heroicons

A [Django Cotton](https://django-cotton.com/) Component Library of [Heroicons](https://heroicons.com/)

## Usage

To use the icons in your templates, simply add the component tag with the icon name as the tag name. The default variant
is 'outline', but you can specify a different variant using the 'variant' attribute.

Any additional HTML attributes (e.g. `class`, `style`, `id`) are passed directly to the `<svg>` element.

```html
<!-- The default variant is 'outline' -->
<c-heroicon.cloud />

<!-- Specify the variant with the 'variant' attribute -->
<c-heroicon.shopping-bag variant="mini" />

<!-- Add additional classes -->
<c-heroicon.square-3-stack-3d class="text-violet-700" />

<!-- Control size with classes or style -->
<c-heroicon.eye class="w-3 h-3" />
<c-heroicon.eye style="width: 2rem; height: 2rem;" />
```

### Outline variant options

The outline variant exposes `stroke_width`, `stroke_linecap`, and `stroke_linejoin` attributes:

```html
<c-heroicon.cloud stroke_width="2" />
```

## Installation

```bash
pip install cotton-heroicons
```

Update Django settings:

```python
INSTALLED_APPS = [
    ...
    'django_cotton',
    'cotton_heroicons',
    ...
]
```
