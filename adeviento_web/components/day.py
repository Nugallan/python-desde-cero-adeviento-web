import reflex as rx
from adeviento_web.styles.styles import Size, Color

def day(number: int, image: str = "gift.png", url: str = "") -> rx.Component:
    return rx.box(
        rx.cond(
            url != "", 
            rx.link( # Pinta el cuadrado del calendario cuando sea distinto de vacío
                rx.image(
                    src=image,
                    alt=f"Regalo asociado al día {number}"
                ),
                href=url,
                is_external=True,
                position="absolute",
            )
        ),
        rx.cond(
            url == "",             
            rx.image(
                src=image,
                alt=f"Regalo asociado al día {number}",
                position="absolute",
            )
        ),
        rx.text(
            number,
            padding=Size.DEFAULT.value,
            position="absolute"
        ),
        bg=Color.ACCENT.value,
        width="100px",
        aspect_ratio="1", # aseguramos que el ancho y el alto sean iguales
        position="relative"
    )