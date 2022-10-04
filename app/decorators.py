# -*- coding: utf-8 -*-

def sqlexception_handler(sqlfunc):
    def inner_function(*args, **kwargs):
        try:
            sqlfunc(*args, **kwargs)
        except Exception as error:
            return "Ocurrió un error con el manejo de la DB - " + str(error.orig) + " - " + str(error.params)
    return inner_function
