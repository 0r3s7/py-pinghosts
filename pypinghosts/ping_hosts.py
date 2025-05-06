import subprocess
import csv

#Funzione che carica host da file .txt
def carica_host_da_txt(percorso_file):
    with open(percorso_file, "r", encoding="utf-8") as f: 
        return [riga.strip() for riga in f if riga.strip()]

#Funzione che effettua ping 
def ping_pc(host):
    try:
        print(f"Eseguo: ping -n 4 {host}")
        risultato = subprocess.run(
            ["ping", "-n", "4", host],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            creationflags=subprocess.CREATE_NO_WINDOW #per non aprire shell cmd ad ogni ping
        )
        print(f"Output:\n{risultato.stdout}")
        print(f"Codice di ritorno: {risultato.returncode}")
        if risultato.returncode == 0:
            return "Raggiungibile"
        else:
            return "Non raggiungibile"
    except Exception as e:
        print(f"Errore per {host}: {e}")
        return "Errore"


# Carica i DNSHostName dal file
lista_pc = carica_host_da_txt("hosts.txt")

# Apri file CSV in scrittura
with open("risultati_ping.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Host", "Stato"])

    for pc in lista_pc:
        stato = ping_pc(pc)
        print(f"{pc} -> Terminale {stato}")
        writer.writerow([pc, stato])
