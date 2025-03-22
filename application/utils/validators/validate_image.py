from django.core.exceptions import ValidationError


def is_png_svg(image):
    if not image.name.lower().endswith('.png') and not image.name.lower().endswith('.svg'):
        raise ValidationError('Deve ser PNG ou SVG.')
    