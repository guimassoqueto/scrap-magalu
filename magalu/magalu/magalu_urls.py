MAGALU_URLS = {
    "beleza_magalu": [f"https://www.magazineluiza.com.br/beleza-e-perfumaria/l/pf/seller---magazineluiza/?page={i}" for i in range(1, 16)],
    "beleza_epoca": [f"https://www.magazineluiza.com.br/beleza-e-perfumaria/l/pf/seller---epocacosmeticos-integra/?page={i}" for i in range(1, 16)],
    "cama_mesa_banho": [f"https://www.magazineluiza.com.br/cama-mesa-e-banho/l/cm/seller---magazineluiza/?page={i}" for i in range(1, 6)],
    "eletrodomesticos": [f"https://www.magazineluiza.com.br/eletrodomesticos/l/ed/seller---magazineluiza/?page={i}" for i in range(1, 6)],
    "informatica": [f"https://www.magazineluiza.com.br/informatica/l/in/?page={i}" for i in range(1, 6)],
    "games": [f"https://www.magazineluiza.com.br/games/l/ga/seller---magazineluiza/?page={i}" for i in range(1, 2)],
    "mercado": [f"https://www.magazineluiza.com.br/mercado/l/me/seller---magazineluiza/?page={i}" for i in range(1, 6)],
    "moveis": [f"https://www.magazineluiza.com.br/moveis/l/mo/seller---magazineluiza/?page={i}" for i in range(1, 2)],
    "tv_video": [f"https://www.magazineluiza.com.br/tv-e-video/l/et/seller---magazineluiza/?page={i}" for i in range(1, 2)],
    "utilidades_domesticas": [f"https://www.magazineluiza.com.br/utilidades-domesticas/l/ud/seller---magazineluiza/?page={i}" for i in range(1, 2)],
    "smartphones": [f"https://www.magazineluiza.com.br/celulares-e-smartphones/l/te/seller---magazineluiza/?page={i}" for i in range(1, 2)]
}

def get_urls(categories: str):
    categories = categories.split(',')
    urls = []

    for category in categories: 
        urls += MAGALU_URLS[category]

    return urls