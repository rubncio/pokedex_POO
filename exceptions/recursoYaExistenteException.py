from fastapi import HTTPException
class RecursoYaExistenteException(HTTPException):
    def __init__(recurso: str):
        super.__init__(409, f"este recurso de {recurso} ya existe")