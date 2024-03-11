# Wat gaan we doen?

Bezig met: 

- Hoe werkt het examen
- Deze week dingen doen
- Door offSec modules heen werken
- zoveel mogelijk flags halen
  NB: alle flags halen in de omgeving is gratis 10% op je examen

Vragen stellen is aangeraden
TIP: Niet te lang wachten met examen doen. Als je er bijna  bent, of je hebt alles comfortabel doorgewerkt: vooral doen.
De meeste mensen halen het niet de eerste keer en we hebben twee examenpogingen. 
(Verval niet in een: "Ik moet alleen nog *dit* doen en dan ben ik er klaar voor!")

OSCP is de 'entry level moeilijke training'
Het is wel echt status, maar ook het begin van een traject.

Buffer overflows zijn uit pen-200 gehaald? Nu alleen in pen-100?
Hierna: pen-300, web-300

Het examen is gebouwd om jou te laten begrijpen hoe iets werkt. "Niet iets automatisch doen."
Dus geen metasploit en dat soort tools. (Wel payloads e.d.)
Punt is geen automatische vulnerabilities vinden, maar hulp mag wel. - Dus nmap enzo mag wel.
(EternalBlue mag niet)

Er zijn slides, maar er zit niets in de slides wat niet in de trainings zit.

## Vaste oefeningen
Oefenen met:
Op de juiste manier meteen notities maken. 
Meteen screenshots maken bij alles wat je doet. 
Dus: enumerate, enumerate, enumerate en zodra er iets gedaan wordt een notitie en een screenshot maken.

Wat is nodig in een screenshot:

- IP adres
- De exploit
- ??

Don Quichote methode - gewoon gaan. 

Hou je lijstjes bij.

## Vaste valkuilen

Niet genoeg scanning/enumaration
Voorbeeld: als je een poort 80 hebt gevonden en je gaat helemaal door op die poort, maar komt niet verder... kijk nog eens verder. Misschien staat er een poort 3000 nog open..

Doel van de examinator is niet jou zo lang mogelijk bezig te laten zijn, maar om te laten zien dat je snapt hoe het werkt. 
Dus: eerder dat in een e-mail staat wat een wachtwoord van zip bestand is of hoe wachtwoorden zijn opgemaakt, wat handiger werkt dan gewoon een 100GB password file.

## Wat is de scoping?

We gaan door alle modules heen werken, hophop! 

## Maandag

- 6 Information Gathering
- 7 Vulnerability Scanning
- 8 Introduction to Web Application Attacs (als we daar komen)

## Dinsdag

## Woensdag

## Donderdag

- 18 Port Redirection and SSH Tunneling

## Vrijdag

- 

# Op het examen

Laat je niet tegenhouden door dingen.
Bijvoorbeeld: lekker threads en scans toevoegen. Je wordt toch niet tegengehouden.

Examen is gemaakt om je te laten slagen. Dus soms is het simpeler dan je denkt. (Wachtwoorden in files e.d.)
Alle devices zijn hackbaar. 

Alle doosjes zijn los. Dus je hoeft niet heen-en-terug te hoppen van machine naar machine.

## Nmap
(Altijd sudo en -Pn in je examen, dan weet je dat 'ie doet wat je wil dat 'ie doet.)
NMap: sla je outputs op. Daar is de -o optie voor. (-oG is om het ook greppable te maken)
Maak eerst even een mapje met nmap `mkdir nmap`
`nmap -v -sn 10.11.1.1-254 -oG ping-sweep.txt`
-v is verbose
-sn is subnet scan (snelle scan) > sn is zonder porscan
-oG is output greppable 
-oA is is ook Greppable en 'de anderen'
ip is te scannen ip 
txt file is je output file
lekker al je nmap files outputten in je nmap folder
Als je bezig gaat met python en scripting: -oA geeft ook een xml output. Is makkelijker analyseerbaar. -oG is voor de terminalfreaks
-A is meest voorkomende services
-sT is TCP connect scans
-sS half open scan
-sU UDP scans
-sN TCP Null scans
-sF TCP FIN scans
-sX Xmax scans
--open (dan laat ie alleen de open dingen zien)//beter leesbaar
-p#### (# == portnummer) specifieke port scannen
-Pn eerste stappen overslaan, scan 'gewoon' elke host provided
NB: -Pn ook nodig bij geforceerde poorten, want Pn slaat over "bestaat deze machine"

sudo is nodig voor pingen -- normaal alleen handshakes, sudo ook ping -- nodig voor o.a. windows machines

root: synscan
normaal: handshake 
Omdat een gewone gebruiker niet rechten heeft tot raw sockets, maar alleen tcp stack.

Op 't examen lekker sudo'en  

Als je al op 't juiste segment zit krijg je de windows machines wel, want de machines zitten in de arp

commando: arp -a 

SNMP niet overslaan

/usr/share/nmap//cripts
ls *.db
script.db

sudo nmap --script vuln $IP
== alle scripts draaien die vulns pakken 
sudo nmap --script "vuln and safe" -p 21,22,8080,10000 $IP -Pn -vv
vuln en safe scripts draaien op vier poorten op ip adres 

--script-updatedb (update database...)

# Linux Commands

## Ip things
ip -br add

## Processes
ps -ef | grep *thing*
dus als iemand passwd doet voor password change
zie je met ps -ef | grep pass 
wie er bezig is

r = read
w = write
x = execute
s = sudoers (it's a suid bit)

`echo $$`
== huidige Processes

kill -9 $$
Kill huidige proces en remove history

## Ping 

standaard ttl bij windows == 128
standaard ttl bij andere dingen == 64

## arp

`arp -a` 
om de arp map te zien 

Werkt pas in het netwerk, dus vanaf de router ofzo.
arp laat je hele eigen broadcast domein zien 
arp doet mac adres vertaling

dus bij level3 communicatie wordt er eerst een arp request gedaan

# Information Gathering

Twee vormen, passief en actief.
Lekker over discussieren, de ene zegt: passief betekent geen interactie met machine. De andere vind het: passief is als je als normale gebruiker bezig bent.

WHOIS: passief. Staat heel veel informatie in. Het is - op basis van IP adres - een telefoonboek. Staat alle info in.
Argumenten: vroeger heel veel informatie delen met whois diensten, vanwege een tekort aan ip adressen.
Waarom interessant? Fysieke locatie, nameservers, achtergrondinfo. Dus handig voor social engineering, maar ook je technische netwerkkant. Het is volledig enumeration.

## DNS

A: ip naar naam
NS: name servers (azure e.d.)
MX: mail server


nslookup (in windows)
dns lookup in command line

Computers zijn meer fan van ipv6 dan ipv4, dus een makkelijke mitm is ipv6 gateway zijn.
mtlm relay x (mitm voor mtlm verkeer) - komt later

Bij inrichten ipv6: je bent een stuk veiliger als je geen voorspelbare adressen invult.

DNS MX en NS requests zijn handig, want je ziet gelijk wat iemand 'ongeveer' doet. (Dus bij een MX zie je bijvoorbeeld al een outlook, dan mag je de aanname ook doen dat iemand outlook gebruikt. En mogelijk dus ook word.)

ADFS -- doorlink 'sending you to your organisations inlog page'

dus in office365 kun je door een 'user@domain' te proberen kun je zien of een user valid is.

SecLists == wordlists of standard subdomains
`sudo apt install seclists`

## Portscans
Dev/TCP < bash handmatig werken

Als een poort luistert naar een well known taal moet je ook die taal spreken. (Een UDP poort luistert alleen naar UDP.)
LET OP OP EXAMEN: UDP OOK SCANNEN
Dus: lijstje bijhouden met wat heb ik aan scans en poorten e.d. gevonden. 
Vroeg beginnen met 'welke stappen heb ik gedaan' en 'wat is daaruit gekomen'

Nmap doet standaard de 1000 meest gebruikte poorten.

Altijd gewoon Nmap 'alles' doen bij je examen. Je bent toch niet gelimiteerd in bandbreedte en er is geen detection gaande.

## SMTP Enumeration  

SMTP == simple mail transport protocol
port = standaard 25 

VRFY request 

## SNMP Enumeration

Nazoeken

## LLDP / CDP

LLDP == Link Layer Discovery protocol
CDP == Cisco discovery protocol

Gewoon even wiresharken. 
Elke 30 seconden roept een switch en router: "Hallo ik ben een switch/router, ik ben dit device en ben bereikbaar via zus en zo."
En dan zoeken naar standaard exploits, natuurlijk.

# Vulnerability Scanning 

Lekker snel doorheen, mag toch niet op het examen.

Een automated scanner doet meestal:

1. Host discovery 
2. Port scanning
3. Operating system, service and version detection 
4. Matching the results to a vulnerability database

Tools:
Nessus vulnerability scanner
OpenVAS
