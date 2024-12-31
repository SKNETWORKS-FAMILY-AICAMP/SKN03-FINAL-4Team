import torch
import openai
import os
from nejot.config import OPENAI_API_KEY, EMBEDDING_CACHE_FILE
from nejot.utils.similarity_utils import calculate_similarity

openai.api_key = OPENAI_API_KEY
device = "cpu"

def get_openai_embedding(text):
    try:
        response = openai.Embedding.create(
            model="text-embedding-ada-002",
            input=[text]
        )
        embedding = response["data"][0]["embedding"]
        return torch.tensor(embedding, device="cpu")
    except Exception as e:
        print(f"임베딩 생성 오류: {e}")
        return None

def load_cached_embeddings():
    if os.path.exists(EMBEDDING_CACHE_FILE):
        data = torch.load(EMBEDDING_CACHE_FILE, map_location="cpu")
        return data
    else:
        return {}

def update_embedding_cache(model_name, information):
    from config import EMBEDDING_CACHE_FILE
    new_embedding = get_openai_embedding(model_name + " " + information.strip() if information else model_name)
    if new_embedding is not None:
        if os.path.exists(EMBEDDING_CACHE_FILE):
            embedding_cache = torch.load(EMBEDDING_CACHE_FILE, map_location="cpu")
        else:
            embedding_cache = {}
        embedding_cache[model_name] = new_embedding
        torch.save(embedding_cache, EMBEDDING_CACHE_FILE)
        print(f"'{model_name}'에 대한 임베딩 캐시 업데이트 완료.")
    else:
        print(f"'{model_name}'에 대한 임베딩 생성 실패. 캐시 업데이트를 건너뜹니다.")