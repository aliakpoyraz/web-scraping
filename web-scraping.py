import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://teknofest.org" 
table_url = "https://teknofest.org/tr/competitions/competition_report/?category=4&search=&page={}"

data_list = []

for page in range(1,100):
    print(f"Sayfa {page} işleniyor...")
    response = requests.get(table_url.format(page))
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        tbody = soup.find("tbody", id="myTable")

        if tbody:
            rows = tbody.find_all("tr")

            for row in rows:
                cells = row.find_all("td")
                if len(cells) == 4:
                    th_cells = row.find_all("th")
                    if th_cells:
                        competition_name = th_cells[0].text.strip()
                    else:
                        competition_name = cells[0].text.strip() 

                    detail_link = cells[3].find("a")
                    if detail_link:
                        detail_url = base_url + detail_link.get('href')
                    else:
                        detail_url = "Link bulunamadı"

                    data_list.append({
                        "Yarışma Adı": competition_name,
                        "Takım Adı": cells[0].text.strip(),
                        "Yıl": cells[1].text.strip(),
                        "Detay": detail_url
                    })
        else:
            print(f"Sayfa {page} - tbody bulunamadı.")
    else:
        print(f"Sayfa {page} yüklenemedi. Durum kodu: {response.status_code}")

df = pd.DataFrame(data_list)
df.to_csv("/Users/aak/Desktop/teknofest_verileri.csv", index=False, encoding="utf-8")
print("Veriler tablo_verileri.csv dosyasına kaydedildi.")