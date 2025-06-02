import reflex as rx

def link_icon(icon: str, url: str) -> rx.Component:
    return rx.link(
        "",
        class_name=f"nes-icon {icon} is-medium", # "nes-icon" es la clase de la fuente de letra de 'https://github.com/nostalgic-css/NES.icons'
        on_click=rx.redirect(
            url,
            is_external=True
        )
    )