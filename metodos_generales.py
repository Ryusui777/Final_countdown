class MetodosGenerales:
    def __init__(self):
        pass

    @staticmethod
    def get_resolution() \
            -> tuple:
        """
        :return: tuple con las medidas adecuadas para la resolucion de la ventana relativo al tamano del monitor
        """
        from screeninfo import get_monitors
        screen = [monitor for monitor in get_monitors()]
        for primary_screen in screen:
            if primary_screen.is_primary:
                size_tup = (primary_screen.width - (primary_screen.width / 384),
                            primary_screen.height - (primary_screen.height / 13.5))
                return size_tup
