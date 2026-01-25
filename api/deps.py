from fastapi import Depends
from core.security import verificar_api_key

api_key_dep = Depends(verificar_api_key)
