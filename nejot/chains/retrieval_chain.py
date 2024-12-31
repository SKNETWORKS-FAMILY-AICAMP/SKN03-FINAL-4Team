from nejot.chains.embedding_chain import get_openai_embedding
from nejot.utils.similarity_utils import calculate_similarity

def search_with_cached_embeddings(embedding_cache, spec, all_data, similarity_threshold=0.95):
    if not embedding_cache:
        return {"details":"DB 관련 상세정보를 찾지 못했습니다."}
    user_embedding = get_openai_embedding(spec)
    if user_embedding is None:
        return {"details":"DB 관련 상세정보를 찾지 못했습니다."}

    best_match = {"model": None, "similarity": 0}
    for model_name, embedding in embedding_cache.items():
        sim = calculate_similarity(user_embedding, embedding)
        if sim > best_match["similarity"]:
            best_match = {"model": model_name, "similarity": sim}

    if best_match["similarity"] > similarity_threshold:
        for row in all_data:
            if row['Model'] == best_match['model']:
                rank = row.get('Rank', 'N/A')
                benchmark = row.get('Benchmark', 'N/A')
                url = row.get('URL', 'N/A')
                type_ = row.get('Type', 'N/A')
                brand = row.get('Brand', 'N/A')
                information = row.get('information', 'N/A')

                detailed_info = (
                    f"Type: {type_}\n"
                    f"Brand: {brand}\n"
                    f"Model: {best_match['model']}\n"
                    f"Rank: {rank}\n"
                    f"Benchmark: {benchmark}\n"
                    f"URL: {url}\n"
                    f"Information: {information}\n"
                )
                return {
                    "model": best_match['model'],
                    "rank": rank,
                    "benchmark": benchmark,
                    "url": url,
                    "similarity": best_match["similarity"],
                    "details": detailed_info
                }
        return {"details":"DB 관련 상세정보를 찾지 못했습니다."}
    else:
        return {"details":"DB 관련 상세정보를 찾지 못했습니다."}
