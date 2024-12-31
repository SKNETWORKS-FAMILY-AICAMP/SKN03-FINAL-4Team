import torch

def calculate_similarity(vec1, vec2):
    if vec1.device != vec2.device:
        vec2 = vec2.to(vec1.device)
    vec1 = vec1 / torch.norm(vec1)
    vec2 = vec2 / torch.norm(vec2)
    similarity = torch.dot(vec1, vec2)
    return similarity.item()