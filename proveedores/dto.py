from pydantic import BaseModel
from typing import Optional

class ProveedorDTO(BaseModel):
    id: Optional[int]
    nombre: str
    direccion: str
    email: str
    telefono: str
    cuit: str
    razon_social: str
    deleted: bool = False

    class Config:
        orm_mode = True
