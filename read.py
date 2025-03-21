def read_capacity(filepath):
    with open(filepath, "r") as f:
        capacity = int(f.read().strip())
    return capacity

def read_list(filepath):
    with open(filepath, "r") as f:
        content = f.read().strip().split()
        return [int(x) for x in content]

def load_knapsack_instance(basepath):
    capacity = read_capacity(f"{basepath}_c.txt")
    weights = read_list(f"{basepath}_w.txt")
    profits = read_list(f"{basepath}_p.txt")
    items = [{"weight": w, "profit": p} for w, p in zip(weights, profits)]
    return capacity, items

def mostrar_estructura(capacity, items):
    print("\n=== Estructura de la instancia cargada ===")
    print(f"Capacidad de la mochila: {capacity}")
    print(f"Cantidad de objetos: {len(items)}")
    print("\nObjetos:")
    print(f"{'ID':<5} {'Peso':<10} {'Beneficio':<10} {'Ratio (P/W)':<10}")
    print("-" * 40)
    for i, item in enumerate(items, start=1):
        ratio = item['profit'] / item['weight'] if item['weight'] != 0 else 0
        print(f"{i:<5} {item['weight']:<10} {item['profit']:<10} {ratio:<10.2f}")
    print("=" * 40)

# Ejemplo de uso:
if __name__ == "__main__":
    basepath = "p05"  
    capacity, items = load_knapsack_instance(basepath)
    mostrar_estructura(capacity, items)
