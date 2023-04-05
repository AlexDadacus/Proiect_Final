# Proiect_Final

# Structură proiect și funcționalități acoperite:

Proiectul este împărțit în 3 features. Primul feature este pentru pagina de home a site-ului și testează paginile care se deschid din aceasta. În cadrul acestui feature 
avem 5 scenarii. Testarea se face prin parcurgerea scenariilor și verificarea cu un assert pentru link-ul care se așteaptă a fi deschis din pagina de home.
Al doilea feature este pentru pagina de login, cu 2 scenarii de login:
logarea cu credențiale valide
logarea cu credențiale invalide:
	- logarea cu parolă invalidă(username existent)
	- logarea cu username invalid(parolă validă)
	- logarea cu username și parolă invalide
	- logarea cu câmpuri blank
Al treilea feature vizează pagina după logarea cu succes cu două scenarii: unul care verifică mesajul apărut după logarea cu succes, iar al doilea verifică funcționalitatea
butonului de logout.

# Înainte de a rula proiectul trebuie instroduse următoarele comenzi în terminal Pycharm:
● pip install selenium (sau pip install -U selenium - pt update la zi)
● pip install behave (o librărie bdd care va interpreta și rula testele scrise în gherkin)
● pip install behave-html-formatter (ne ajută să generăm rapoarte bdd)
● pip install webdriver-manager

# Rulare proiect și raport:

Pentru a rula proiectul și a genera un raport se folosește următoarea comandă în terminal: behave -f html –o raport.html.

# Clonare și actualizare proiect:

Pentru a clona proiectul, după instalarea și deschiderea git-ului se folosește comanda “git clone” urmată de link-ul în care se regăsește proiectul. 
Și dacă se aduc modificări la proiect, acesta se poate actualiza printr-un commit nou folosind comenzile “git add .”,  “git commit –m ‘final commit‘ ” și  “git push”.
