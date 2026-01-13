"""
EX02 (Listas)
Eliminar duplicados manteniendo el orden de aparición.
"""

def unique_preserve_order(values: list[int]) -> list[int]:
    """
    Devuelve una NUEVA lista sin duplicados, manteniendo el orden.

    Ejemplo:
    - [3, 1, 3, 2, 1] -> [3, 1, 2]

    Requisito:
    - No modifiques la lista original.
    """
    raise NotImplementedError("Implementa unique_preserve_order(values)")

def unique_preserve_order(values: list[int]) -> list[int]:
    result = []
    for v in values:
        if v not in result:
            result.append(v)
    return result
