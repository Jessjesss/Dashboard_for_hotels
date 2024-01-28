import csv


data = [
    (1, "phone", "Po telefonu"),
    (2, "email", "Po elektronnoy pochte"),
    (3, "vk", "Bot ili direct"),
    (4, "instagram", "direct"),
    (5, "Telegram", "bot"),
    (6, "website_module", "Modul bronirovaniya na sajte"),
    (7, "OTA", "Cherez OTA"),
    (8, "reception", "Prodazhi s resepshn")
]

with open("booking_channels.csv", "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file, delimiter=",")
    writer.writerow(["booking_channel_id", "booking_channel_name", "description"])
    for row in data:
        writer.writerow(row)