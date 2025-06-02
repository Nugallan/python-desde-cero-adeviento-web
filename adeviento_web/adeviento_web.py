import reflex as rx
import adeviento_web.styles.styles as styles
# from adeviento_web.styles.styles import Size
from .views.navbar import navbar
from .views.header import header
from .views.instructions import instructions
from .views.calendar import calendar
from .views.partners import partners
from .views.author import author
from .views.footer import footer
from .components.github import github

def index() -> rx.Component:
    return rx.box( # 'rx.box' sería como usar un 'div' en html
        rx.script("document.documentElement.lang = 'es'"), # Buena práctica indicar el lenguaje de la página
        rx.script(src="/js/snow.js"),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                instructions(),
                calendar(),
                author(),
                partners(),
                footer(),
                github(),
                align="center",
                width="100%",
                spacing="6" # no podríamos usar 'Size.VERY_BIG.value' porque 'vstack' sólo acepta números enteros
            )
        )
    )
    
app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)
app.add_page(
    index,
    title="Calendario de aDEViento 2023 | 24 días. 24 regalos",
    description = "Por cuarto año, ¡aquí está el calendario de adviento sorpresa de nuestra comunidad de developers! Del 1 al 24 de diciembre."
)

# app.compile() -> 'app.compile' está obsoleto