import os
import json
import logging
import requests

import pandas as pd

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    logging.info("Starting to scrape champion")
    logging.info("Initializing Chrome driver")

    languages = pd.read_csv("data/language.csv").language.tolist()
    release_date = pd.read_csv("data/release_date.csv", index_col="id")
    lanes = pd.read_csv("data/lane.csv", index_col="id")
    regions = pd.read_csv("data/region.csv", index_col="id")

    for language in languages:
        url = requests.get(
            f"https://ddragon.leagueoflegends.com/cdn/14.21.1/data/{language}/champion.json"
        )

        champion_information = json.loads(url.text)["data"]

        rows = []

        for champion in champion_information:
            logging.info(f"Scraping {language} data for champion : {champion}")

            row = []

            champion_id = champion_information[champion]["id"]
            champion_name = champion_information[champion]["name"]
            champion_title = champion_information[champion]["title"]

            champion_splash = f"https://ddragon.leagueoflegends.com/cdn/img/champion/splash/{champion}_0.jpg"
            champion_loading = f"https://ddragon.leagueoflegends.com/cdn/img/champion/loading/{champion}_0.jpg"
            champion_square = f"https://ddragon.leagueoflegends.com/cdn/14.21.1/img/champion/{champion}.png"

            url = requests.get(
                f"https://ddragon.leagueoflegends.com/cdn/14.21.1/data/{language}/champion/{champion}.json"
            )

            champion_detail = json.loads(url.text)["data"][champion]

            champion_spell_1 = f'https://ddragon.leagueoflegends.com/cdn/14.21.1/img/spell/{champion_detail["spells"][0]["id"]}.png'
            champion_spell_2 = f'https://ddragon.leagueoflegends.com/cdn/14.21.1/img/spell/{champion_detail["spells"][1]["id"]}.png'
            champion_spell_3 = f'https://ddragon.leagueoflegends.com/cdn/14.21.1/img/spell/{champion_detail["spells"][2]["id"]}.png'
            champion_spell_4 = f'https://ddragon.leagueoflegends.com/cdn/14.21.1/img/spell/{champion_detail["spells"][3]["id"]}.png'
            champion_passive = f'https://ddragon.leagueoflegends.com/cdn/14.21.1/img/passive/{champion_detail["passive"]["image"]["full"]}'

            tags_traduction = pd.read_csv(f"data/tags/{language}.csv", index_col="id")

            tags = champion_detail["tags"]
            tags = [tags_traduction.loc[tag, "name"] for tag in tags]
            tags = "*".join(tags)

            region_traduction = pd.read_csv(
                f"data/region/{language}.csv", index_col="id"
            )

            region = regions.loc[champion_id, "region"]
            region = region_traduction.loc[region, "name"]

            rows.append(
                [
                    champion_id,
                    champion_name,
                    champion_title,
                    tags,
                    region,
                    lanes.loc[champion_id, "lane"],
                    release_date.loc[champion_id, "release_date"],
                    champion_splash,
                    champion_loading,
                    champion_square,
                    champion_spell_1,
                    champion_spell_2,
                    champion_spell_3,
                    champion_spell_4,
                    champion_passive,
                ]
            )

        df = pd.DataFrame(
            rows,
            columns=[
                "id",
                "name",
                "title",
                "tags",
                "region",
                "lane",
                "release_date",
                "splash",
                "loading",
                "square",
                "spell_1",
                "spell_2",
                "spell_3",
                "spell_4",
                "passive",
            ],
        )

        output_dir = "data/champion"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        df.to_csv(f"{output_dir}/champion_{language}.csv", index=False)
