# Clinică Medicală – Sistem de Management al Programărilor

Acest proiect reprezintă un sistem simplu de management al programărilor pentru o clinică medicală, implementat în Python. Aplicația permite utilizatorilor să-și creeze conturi, să se autentifice, să facă programări, să le vizualizeze, să le modifice, să le filtreze și să calculeze costul analizelor.

---

## Funcționalități Detaliate

Sistemul oferă un set de funcționalități pentru gestionarea completă a programărilor medicale:

- Autentificare utilizator:

Creare cont nou: Permite utilizatorilor să-și înregistreze un nume de utilizator și o parolă, stocate temporar în memoria aplicației (dicționarul users).

Conectare: Verifică numele de utilizator și parola introduse față de cele înregistrate. O autentificare reușită oferă acces la meniul principal al aplicației.

- Management Programări:

Adăugare programare: Solicită utilizatorului să introducă detalii complete pentru o nouă programare: numele pacientului, numele medicului, data (format ZZ/LL), numele analizei, durata analizei (în minute), ora programării (HH:MM) și prețul analizei (în RON). Aceste date sunt stocate ca o instanță a clasei programare în lista globală programari.

Afișare programări: Listează toate programările existente în sistem, prezentând detaliile fiecăreia într-un format lizibil: "Pacientul [nume_pacient] are o programare la doctorul [nume_doctor] în data de [data]. Numele analizei este [nume_analiza], având durata de [durata] minute de la ora [ora] și prețul de [preț] RON."

Modificare detalii programare: Permite actualizarea unei programări existente. Utilizatorul specifică poziția (indexul) programării în listă, după care i se solicită să introducă noile detalii pentru fiecare câmp (nume pacient, nume doctor, dată, nume analiză, durată, oră, preț).

Anulare programare: Elimină o programare din listă, specificată de utilizator prin poziția (indexul) acesteia.

- Filtrare Programări:

După numele medicului: Utilizatorul introduce numele unui medic, iar sistemul afișează toate programările asociate acelui medic.

După numele pacientului: Utilizatorul introduce numele unui pacient, iar sistemul afișează toate programările asociate acelui pacient.

- Calcul costuri:

Calcularea sumei totale de plată: Permite utilizatorului să introducă numele unui pacient, iar aplicația iterează prin programările acestuia, acumulând și afișând suma totală a prețurilor analizelor.

---

## Structura fișierelor

main.py – Fișierul principal care conține întreaga logică a aplicației, incluzând definiția clasei programare, gestionarea utilizatorilor și a programărilor, precum și bucla principală a programului ce gestionează interacțiunea cu utilizatorul.

---

## Cerințe & Rulare Locală

1. Asigură-te că ai instalat Python pe sistemul tău.
2. Copiază codul într-un fișier numit main.py.
3. Deschide un terminal sau o linie de comandă.
4. Navighează la directorul unde ai salvat main.py.
5. Rulează aplicația folosind comanda: python main.py.

---

## Scenariul de Lucru al Aplicației

Aplicația rulează într-un mediu de consolă și ghidează utilizatorul prin intermediul unor meniuri interactive.

- Inițializarea Sistemului și Autentificarea
La pornirea aplicației (main.py), utilizatorul este întâmpinat cu mesajul "Bine ați venit la clinica noastră medicală!". Sistemul prezintă două opțiuni inițiale:

1. Creare cont: Selectând 1, utilizatorilor noi li se permite să-și înregistreze un nume de utilizator și o parolă. Aceste credențiale sunt stocate într-un dicționar (users) în memoria aplicației. Mesajul "Felicitări! V-ați creat un cont cu succes!" confirmă crearea contului.
2. Conectare: Selectând 2, utilizatorii existenți pot încerca să se autentifice. Sistemul solicită numele de utilizator și parola. Dacă credențialele sunt valide, variabila logat devine True, iar utilizatorul este salutat cu "Autentificarea dumneavoastră a fost reușită!" și are acces la meniul principal. În caz contrar, va primi mesajul "Nume de utilizator sau parolă incorectă!".

- Meniul Principal (După Autentificare)
Odată autentificat, utilizatorul are acces la meniul principal al sistemului de management al programărilor, care include următoarele opțiuni:

1. Fă o programare la clinica noastră.

Utilizatorul este ghidat să introducă secvențial: numele pacientului, numele medicului, data analizei (ZZ/LL), numele analizei, durata (minute), ora (HH:MM) și prețul (RON).

După introducerea tuturor datelor, programarea este adăugată, iar sistemul afișează "Ați adăugat o nouă programare!".

2. Pentru a afișa programările.

Aplicația listează toate programările înregistrate, prezentând detaliile complete ale fiecăreia (pacient, doctor, dată, analiză, durată, oră, preț).

3. Pentru a modifica datele unei programări.

Utilizatorul introduce poziția numerică (indexul) programării în listă.

Aplicația solicită apoi introducerea noilor valori pentru toate câmpurile programării respective.

Mesajul "Ați modificat detaliile programării!" confirmă actualizarea.

4. Pentru a filtra programările în funcție de numele medicului.

Utilizatorul introduce numele medicului căutat.

Sistemul afișează toate programările unde numele medicului corespunde căutării.

5. Pentru a filtra programările în funcție de numele pacientului.

Utilizatorul introduce numele pacientului căutat.

Sistemul afișează toate detaliile programărilor unde numele pacientului corespunde căutării.

6. Pentru a calcula suma de plată a mai multor analize ale unui pacient.

Utilizatorul introduce numele pacientului.

Aplicația parcurge programările, însumează prețurile analizelor asociate pacientului și afișează totalul.

7. Pentru a anula o programare.

Utilizatorul introduce poziția (indexul) programării pe care dorește să o anuleze.

Programarea este eliminată din lista programari, iar operațiunea este confirmată cu "Ați anulat o programare!".

8. Pentru a vă deconecta.

Această opțiune încheie sesiunea curentă, setează logat = False și afișează un mesaj de rămas bun: "Vă mulțumim că ați ales serviciile clinicii noastre! La revedere!". Aplicația se închide.

- Comportament în Caz de Intrare Invalidă
Dacă utilizatorul introduce o opțiune numerică invalidă (care nu se află în lista de opțiuni disponibile) în oricare meniu, sistemul afișează mesajul "Operație invalidă!" și meniul este reafișat, permițând utilizatorului să încerce din nou.

---

## Realizat de

Proiect realizat de bogdanch7
An universitar 2024–2025

---

## Licență

Acest proiect este creat pentru uz educațional.
