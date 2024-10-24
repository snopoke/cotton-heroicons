# cotton-heroicons

A [Django Cotton](https://django-cotton.com/) Component Library of [Heroicons](https://heroicons.com/)

## Usage

To use the icons in your templates, simply add the component tag with the icon name as the tag name. The default variant
is 'outline', but you can specify a different variant using the 'variant' attribute. You can also add additional classes
using the 'class' attribute.

```html
<!-- The default variant is 'outline' -->
<c-heroicon.cloud/>

<!-- Specify the variant with the 'variant' attribute -->
<c-heroicon.shopping-bag variant="mini"/>

<!-- Add additional classes using the 'class' attribute -->
<c-heroicon.square-3-stack-3d class="text-violet-700"/>
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
