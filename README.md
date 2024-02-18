# Projekt: Platforma za dijeljenje ideja

## Zadatak:
Cilj ovog projekta je razviti web aplikaciju koja omogućava korisnicima dijeljenje ideja, kao i njihovo komentiranje s ostalim korisnicima. Aplikacija bi trebala pružiti prostor za kreiranje, pregled, ocjenjivanje (u obliku like-ova) kao i komentiranje ideja, potičući time kreativnost i inovativnost.

## Funkcionalnosti aplikacije:
### Korisnički profili:
Jedna od funkcionalnosti aplikacije je omogućiti korisnicima registraciju i stvaranje profila. Za samu registraciju korisnici su obavezni unesti: korisničko ime, ime, prezime, e-mail i lozinku, a prijaviti se mogu pomoću korisničkog imena i lozinke. Nakon prijave, korisnici dodatno mogu uređivati vlasititi profil dodavajući detalje poput: biografije, slike profila te linkova na njihovu web stranicu, Facebook, Instagram i GitHub ukoliko imaju nešto od navedenog. Sve dodatne stavke biti će prikazane na stranici njihovog profila.

### Ideje:
Ideje su glavni dio ove aplikacije, a zamišljeno je na način da korisnici mogu pisati objave poput foruma, u kojima zapravo predstavljaju svoje ideje. Nakon što je korisnik prijavljen, nudi mu se opcija dodavanja objave (ideje) u kojoj trebaju definirati naslov, tag, odabrati kategoriju kojoj ideja pripada (dodatno mogu stvoriti novu kategoriju, ukoliko ona ne postoji od ranije) te dodati tekst i po želji sliku kako bi bolje prezentirali vlastitu ideju. Navedenim idejama se automatski dodjeljuju atributi kao što su datum stvaranja (datum tog dana) i autor (prijavljeni korisnik koji piše objavu). Naravno, autor ideje ima mogućnost uređivanja objave, kao i opciju da ju obriše.

### Ocjene:
Svaki prijavljeni korisnik može na objavu reagirati pomoću like gumba, te mu se prikazuje koliki je broj korisnika koji su već ranije like-ali objavu.

### Komentari:
Ispod svake objave, prijavljenim korisnicima se nudi opcija pisanja komentara koji je povezan sa autorom i objavom za koju se pisao komentar. Također, svaki autor komentara može uređivati svoj komentar ili ga prema potrebi ukloniti. S druge strane, neprijavljeni korisnici mogu čitati komentare, no nisu ih u mogućnosti pisati dok se ne prijave u aplikaciju.

### Pregledavanje i pretraživanje:
Korisnicima se na početnoj stranici prikazuju sve ideje (objave) koje postoje na ovoj platformi, a po potrebi mogu filtrirati objave na onu kategoriju koja ih zanima, što mogu jednostavno napraviti klikom na "Category" u navigaciji te odabirom željene kategorije.


### Responzivni dizajn:
Aplikacija je prilagođena za mobilne uređaje kako bi omogućila pristup korisnicima sa svih vrsta pametnih uređaja.

## Tehnički zahtjevi:
Aplikacija je razvijena koristeći Django i Python web okvir.
Baza podataka je konfigurirana prema potrebama aplikacije.
Za izradu korisničkog sučelja koriste se HTML, CSS i JavaScript.
Implementirani su sigurnosni mehanizmi, uključujući autentikaciju i autorizaciju.

## Student:
Ovaj projekt se izvodi samostalno od strane studenta:
#### Ime i Prezime: Daniel Duda
#### ID broj: 0318008016 
#### Email: daniel.duda@uniri.hr
