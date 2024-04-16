import os

# Functie om een KNMI-bestand in te lezen
def lees_knmi_bestand(bestandsnaam):
    try:
        with open(bestandsnaam, 'r') as f:
            lines = f.readlines()
            return lines
    except FileNotFoundError:
        print("Het opgegeven bestand kon niet worden gevonden.")
        return None
    except Exception as e:
        print("Er is een fout opgetreden bij het lezen van het bestand:", str(e))
        return None

# Functie om de inhoud van het KNMI-bestand te tonen
def toon_knmi_inhoud(bestandsinhoud):
    if bestandsinhoud:
        for line in bestandsinhoud:
            print(line.strip())  # Strip om eventuele witruimte te verwijderen
    else:
        print("Er is geen geldige inhoud om weer te geven.")

# Hoofdprogramma
if __name__ == "__main__":
    # Volledig pad naar het KNMI-bestand
    bestandsnaam = "C:\\xampp\\htdocs\\parsing\\bron.txt"

    # Controleer of het bestand bestaat
    if os.path.exists(bestandsnaam):
        knmi_inhoud = lees_knmi_bestand(bestandsnaam)  # Inhoud van het KNMI-bestand lezen

        # De inhoud van het KNMI-bestand tonen
        toon_knmi_inhoud(knmi_inhoud)

        input("Druk op Enter om af te sluiten...")
    else:
        print("Het opgegeven bestand kon niet worden gevonden.")
