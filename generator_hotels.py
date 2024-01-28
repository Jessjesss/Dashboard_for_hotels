import csv

data = [
    ['hotel_id', 'name', 'address', 'phone_number', 'count_rooms', 'description'],
    [1, 'Greenland', 'Sheregesh, ul. Snezhnaya 8/1', '+7384732014144', 38, 'Otel u podnozhia gory, na sektore A, god postroiki 2008. Rasschitan na srednii klass.'],
    [2, 'SHER', 'Sheregesh, ul. Lunnaya 34', '+7384732034244', 41, 'Sovremennii otel, v 2 km. ot trass sektora B. God postroiki 2017. Premium segment'],
    [3, 'Berg hotel', 'Sheregesh, ul. Ryabinovaya 40', '+7384732154145', 38, 'Sovremennii otel, raspolozhen na sektore B. God postroiki 2019. Premium segment'],
    [4, 'Ski inn', 'Sheregesh, ul. Ryabinovaya 212', '+7384732013133', 66, 'Sovremennii otel, raspolozhen na sektore F. God postroiki 2020. Premium segment']
]

with open('hotels.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(data)
