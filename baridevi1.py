def solution(n, ratings):
    # Criar um dicionário para armazenar as avaliações de cada prato
    dishes_ratings = {}

    # Percorrer as avaliações e atualizar o dicionário
    for i in range(n):
        dish_id, rating = ratings[i]
        if dish_id not in dishes_ratings:
            dishes_ratings[dish_id] = [rating, 1]  # [soma das avaliações, quantidade de avaliações]
        else:
            dishes_ratings[dish_id][0] += rating
            dishes_ratings[dish_id][1] += 1

    # Encontrar o prato mais bem avaliado (maior média de avaliações)
    max_avg_rating = 0
    best_dish_id = None
    for dish_id, (total_rating, num_reviews) in dishes_ratings.items():
        avg_rating = total_rating / num_reviews
        if avg_rating > max_avg_rating:
            max_avg_rating = avg_rating
            best_dish_id = dish_id

    return best_dish_id

# Entrada de amostra:
n = 5
ratings = [[512, 3], [123, 4], [987, 2], [512, 3], [123, 3]]
out_ = solution(n, ratings)
print(out_)  # Saída de amostra: 1 (o prato com ID 1 recebeu a média de avaliação mais alta)
