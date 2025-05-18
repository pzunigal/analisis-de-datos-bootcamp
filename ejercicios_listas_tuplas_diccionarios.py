ventas = [
    {"fecha": "2024-01-01", "producto": "Camisa", "cantidad": 5, "precio": 20.000},
    {"fecha": "2024-01-01", "producto": "Pantalon", "cantidad": 3, "precio": 40.000},
    {"fecha": "2024-01-02", "producto": "Camisa", "cantidad": 2, "precio": 20.000},
    {"fecha": "2024-01-02", "producto": "Zapatos", "cantidad": 1, "precio": 80.000},
    {"fecha": "2024-01-03", "producto": "Pantalon", "cantidad": 4, "precio": 40.000},
    {"fecha": "2024-01-03", "producto": "Camisa", "cantidad": 3, "precio": 20.000},
    {"fecha": "2024-01-04", "producto": "Zapatos", "cantidad": 2, "precio": 80.000},
]

# Calcular el total de ventas
ingresos_totales = 0
for venta in ventas:
    ingresos_totales += venta["cantidad"] * venta ["precio"]

print(f"Ingresos totales: ${ingresos_totales:.2f}")

# Calcular el producto más vendido
ventas_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    ventas_por_producto[producto] = ventas_por_producto.get(producto, 0) + cantidad

producto_mas_vendido = max(ventas_por_producto, key= ventas_por_producto.get)
cantidad_mas_vendida = ventas_por_producto[producto_mas_vendido]

print(f"Producto más vendido: {producto_mas_vendido} ({cantidad_mas_vendida} unidades)")

# Calcular promedio de ventas por producto
precios_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    precio = venta["precio"]

    if producto not in precios_por_producto:
        precios_por_producto[producto] = (0, 0)

    suma_precios, total_unidades = precios_por_producto[producto]
    precios_por_producto[producto] = (suma_precios + precio * cantidad, total_unidades + cantidad)

print ("Precio promedio por producto:")
for producto, (suma_precios, total_unidades) in precios_por_producto.items():
    promedio = suma_precios / total_unidades
    print(f"- {producto}: ${promedio:.2f}")

## Calcular ingresos por día
ingresos_por_dia = {}
for venta in ventas:
    fecha = venta["fecha"]
    ingreso = venta["fecha"]
    ingreso = venta["cantidad"] * venta["precio"]
    ingresos_por_dia[fecha] = ingresos_por_dia.get(fecha, 0) + ingreso

print("Ingresos por dia:")
for fecha, ingreso in ingresos_por_dia.items():
    print(f"- {fecha}: ${ingreso:.2f}")

# Resumen de ventas por producto
resumen_ventas = {}
for producto in ventas_por_producto:
    suma_precios, total_unidades = precios_por_producto[producto]
    resumen_ventas[producto] = {
        "cantidad_total": total_unidades,
        "ingresos_totales": suma_precios,
        "precio_promedio": suma_precios / total_unidades
    }

print("\nResumen de ventas por producto:")
for producto, datos in resumen_ventas.items():
    print(f"\nProducto: {producto}")
    print(f"- Cantidad total vendida: {datos["cantidad_total"]}")
    print(f"- Ingresos totales: ${datos["ingresos_totales"]:.2f}")
    print(f"- Precio promedio: ${datos["precio_promedio"]:.2f}")
