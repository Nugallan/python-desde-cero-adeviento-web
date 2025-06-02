import reflex as rx
import adeviento_web.constants as constants
import adeviento_web.styles.styles as styles
from adeviento_web.components.header_text import header_text
from adeviento_web.components.button import button
from adeviento_web.components.day import day
from adeviento_web.styles.styles import Size

def calendar() -> rx.Component:
    return rx.vstack(
        header_text(
            "heart",
            "Calendario de aDEViento"
        ),
        rx.vstack(
            rx.hstack(
                rx.text("El evento comienza en "),
                rx.text(id="countdown"), # 'countdown' es el id del script de assets/js/countdown.js 
                align_items="start"
            ),
            button(
                "Recordar",
                constants.DISCORD_EVENT_URL
            ),
            rx.el.span(
                "• Los regalos son sorpresa, permanecerán ocultos hasta el día de su publicación. No olvides pasarte por aquí cada día para descubrir un nuevo sorteo."
            ),
            class_name="nes-container is-dark with-title",
            align_items="start",
            width= "100%"
        ),
        rx.grid(
            rx.foreach(list(range(1, 25)), lambda number: # uso 'lambda' para pasar el número a la función day
                day(number)
            ),
            # Grid responsivo con breakpoints
            grid_template_columns={
                "base": "repeat(3, 1fr)",      # móvil: 3 columnas
                "sm": "repeat(3, 1fr)",        # tablet pequeña: 3 columnas  
                "md": "repeat(4, 1fr)",        # tablet/desktop: 4 columnas
                "lg": "repeat(5, 1fr)",        # desktop grande: 5 columnas
                "xl": "repeat(6, 1fr)"         # muy grande: 6 columnas
            },
            gap=Size.DEFAULT.value,
            width="100%",
            padding_top=Size.BIG.value
        ),
        rx.script(src="assets/js/countdown.js"),
        style=styles.max_width_style
    )