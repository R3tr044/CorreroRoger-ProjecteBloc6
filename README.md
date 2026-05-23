# Projecte Bloc 6 - Desenvolupament Web amb Django

---

## 1. Introducció

### Descripció breu del projecte i objectius principals
Aquest projecte consisteix en el desenvolupament d'una aplicació web completa de tipus **Blog** utilitzant el framework **Django**. 

L'objectiu principal és posar en pràctica i consolidar els coneixements de programació web del Bloc 6. Específicament, s'ha dissenyat una estructura de dades relacional per gestionar publicacions (posts), autors i etiquetes (tags). El projecte busca demostrar el domini en la creació de models, la configuració de rutes dinæmiques (URLs), la implementació de vistes per renderitzar plantilles HTML, i l'ús del panell de gestió natiu de Django per a l'administració de continguts. Finalment, s'inclou l'objectiu d'automatitzar la documentació del codi font mitjançant fluxos de treball d'integració contínua (CI/CD).

---

## 2. Instal·lació ràpida

### Com clonar el repositori
Per obtenir una còpia local del projecte en el teu ordinador, obre la teva terminal i executa el següent comandament per clonar el repositori des de GitHub i entrar a la carpeta del projecte:

    git clone https://github.com/R3tr044/CorreroRoger-ProjecteBloc6.git
    cd CorreroRoger-ProjecteBloc6

### Instal·lar dependències
Per poder instal·lar les dependències i llibreries del projecte, primer es recomana crear i activar un entorn virtual de Python per aïllar els paquets. Executa els següents comandaments a la terminal:

    python -m venv venv
    venv\Scripts\activate

Una vegada activat l'entorn virtual, instal·la de cop tots els paquets, el framework Django i les llibreries del sistema necessàries que estan especificades al fitxer de requeriments mitjançant el següent comandament:

    python -m pip install --upgrade pip
    pip install -r requirements.txt

### Executar migracions
Abans d'iniciar l'aplicació per primera vegada, és obligatori preparar i generar l'estructura de la base de dades local. Executa el següent comandament de gestió de Django per aplicar les migracions i crear totes les taules corresponents als models del blog:

    python manage.py migrate

---

## 3. Execució del projecte

### Com executar el servidor localment
Una vegada completada tota la instal·lació ràpida de les dependències i configurada la base de dades, pots aixecar el servidor de desenvolupament local natiu de Django executant el següent comandament a la teva terminal:

    python manage.py runserver

### URL per accedir-hi
Quan el servidor local s'estigui executant correctament i es mostri actiu a la terminal, podràs accedir, interactuar i testejar l'aplicació obrint el teu navegador web preferit i introduint les següents adreces URL:

* 🌐 **URL d'accés a l'aplicació principal (Interfície del Blog):** http://127.0.0.1:8000/
* ⚙️ **URL d'accés al Panell d'Administració (Django Admin):** http://127.0.0.1:8000/admin/

---

## 4. Documentació dels fitxers .py (Pydoc)

### Generació de la documentació i GitHub Actions
La documentació tècnica de tots els fitxers font del projecte ha estat generada automàticament utilitzant l'eina de documentació de Python. S'ha configurat una GitHub Action automàtica que compila els fitxers HTML resultants en cada actualització de codi.

### Enllaç per a visualitzar la documentació correctament
Per poder navegar i revisar tota la documentació estructurada des de qualsevol navegador web, s'ha publicat mitjançant GitHub Pages al següent enllaç:

* 📄 **Visualitzar la documentació en línia:** [Documentació del Projecte (GitHub Pages)](https://r3tr044.github.io/CorreroRoger-ProjecteBloc6/)