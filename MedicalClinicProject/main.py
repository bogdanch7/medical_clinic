class programare:
    nume = ""
    nume_doctor = ""
    data = ""
    numele_analizei = ""
    durata_analizei = ""
    ora_analizei = ""
    medic_cautat = ""
    pacient_cautat = ""
    nume_pacient = ""
    pret = 0

users = {}
logat = False
programari = []
suma = 0
print("Bine ați venit la clinica noastră medicală! ")
while True:
    if logat:
        print("Selectați opțiunea: ")
        print("1. Pentru a face o programare la clinica noastră. ")
        print("2. Pentru a afișa programările. ")
        print("3. Pentru a modifica datele unei programări. ")
        print("4. Pentru a filtra programările în funcție de numele medicului. ")
        print("5. Pentru a filtra programările în funcție de numele pacientului. ")
        print("6. Pentru a calcula suma de plată a mai multor analize ale unui pacient. ")
        print("7. Pentru a anula o programare. ")
        print("8. Pentru a vă deconecta. ")
        inp = int(input())
        if inp == 2:
            print("Afișează programările. ")
            for i in programari:
                print("Pacientul", i.nume, "are o programare la doctorul", i.nume_doctor, "în data de", i.data + ".", "Numele analizei este", i.numele_analizei + ",", "având durata de", i.durata_analizei, "minute", "de la ora", i.ora_analizei, "și prețul de", i.pret, "RON.")
        elif inp == 1:
            print("Fă o programare la clinica noastră. ")
            t = programare()
            t.nume = str(input("Introduceți numele pacientului: "))
            t.nume_doctor = str(input("Introduceți numele medicului: "))
            t.data = str(input("Introduceți data analizei (data va avea formatul ZZ/LL): "))
            t.numele_analizei = str(input("Introduceți numele analizei: "))
            t.durata_analizei = int(input("Introduceți durata analizei (minute): "))
            t.ora_analizei = str(input("Introduceți ora programării (HH:MM): "))
            t.pret = int(input("Introduceți prețul analizei (RON): "))
            programari.append(t)
            print("Ați adăugat o nouă programare! ")
        elif inp == 3:
            print("Modifică datele unei programări. ")
            id = int(input("Poziția programării în listă: "))
            t = programare
            t.nume = str(input("Introduceți noul nume al pacientului: "))
            t.nume_doctor = str(input("Introduceți noul nume al doctorului: "))
            t.data = str(input("Introduceți noua dată a analizei (ZZ/LL): "))
            t.numele_analizei = str(input("Introduceți numele analizei: "))
            t.durata_analizei = str(input("Introduceți durata analizei (minute): "))
            t.ora_analizei = str(input("Introduceți noua oră a analizei (HH:MM): "))
            t.pret = str(input("Introduceți prețul analizei (RON): "))
            programari[id] = t
            print("Ați modificat detaliile programării! ")
        elif inp == 4:
            print("Afișează programările în funcție de numele medicului: ")
            medic_cautat = input("Introduceți numele medicului: ")
            for programare in programari:
                if programare.nume_doctor == medic_cautat:
                    print("Pacientul", programare.nume, "are o programare la medicul", programare.nume_doctor, "în data de", programare.data + ".")
            print("Ați afișat programările! ")
        elif inp == 5:
            print("Afișează programările în funcție de numele pacientului: ")
            pacient_cautat = input("Introduceți numele pacientului: ")
            for i in programari:
                if i.nume == pacient_cautat:
                    print("Pacientul", i.nume, "are o programare la doctorul", i.nume_doctor, "în data de", i.data + ".", "Numele analizei este", i.numele_analizei + ",", "având durata de", i.durata_analizei, "minute", "la ora", i.ora_analizei, "și prețul de", i.pret, "RON.")
            print("Ați afișat programările! ")
        elif inp == 6:
            print("Afișează suma de plată a analizelor ale pacientului dat: ")
            nume_pacient = input("Introduceți numele pacientului: ")
            for programare in programari:
                if programare.nume == nume_pacient:
                    suma += int(programare.pret)
                    print(f"Suma analizelor pacientului", nume_pacient, "este", suma, "RON.")
            print("Ați afisat suma analizelor! ")
        elif inp == 7:
            print("Anulează o programare. ")
            id = int(input("Introduceți poziția programării în listă: "))
            programari.pop(id)
            print("Ați anulat o programare!")
        elif inp == 8:
            print("Deconectare.")
            print("Vă mulțumim că ați ales serviciile clinicii noastre! La revedere!")
            break
        else:
            print("Operație invalidă!")
    else:
        print("Selectați opțiunea: ")
        print("1. Pentru a vă crea un cont. ")
        print("2. Pentru a vă conecta.")
        inp = int(input())
        if inp == 1:
            print("Creează-ți un cont.")
            username = str(input("Introduceți numele de utilizator: "))
            password = str(input("Introduceți parola: "))
            users[username] = password
            print("Felicitări! V-ați creat un cont cu succes! ")
        elif inp == 2:
            print("Conectare.")
            username = str(input("Introduceți numele de utilizator: "))
            password = str(input("Introduceți parola: "))
            if username in users and users[username] == password:
                logat = True
                print("Autentificarea dumneavoastră a fost reușită! ")
            else:
                print("Nume de utilizator sau parolă incorectă! ")
        else:
            print("Operație invalidă! ")