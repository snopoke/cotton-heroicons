# cotton-heroicons

A [Django Cotton](https://django-cotton.com/) Component Library of [Heroicons](https://heroicons.com/)

## Usage

To use the icons in your templates, simply add the component tag with the icon name as the tag name. The default variant
is 'outline', but you can specify a different variant using the 'variant' attribute.

Any additional HTML attributes (e.g. `class`, `id`) are passed directly to the `<svg>` element.

Each variant has a default size that matches the Heroicons recommendations:
- **outline** / **solid**: 1.5rem (24px)
- **mini**: 1.25rem (20px)
- **micro**: 1rem (16px)

You can override the default size by passing a `style` attribute.

```html
<!-- The default variant is 'outline' -->
<c-heroicon.cloud />

<!-- Specify the variant with the 'variant' attribute -->
<c-heroicon.shopping-bag variant="mini" />

<!-- Add additional classes -->
<c-heroicon.square-3-stack-3d class="text-violet-700" />

<!-- Override the default size -->
<c-heroicon.eye style="width: 0.75rem; height: 0.75rem;" />
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
