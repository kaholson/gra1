import random

def character_creation():
    print("Witaj w świecie, gdzie pokój i technologia nie zapełniają pustki w twoim sercu.")
    print("Jako sierota powojenna musisz wybrać swoją ścieżkę.\n")
    
    stats = {"HP": 10, "MaxHP": 10, "Ekwipunek": [], "Status": []}


    # Życie przed wojskiem
    print("Życie było ciężkie, więc musiałeś zmusić się do:")
    print("1. Złodziejstwa")
    print("2. Rozbójnictwa")
    print("3. Uczciwej pracy")
    choice = input("Wybierz (1/2/3): ").strip()
    if choice == "1":
        stats["Ekwipunek"].append("Wytrych")
        print("Wybrałeś życie złodzieja.")
    elif choice == "2":
        stats["HP"] += 5
        stats["MaxHP"] += 5
        print("Wybrałeś życie rozbójnika.")
    else:
        print("Wybrałeś uczciwą pracę.")

    # Trening w armii
    print("\nKrol postanowil powolac cala mlodziez do wojska")
    print("\nPodczas służby trenowałeś:")
    print("1. Fechtunek")
    print("2. Strzelectwo")
    print("3. Magię")
    choice = input("Wybierz (1/2/3): ").strip()
    if choice == "1":
        stats["Ekwipunek"].extend(["Miecz", "Tarcza"])
        print("Wybrałeś fechtunek.")
    elif choice == "2":
        stats["Ekwipunek"].extend(["Łuk", "Kołczan"])
        print("Wybrałeś strzelectwo.")
    elif choice == "3":
        stats["Ekwipunek"].append("Magiczny patyk")
        stats["Status"].append("Czarodziej")
        print("Wybrałeś magię.")

    # Nauka przedmiotu
    print("\nJako część armii zostałeś zmuszony do nauki:")
    print("1. Biologii")
    print("2. Botanologii")
    print("3. Magii")
    choice = input("Wybierz (1/2/3): ").strip()
    if choice == "1":
        stats["Status"].append("Biolog")
        print("Zyskałeś wiedzę o biologii.")
    elif choice == "2":
        stats["Status"].append("Botanik")
        print("Zyskałeś wiedzę o botanice.")
    elif choice == "3":
        if "Czarodziej" not in stats["Status"]:
            stats["Status"].append("Czarodziej")
            print("Zyskałeś wiedzę o magii.")
        else:
            stats["Status"].append("Potężny czarodziej")
            print("Zyskałeś wiedzę o magii i stałeś się potężnym czarodziejem.")

    # Ostatni dzień przygotowań
    print("\nOstatniego dnia przygotowań postanowiłeś:")
    print("1. Oddać się rozpuście w mieście")
    print("2. Zabrać dodatkowy prowiant i sprzęt")
    print("3. Spakować apteczkę")
    choice = input("Wybierz (1/2/3): ").strip()
    if choice == "1":
        stats["Status"].append("Wczorajszy")
        print("zmeczyly cie nocne ekscesy.")
    elif choice == "2":
        stats["Ekwipunek"].extend(["Pochodnia", "Prowiant"])
        print("Czujesz sie przygotowany.")
    elif choice == "3":
        stats["Ekwipunek"].append("Apteczka")
        print("Spakowałeś apteczkę.")

    print("\n=== Twój Bohater ===")
    print(f"HP: {stats['HP']}/{stats['MaxHP']}")
    print("Ekwipunek:", ", ".join(stats["Ekwipunek"]))
    print("Status:", ", ".join(stats["Status"]))
    print("\nCzas nadszedł.")
    forest(stats)

def forest(stats):
    print("\nUdajecie się do lasu. Nagle słychać krzyki zewsząd.")
    print("Twoja grupa została zaatakowana przez wrogą armię. Uciekasz w stronę lasu.")

    # Definicja wydarzeń i ich wag
    events = [
        "Napotkałeś wilka!",
        "Znalazłeś opuszczoną skrzynię.",
        "Spotkałeś wędrowca, który proponuje pomoc."
    ]
    weights = [0.3, 0.3, 0.4]  # Zrównoważone proporcje

    # Dynamiczne losowanie wydarzeń
    event = random.choices(events, weights=weights, k=1)[0]
    print(event)

    # Obsługa wydarzenia
    if "skrzynię" in event:
        if "Wytrych" in stats["Ekwipunek"]:
            print("Używasz wytrychu, aby otworzyć skrzynię. Znalazłeś miksturę zdrowia!")
            stats["Ekwipunek"].append("Mikstura zdrowia")
        else:
            print("Nie masz wytrychu, więc nie możesz otworzyć skrzyni.")
    elif "wilka" in event:
        if "Miecz" in stats["Ekwipunek"]:
            print("Udaje ci się zabić wilka bez obrażeń.")
        else:
            print("Wilk atakuje cię z nienacka. Udaje ci się uciec, ale tracisz zdrowie.")
            stats["HP"] -= 5
            if stats["HP"] <= 0:
                print("\n=== Zakończenie: Zginąłeś ===")
                return None
    elif "wędrowca" in event:
        print("\nSpotykasz wędrowca. Co robisz?")
        print("1. Zostań z nim.")
        print("2. Zabij go i schowaj się w jego mieszkaniu.")
        print("3. Zignoruj go i idź dalej.")
        if "Potężny czarodziej" in stats["Status"]:
            print("4. Dzięki wiedzy magicznej, rozumiesz, że proponuje ci obalenie króla. Zgadzasz się na to.")

        choice = input("Wybierz (1/2/3/4): ").strip()
        if choice == "1":
            print("Zostałeś z wędrowcem. Twoja podróż kończy się tutaj.")
            print("\n=== Zakończenie 1/11 ===")
            return None
        elif choice == "2":
            print("Zabiłeś wędrowca i schowałeś się w jego mieszkaniu. Niestety, armia cię dopadła.")
            print("\n=== Zakończenie 2/11 ===")
            return None
        elif choice == "3":
            print("Ignorujesz wędrowca i idziesz dalej.")
        elif choice == "4":
            print("Wędrowiec przekonuje cię do obalenia króla.")
            stats["Status"].append("Rebelia")

    if "Botanik" in stats["Status"]:
        print("Znajdujesz trującą roślinę i zatrzymujesz ją na później.")
        stats["Ekwipunek"].append("Trująca roślina")
        next(stats)
    else:
        next(stats)

    # Wybór dalszej drogi
def next(stats):
    print("\nStoisz przed wyborem drogi:")
    print("1. Przejście przez jaskinię.")
    print("2. Przejście przez górę.")
    choice = input("Wybierz (1/2): ").strip()

    if choice == "1":  #jaskinia
        if "Pochodnia" in stats["Ekwipunek"] or ("Czarodziej" in stats["Status"] and "Magiczny patyk" in stats["Ekwipunek"]):
            print("Masz światło. Udaje ci się przejść przez jaskinię.")
            print("Znajdujesz dziwny kamień!")
            stats["Ekwipunek"].append("Kamień runiczny")
            city(stats)
        else:
            print("Nie masz światła i gubisz się w ciemności. Umierasz z wycieńczenia.")
            stats["HP"] = 0
            if stats["HP"] <= 0:
                print("\n=== Zakończenie 3/11===")
                return stats
        #gora
    elif choice == "2":
        print("Przechodzisz przez trudny teren górski. Niestety skręciłeś kostkę.")
        stats["HP"] -= 5
        if "Apteczka" in stats["Ekwipunek"]:
            print("Używasz apteczki, aby opatrzyć skręconą kostkę. Odzyskujesz część zdrowia.")
            stats["HP"] += 4
        elif stats["HP"] <= 0:
            print("Twoje rany sa za ciezkie. Umierasz")
            print("\n=== Zakończenie 4/11 ===")   

        if "Biolog" in stats["Status"]:
                print("Podążasz za śladami zwierząt i unikasz walki z cyklopem.")
                city(stats)
        else:
            mountain(stats)

    #gora cd
def mountain(stats):
    print("Na drodze pojawia się cyklop!")

    if "Botanik" in stats["Status"] and "Trująca roślina" in stats["Ekwipunek"]:
        print("Zatruwasz swój miecz trującą rośliną i pokonujesz cyklopa.")
        print("Jednak trochę ucierpiales podczas walki.")
        stats["HP"] -= 2
        stats["Ekwipunek"].append("Oko cyklopa")
    elif "Łuk" in stats["Ekwipunek"]:
        if "Wczorajszy" in stats["Status"]:
            print("Jesteś zbyt zmęczony, aby celnie strzelić. Cyklop cię zabija.")
            stats["HP"] = 0
            return stats
        else:
            print("Celny strzał w oko zabija cyklopa! Zyskujesz jego oko jako trofeum.")
            stats["Ekwipunek"].append("Oko cyklopa")
    else:
        print("Nie masz broni. Uciekasz, ale tracisz zdrowie.")
        stats["HP"] -= 5

    if stats["HP"] <= 0:
        print("Twoje rany sa za glebokie. Umierasz")
        print("\n=== Zakończenie 5/11 ===")
        return stats
    else:
        city(stats)

#miasto
def city(stats):
    if stats["HP"] < stats["MaxHP"] // 2:
        print("Jesteś poważnie ranny i masz mniej niż połowę zdrowia.")
        if random.random() < 0.3:
            print("Wykrwawiasz się przed bramą miasta. Umierasz.")
            print("\n=== Zakończenie 6/11 ===")
            return
        else:
            print("Cudem docierasz do bramy miasta.")
    print("Dotarles do miasta zmeczony po ciezkiej podrozy. Co robisz?")
    print("1. Poddajesz się i nic nie mówisz.")
    print("2. Próbujesz dostać się do pałacu.")
    if "Kamień runiczny" in stats["Ekwipunek"] and "Czarodziej" in stats["Status"]:
        print("3.Uciekasz przy pomocy kamienia runicznego do innego kraju.")

    choice = input("Wybierz (1/2): ").strip()

    if choice == "1":
        print("Poddajesz się straży miejskiej i zostajesz aresztowany.")
        print("\n=== Zakończenie 7/11 ===")
    elif choice == "3":
            print("Rozpoczynasz nowe życie.")
            print("\n=== Zakończenie 8/11 ===")
            return stats
    else:
        palace(stats)

#koniec
def palace(stats):
    if "Rebelia" in stats["Status"]:
        print("Wykorzystujesz swoje moce, aby obalić króla. Przejmujesz miasto i rozpoczynasz rządy jako nowy władca.")
        print("\n=== Zakończenie 11/11: Nowy Władca ===")
    elif "Oko cyklopa" in stats["Ekwipunek"]:
        print("Król docenia twoje trofeum i zamiast egzekucji wysyła cię do więzienia.")
        print("\n=== Zakończenie 10/11 ===")
    else:
        print("Zostajesz oskarżony o dezercję i skazany na śmierć.")
        print("\n=== Zakończenie 9/11 ===")


if __name__ == "__main__":
    while True:
        print("\n=== Witaj w grze ===")
        stats = character_creation() 
        if stats: 
            stats = forest(stats) 

        play_again = input("\nCzy chcesz zagrać ponownie? (tak/nie): ").strip().lower()
        if play_again != "tak":
            print("Dzięki za grę!")
            break