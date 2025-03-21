import numpy as np
import random
from read import load_knapsack_instance, mostrar_estructura

# Parámetros del ACO
num_iterations = 500
num_ants = 30
alpha = 1.0   # Influencia de las feromonas
beta = 3.0    # Influencia de la heurística (beneficio/peso)
rho = 0.4     # Evaporación
Q = 100       # Intensidad de feromona depositada


def initialize_pheromones(num_items):
    """Inicializa el vector de feromonas con un valor pequeño."""
    return np.ones(num_items) * 0.1


def probability_distribution(pheromones, items, allowed_items, alpha, beta):
    """Calcula la probabilidad de seleccionar cada ítem aún no elegido."""
    probabilities = []
    for i in allowed_items:
        tau = pheromones[i] ** alpha
        eta = (items[i]['profit'] / items[i]['weight']) ** beta
        probabilities.append(tau * eta)

    probabilities = np.array(probabilities)
    if probabilities.sum() == 0:
        probabilities = np.ones(len(allowed_items)) / len(allowed_items)
    else:
        probabilities = probabilities / probabilities.sum()

    return probabilities


def construct_solution(pheromones, items, capacity):
    """Cada hormiga construye una solución basada en probabilidades."""
    solution = []
    remaining_capacity = capacity
    allowed_items = list(range(len(items)))

    while allowed_items:
        probabilities = probability_distribution(pheromones, items, allowed_items, alpha, beta)
        chosen_index = np.random.choice(range(len(allowed_items)), p=probabilities)
        chosen_item = allowed_items[chosen_index]

        if items[chosen_item]['weight'] <= remaining_capacity:
            solution.append(chosen_item)
            remaining_capacity -= items[chosen_item]['weight']

        allowed_items.remove(chosen_item)

    return solution


def evaluate_solution(solution, items):
    """Calcula el beneficio total de una solución."""
    total_profit = sum(items[i]['profit'] for i in solution)
    total_weight = sum(items[i]['weight'] for i in solution)
    return total_profit, total_weight


def update_pheromones(pheromones, best_solution, best_profit):
    """Actualiza las feromonas globales."""
    pheromones *= (1 - rho)
    for i in best_solution:
        pheromones[i] += Q / (1 + best_profit)


def aco_knapsack(items, capacity):
    pheromones = initialize_pheromones(len(items))
    best_solution = []
    best_profit = 0

    for iteration in range(num_iterations):
        all_solutions = [construct_solution(pheromones, items, capacity) for _ in range(num_ants)]
        all_profits = [evaluate_solution(sol, items)[0] for sol in all_solutions]

        max_profit = max(all_profits)
        if max_profit > best_profit:
            best_profit = max_profit
            best_solution = all_solutions[all_profits.index(max_profit)]
            print(f"Iteración {iteration+1}: Nueva mejor solución con beneficio {best_profit}")

        update_pheromones(pheromones, best_solution, best_profit)

    return best_solution, best_profit


def main():
    basepath = input("Ingrese el nombre base de la instancia (ejemplo: p05): ")
    capacity, items = load_knapsack_instance(basepath)
    mostrar_estructura(capacity, items)

    best_solution, best_profit = aco_knapsack(items, capacity)

    print("\nMejor solución encontrada:")
    print(f"Ítems seleccionados: {best_solution}")
    print(f"Beneficio total: {best_profit}")
    print(f"Peso total: {sum(items[i]['weight'] for i in best_solution)} de capacidad {capacity}")


if __name__ == "__main__":
    main()
