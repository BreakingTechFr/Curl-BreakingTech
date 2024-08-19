import subprocess
import re
import os

# Définition des couleurs
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
    ORANGE = '\033[38;5;208m'

def clear_terminal():
    """Efface le terminal en fonction du système d'exploitation."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_logo():
    logo = """
 _____               _      ______                     _     _                _____              _     
/  __ \             | |     | ___ \                   | |   (_)              |_   _|            | |    
| /  \/ _   _  _ __ | |     | |_/ / _ __   ___   __ _ | | __ _  _ __    __ _   | |    ___   ___ | |__  
| |    | | | || '__|| |     | ___ \| '__| / _ \ / _` || |/ /| || '_ \  / _` |  | |   / _ \ / __|| '_ \ 
| \__/\| |_| || |   | |     | |_/ /| |   |  __/| (_| ||   < | || | | || (_| |  | |  |  __/| (__ | | | |
 \____/ \__,_||_|   |_|     \____/ |_|    \___| \__,_||_|\_\|_||_| |_| \__, |  \_/   \___| \___||_| |_|
                                                                        __/ |                          
                                                                       |___/             
    """
    print(Colors.BLUE + logo + Colors.RESET)

def get_initial_status(url):
    try:
        # Exécuter la commande curl pour obtenir les en-têtes HTTP de l'URL initiale
        result = subprocess.run(['curl', '-I', '-s', '-o', '/dev/null', '-w', '%{http_code}', url],
                                capture_output=True, text=True)
        
        # Récupérer le code de statut HTTP
        http_code = result.stdout.strip()
        return http_code
    
    except Exception as e:
        print(f"Erreur lors de l'exécution de curl pour l'URL initiale : {e}")
        return None

def get_redirections(url):
    try:
        # Exécuter la commande curl avec les options nécessaires pour suivre les redirections
        result = subprocess.run(['curl', '-s', '-L', '-w', '%{url_effective} %{http_code}\\n', '-o', '/dev/null', url],
                                capture_output=True, text=True)
        
        # Récupérer la sortie
        output = result.stdout
        
        # Séparer les différentes lignes
        lines = output.strip().split("\n")
        
        # Liste pour stocker les redirections
        redirections = []
        
        for line in lines:
            match = re.match(r'(.*) (\d{3})$', line.strip())
            if match:
                redirections.append((match.group(1), match.group(2)))

        return redirections
    
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de curl pour les redirections : {e}")
        return []
    except Exception as e:
        print(f"Erreur inattendue lors de l'exécution de curl pour les redirections : {e}")
        return []

def format_status_code(status_code):
    """Retourne le code de statut avec la couleur appropriée."""
    if status_code.startswith('2'):
        return Colors.GREEN + status_code + Colors.RESET
    elif status_code.startswith('3'):
        return Colors.YELLOW + status_code + Colors.RESET
    elif status_code.startswith('4'):
        return Colors.RED + status_code + Colors.RESET
    elif status_code.startswith('5'):
        return Colors.MAGENTA + status_code + Colors.RESET
    else:
        return Colors.BLUE + status_code + Colors.RESET

def main():
    while True:
        # Effacer le terminal avant d'afficher le logo
        clear_terminal()
        
        # Afficher le logo au démarrage
        display_logo()
        
        url = input("Entrez l'URL que vous souhaitez tester (http ou https) : ").strip()
        
        # Vérifier si l'URL commence par http:// ou https://
        if not url.startswith("http://") and not url.startswith("https://"):
            print("L'URL doit commencer par 'http://' ou 'https://'.")
            scheme = input(f"{Colors.ORANGE}Voulez-vous utiliser 'http' ou 'https' ? (Entrez 'http' ou 'https') : {Colors.RESET}").strip().lower()

            if scheme in ['http', 'https']:
                url = scheme + "://" + url
            else:
                print("Schéma non reconnu. Utilisation de 'https://' par défaut.")
                url = "https://" + url
        
        # Obtenir le statut de l'URL initiale
        initial_status = get_initial_status(url)
        
        if initial_status:
            print(f"Statut de l'URL de base ({url}) : {format_status_code(initial_status)}")
        
        # Obtenir les redirections
        redirections = get_redirections(url)
        
        if redirections:
            print("\nListe des redirections :")
            for i, (redirect_url, status_code) in enumerate(redirections[:-1]):
                print(f"Redirection {i + 1} : URL = {redirect_url}, Statut HTTP = {format_status_code(status_code)}")
            
            # Dernière URL et son statut
            final_url, final_status = redirections[-1]
            print(f"\nURL finale : {final_url}, Statut HTTP = {format_status_code(final_status)}")
        else:
            print("Aucune redirection trouvée ou erreur lors de la requête.")
        
        # Demander à l'utilisateur s'il souhaite analyser une autre URL ou quitter
        choice = input(f"\n Souhaitez-vous analyser une autre URL ? (Entrez '1' pour continuer ou '2' pour quitter) : ").strip().lower()
        if choice != '1':
            print("Merci d'avoir utilisé l'application. Au revoir !")
            break

if __name__ == "__main__":
    main()
