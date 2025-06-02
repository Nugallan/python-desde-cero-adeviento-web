import datetime
import reflex as rx
import adeviento_web.constants as constants
import adeviento_web.styles.styles as styles
from adeviento_web.styles.styles import Size, Color, TextColor
from adeviento_web.components.header_text import header_text
from adeviento_web.components.button import button

def author() -> rx.Component:
    return rx.vstack(
        header_text(
            "like",
            "Hola, mi nombre es Brais Moure"
        ),
        rx.flex(
            rx.image(
                src="avatar.jpg",
                width="128px",
                height="128px",
                bg=Color.PRIMARY.value,
                padding="2px",
                border=f"4px solid {Color.SECONDARY.value}",
                border_radius="50%",
                margin_right=Size.SMALL.value,
                margin_bottom=Size.SMALL.value
            ),
            rx.vstack(
                rx.el.span(
                    f"Soy ingeniero de software desde hace más de {experience()} años."    
                ),
                rx.el.span(
                    "En 2018 comencé a divulgar contenido sobre programación y desarrollo de software en redes sociales como ",
                    rx.el.span(
                        "@mouredev.",
                        color=TextColor.ACCENT.value,
                        font_size=Size.DEFAULT.value
                    )
                ),
                rx.mobile_only(
                    rx.vstack(
                        author_buttons()
                    )
                ),
                rx.tablet_and_desktop(
                    rx.hstack(
                        author_buttons()
                    )
                ),
                width="100%",
                align_items="start"
            ),
            align_items="start",
            spacing="6",
            flex_direction=["column", "column", "column", "row", "row"]
        ),
        style=styles.max_width_style
    )
    
def author_buttons() -> rx.Component:
    return rx.box(
        button(
            "Youtube",
            constants.YOUTUBE_URL
        ),button(
            "Twitch",
            constants.TWITCH_URL
        ),button(
            "Discord",
            constants.DISCORD_URL
        ),
    )
    
def experience() -> int:
    return datetime.date.today().year - 2010