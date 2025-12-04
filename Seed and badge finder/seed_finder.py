from collections import defaultdict
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import networkx as nx
import argparse


def select_initial_seed_set(node_embeddings, second_order_neighbors, k=10, beta=0.4):
    seed_set = set()
    no_embeddings = set()
    node_influence = defaultdict(set)

    # Filter second-order neighbors by similarity > beta
    for node, neighbors in second_order_neighbors.items():
        if node not in node_embeddings:
            no_embeddings.add(node)
            continue

        filtered_neighbors = set()
        for neighbor in neighbors:
            if neighbor not in node_embeddings:
                no_embeddings.add(neighbor)
                continue

            similarity = cosine_similarity(
                node_embeddings[node].reshape(1, -1),
                node_embeddings[neighbor].reshape(1, -1)
            )[0][0]

            if similarity > beta:
                filtered_neighbors.add(neighbor)

        node_influence[node] = filtered_neighbors

    # Greedy top-k selection
    influenced_nodes = set()
    while len(seed_set) < k:
        best_node = None
        max_influence = 0

        for node, influences in node_influence.items():
            unique_influences = influences - influenced_nodes
            if len(unique_influences) > max_influence:
                best_node = node
                max_influence = len(unique_influences)

        if best_node is None:
            break

        seed_set.add(best_node)
        influenced_nodes.update(node_influence[best_node])

        # Remove influenced nodes
        for node in node_influence:
            node_influence[node] -= influenced_nodes

    return list(seed_set)



def get_second_order_neighbors(edge_index):
    G = nx.DiGraph()
    G.add_edges_from(edge_index)

    second_order_neighbors = defaultdict(set)

    for node in G.nodes():
        first_order = set(G.successors(node))
        second_order = set()

        for neighbor in first_order:
            second_order.update(G.successors(neighbor))

        second_order.discard(node)
        second_order_neighbors[node] = second_order

    return second_order_neighbors



# ⭐ NEW FUNCTION YOU CAN IMPORT AND USE ⭐
def get_top_k_seeds(k=10, beta=0.4,
                    embedding_file='dict_node_embedding',
                    edge_file='original_edge_index.pkl'):
    """
    Loads embeddings and edges, computes neighbors, selects seeds,
    and returns the top-k seed list.
    """

    # Load embeddings
    with open(embedding_file, 'rb') as file:
        features = pickle.load(file)

    # Load edge index
    with open(edge_file, 'rb') as file:
        edge_index = pickle.load(file)

    # Compute second-order neighbors
    second_order_neighbors = get_second_order_neighbors(edge_index)

    # Select and return seeds
    return select_initial_seed_set(
        node_embeddings=features,
        second_order_neighbors=second_order_neighbors,
        k=k,
        beta=beta
    )



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Select top-k influential nodes.")
    parser.add_argument("--k", type=int, default=10,
                        help="Number of seed nodes to select (default = 10).")
    parser.add_argument("--beta", type=float, default=0.4,
                        help="Similarity threshold (default = 0.4).")

    args = parser.parse_args()

    seeds = get_top_k_seeds(k=args.k, beta=args.beta)
    print("Selected Seed Nodes:", seeds)
