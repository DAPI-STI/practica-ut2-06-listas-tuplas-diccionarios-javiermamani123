"""
EX06 (Compendio: listas + tuplas + diccionarios)
Ticket de compra: calcula coste por producto y total general.
"""

PRICES: dict[str, float] = {"Pan": 1.40, "Huevos": 2.30, "Cebolla": 0.85, "Aceite": 4.35}

def checkout(cart: list[tuple[str, int]]) -> tuple[dict[str, float], float]:
    """
    Recibe un carrito como lista de tuplas (producto, unidades).

    Devuelve:
    - Un diccionario con el coste por producto (producto -> coste)
    - Un float con el total general

    Reglas:
    - Si units < 0 -> ValueError
    - Si un producto no existe en PRICES -> ValueError
    - Si un producto aparece varias veces, se acumulan unidades

    Ejemplo:
    [("Pan", 2), ("Huevos", 1), ("Pan", 1)] ->
      ({"Pan": 4.2, "Huevos": 2.3}, 6.5)
    """
    raise NotImplementedError("Implementa checkout(cart)")


def checkout(cart: list[tuple[str, int]]) -> tuple[dict[str, float], float]:
    costs: dict[str, float] = {}
    total = 0.0

    for product, units in cart:
        if units < 0:
            raise ValueError("Las unidades no pueden ser negativas")

        if product not in PRICES:
            raise ValueError(f"Producto no existente: {product}")

        cost = PRICES[product] * units

        if product in costs:
            costs[product] += cost
        else:
            costs[product] = cost

        total += cost

    # 🔧 Redondear resultados
    for product in costs:
        costs[product] = round(costs[product], 2)

    total = round(total, 2)

    return costs, total
