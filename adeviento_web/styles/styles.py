import reflex as rx
from enum import Enum
from .fonts import Font
from .colors import Color, TextColor

MAX_WIDTH = "1200px" # típico limitar el ancho de la web a que no pase de 1000px 

class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em" # valor de la fuente por defecto
    BIG = "2em"
    BUTTON = "2.75em"
    VERY_BIG = "4em"

STYLESHEETS = [
    "https://unpkg.com/nes.css@latest/css/nes.min.css", # importamos la fuente de letra de 'https://github.com/nostalgic-css/NES.icons'
    "https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap", # importamos la fuente de letra de 'https://fonts.google.com' con el estilo 'Press start 2P'    
]

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "color": TextColor.PRIMARY.value,
    "background": Color.PRIMARY.value,
    rx.heading: {
        "font_family": Font.DEFAULT.value,
        "color": TextColor.ACCENT.value
    },
    rx.link: {
        "text_decoration": "none",
        "_hover": {
            "color": TextColor.ACCENT.value,
            "text_decoration": "none"
        }
    },
    rx.el.span: {
        "font_size": Size.MEDIUM.value
    },
    rx.button: {
        "margin_bottom": Size.DEFAULT.value,
        "height": Size.BUTTON.value,
        "color": f"{TextColor.SECONDARY.value} !important",
        "_hover": {
            "color": f"{TextColor.PRIMARY.value} !important"
        }
    },
    "cursor": "url('https://unpkg.com/nes.css@latest/assets/cursor.png'), auto",  # Cursor personalizado
}

max_width_style = dict(
    align_items="center",
    padding_x=Size.BIG.value,
    width="100%",
    max_width=MAX_WIDTH
)