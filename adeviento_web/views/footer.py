import reflex as rx
import adeviento_web.constants as constants
import adeviento_web.styles.styles as styles
from adeviento_web.styles.styles import Size, TextColor


def footer() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.text(
                "Calendario de aDEViento 2023",
                font_size=Size.MEDIUM.value,
                margin_bottom=Size.ZERO.value
            ),
            rx.link(
                "Creado con ",
                rx.el.i(class_name="nes-icon is-small heart"),
                " (y gracias a ti) por MoureDev by Brais Moure",
                href=constants.MOUREDEV_URL,
                is_external=True,
                font_size=Size.MEDIUM.value,
                color=TextColor.TERTIARY.value
            ),
            align_items="start",
            spacing="4" # no podríamos usar 'Size.MEDIUM.value' porque 'vstack' sólo acepta números enteros
        ),
        rx.spacer(),
        rx.image(
            src="logo.png",
            alt="Logo MoureDev. Una letra \"eme\" entre dos corchetes.",
            class_name="nes-avatar is-large"
        ),
        padding_bottom=Size.BIG.value,
        style=styles.max_width_style,
        align_items="center"
    )