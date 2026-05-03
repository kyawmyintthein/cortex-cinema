def map_movie_context(details: dict, credits: dict) -> dict:
    return {
        "title": details["title"],
        "overview": details["overview"],
        "genres": details["genres"],
        "releaseYear": details["release_year"],
        "director": credits["director"],
        "topCast": credits["top_cast"],
        "popularityBand": details["popularity_band"],
    }
