def update_top_scores(new_name, new_score, filename="top_scores.txt"):
    try:
        with open(filename, 'r') as file:
            scores = [line.strip().split() for line in file.readlines()]
            scores = [(name, int(score)) for name, score in [line for line in scores if len(line) == 2]]
    except FileNotFoundError:
        scores = []

    # Ajoute le nouveau score à la liste
    scores.append((new_name, new_score))

    # Trie la liste des scores en ordre décroissant de score
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)

    # Conserve uniquement les 10 meilleurs scores
    top_scores = sorted_scores[:10]

    # Réécrit les meilleurs scores dans le fichier
    with open(filename, 'w') as file:
        for name, score in top_scores:
            file.write(f"{name} {score}\n")

    print(f"Le fichier {filename} a été mis à jour avec les meilleurs scores.")