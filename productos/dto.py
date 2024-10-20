from pydantic import BaseModel
from typing import Optional
from datetime import date

class ProductoDTO(BaseModel):
    id: Optional[int]
    codigo: str
    descripcion: str
    precio_compra: float
    precio_venta: float
    categoria: str
    stock: int
    reposicion: int
    proveedor_id: int
    lote: Optional[str] = None
    vencimiento: Optional[date] = None

    class Config:
        orm_mode = True
