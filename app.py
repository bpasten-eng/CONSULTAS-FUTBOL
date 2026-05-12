import os
import sys
import requests

# ============================================================
# Football Stats CLI — Consulta de Liga de Fútbol
# Stakeholder: Analista deportivo que necesita datos rápidos
# ============================================================

def get_api_key():
    """Lee la API Key desde variable de entorno (sin hardcoding)."""
    key = os.getenv('SPORTSDB_API_KEY')
    if not key:
        print("[ERROR] La variable de entorno SPORTSDB_API_KEY no está definida.")
        print("        Ejecútala así antes de correr el script:")
        print("        export SPORTSDB_API_KEY='1'")
        sys.exit(1)
    return key

def get_league_teams(api_key, league_name="English Premier League"):
    """
    Consulta los equipos de una liga específica.
    Maneja 4+ tipos de errores según los requisitos del proyecto.
    """
    base_url = f"https://www.thesportsdb.com/api/v1/json/{api_key}/search_all_teams.php"
    params = {"l": league_name}

    print(f"\n{'='*55}")
    print(f"  ⚽  FOOTBALL STATS CLI")
    print(f"{'='*55}")
    print(f"  Liga consultada : {league_name}")
    print(f"  Fuente          : TheSportsDB (api.thesportsdb.com)")
    print(f"{'='*55}\n")

    try:
        response = requests.get(base_url, params=params, timeout=10)

        # Error 1: Respuesta HTTP no exitosa (404, 500, etc.)
        if response.status_code == 404:
            print(f"[ERROR 404] Recurso no encontrado en la API.")
            sys.exit(1)
        elif response.status_code == 401:
            print(f"[ERROR 401] Clave de API inválida o sin autorización.")
            sys.exit(1)
        elif response.status_code != 200:
            print(f"[ERROR HTTP {response.status_code}] Respuesta inesperada del servidor.")
            sys.exit(1)

        # Error 2: Respuesta no es JSON válido
        try:
            data = response.json()
        except ValueError:
            print("[ERROR] La respuesta de la API no es un JSON válido.")
            sys.exit(1)

        # Error 3: Datos vacíos o liga no encontrada
        teams = data.get("teams")
        if not teams:
            print(f"[ERROR] No se encontraron equipos para la liga: '{league_name}'.")
            print("        Verifique el nombre exacto de la liga.")
            sys.exit(1)

        return teams

    # Error 4: Timeout de conexión
    except requests.exceptions.Timeout:
        print("[ERROR TIMEOUT] La solicitud tardó demasiado. Verifique su conexión a internet.")
        sys.exit(1)

    # Error 5: Error de conexión (sin internet, DNS, etc.)
    except requests.exceptions.ConnectionError:
        print("[ERROR CONEXIÓN] No se pudo conectar a la API.")
        print("                 Verifique su conexión a internet.")
        sys.exit(1)

    # Error 6: Cualquier otro error de requests
    except requests.exceptions.RequestException as e:
        print(f"[ERROR SOLICITUD] Error inesperado al consultar la API: {e}")
        sys.exit(1)

def display_teams(teams):
    """
    Muestra los datos procesados de los equipos.
    Extrae y muestra ≥3 campos por equipo: nombre, año fundación, estadio, ciudad.
    """
    print(f"  {'N°':<4} {'EQUIPO':<35} {'FUNDADO':<10} {'ESTADIO':<30} {'CIUDAD'}")
    print(f"  {'-'*4} {'-'*35} {'-'*10} {'-'*30} {'-'*20}")

    for i, team in enumerate(teams[:10], start=1):  # Muestra los primeros 10 equipos
        # Campo 1: Nombre del equipo
        nombre = team.get("strTeam", "N/D")
        # Campo 2: Año de fundación
        fundado = team.get("intFormedYear", "N/D")
        # Campo 3: Estadio
        estadio = team.get("strStadium", "N/D")
        # Campo 4: Ciudad
        ciudad = team.get("strCity", "N/D") or "N/D"

        print(f"  {i:<4} {nombre:<35} {str(fundado):<10} {str(estadio):<30} {ciudad}")

    print(f"\n  Total de equipos encontrados: {len(teams)}")
    print(f"{'='*55}\n")

def main():
    api_key = get_api_key()
    league_name = os.getenv('SPORTSDB_LEAGUE', 'English Premier League')

    teams = get_league_teams(api_key, league_name)
    display_teams(teams)

    print("  ✅ Consulta completada exitosamente.")
    print(f"{'='*55}\n")

if __name__ == "__main__":
    main()