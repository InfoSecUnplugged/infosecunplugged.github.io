Siamo tornati con una nuova puntata di Info Sec. Unplugged. Questa volta siamo in trasferta, a Bolzano, pronti per partecipare all’evento NTS di Monaco.

Riprendiamo da dove ci eravamo lasciati l’ultima volta: avevamo parlato di misure di sicurezza, ma avevamo volutamente lasciato in sospeso il tema del NAC. Io volevo fare qualche esperimento prima di tornarci sopra — e li ho fatti. Ora possiamo raccontarli.

Abbiamo voluto verificare quanto fosse possibile “bypassare” un sistema NAC, ovvero aggirare i controlli di autenticazione di rete. L’esperimento parte da un’idea semplice: creare un dispositivo completamente trasparente che possa riutilizzare il canale di autenticazione 802.1X di un client già connesso. Così il dispositivo diventa invisibile: passa attraverso la rete senza essere rilevato, a meno che non si disponga di strumenti comportamentali molto sofisticati.

Le implicazioni sono importanti. Ci dicono molto sul reale livello di sicurezza offerto da certe soluzioni NAC, che spesso vengono considerate risolutive, quando in realtà riducono solo la probabilità di un attacco.

Siamo partiti con un Raspberry Pi, due porte di rete, un power bank e molta pazienza. Il trucco consiste nel configurare le due interfacce in modalità “transparent”, per far passare i frame senza filtrarli. Abbiamo riutilizzato una patch al kernel di Linux che avevamo sviluppato tempo fa per UNETLAB — un vecchio progetto da cui poi è derivato EVE-NG. Quella patch serve proprio a far transitare frame di livello 2 che normalmente verrebbero bloccati, come quelli 802.1X.

Con questa base abbiamo ricreato un piccolo bridge trasparente. L’autenticazione più comune che incontriamo è quella per porta: quando un client autentica la propria porta, tutto ciò che è “a valle” può comunicare liberamente. È uno schema ancora diffuso, anche se datato. L’altro metodo, l’autenticazione per MAC address, è più rigido e difficile da aggirare, ma anche in questo caso, con qualche accorgimento, è possibile.

Nel nostro test abbiamo voluto spingerci oltre: simulare un attacco reale, mettendoci in mezzo al traffico tra un dispositivo e la rete, senza che nessuno se ne accorgesse. L’obiettivo era impersonare il dispositivo legittimo, ma senza scollegarlo fisicamente. Non sempre infatti è possibile — pensiamo a un server o a un dispositivo critico. Così abbiamo creato un software in grado di lavorare in kernel space, copiando e inoltrando i frame in tempo reale.

Abbiamo battezzato il progetto “Predator P”, ma non lo abbiamo reso pubblico per motivi evidenti: non vogliamo diffondere strumenti che possano essere usati per scopi illegali. In pratica, il dispositivo si inserisce in rete, impara passivamente gli indirizzi IP e MAC, e poi replica il comportamento del client, riservandosi un piccolo intervallo di porte per comunicazioni proprie. È invisibile: lo switch non lo vede, perché non crea un nuovo canale di autenticazione.

Il dispositivo diventa così una sorta di “captatore”, capace di intercettare traffico e impersonare un client già autenticato. È un test di laboratorio, certo, ma mostra chiaramente quanto certe soluzioni NAC siano più fragili di quanto si pensi.

Questo ci porta al punto centrale: troppe volte vediamo implementare soluzioni NAC come se fossero una bacchetta magica. In realtà, si tratta di protocolli nati molti anni fa, con un’idea di sicurezza oggi superata. L’autenticazione per MAC address, ad esempio, si basa su informazioni facilmente falsificabili. Anche i certificati — che restano l’opzione più solida — possono essere rubati e riutilizzati.

Inoltre, l’applicazione pratica di un NAC è complessa e costosa. Dispositivi in standby, stampanti, apparecchi industriali: sono tutti elementi che spesso non supportano le modalità di autenticazione più sicure. Il risultato è che si creano “zone grigie” nella rete, dove il controllo si allenta.

La lezione, per noi, è che serve sempre una valutazione tecnica consapevole. Non basta fidarsi del datasheet di un vendor: bisogna capire fino in fondo cosa fa una tecnologia, e soprattutto cosa non può fare.

Disegnare un’infrastruttura sicura significa accettare che alcune soluzioni vadano bene solo in certi contesti. Ad esempio, un approccio alternativo potrebbe essere quello di trattare la rete “campus” come una zona ad alto rischio, una sorta di DMZ interna, e proteggere l’accesso ai servizi con VPN o proxy. Oppure passare a modelli “wifi only”, in cui il canale è crittografato nativamente.

Un altro strumento sottovalutato è la Private VLAN, che consente di isolare i dispositivi all’interno della stessa rete, impedendo comunicazioni dirette tra client. È un modo semplice per ridurre il rischio di movimenti laterali, e in contesti come hotel, aeroporti o ambienti industriali potrebbe evitare molti problemi.

Naturalmente ogni soluzione va calibrata: nel VoIP, per esempio, la comunicazione diretta tra telefoni può richiedere eccezioni. Ma il principio resta lo stesso: isolare, segmentare, ridurre la superficie d’attacco.

Alla fine tutto si riduce a una questione di consapevolezza. Le aziende spesso sovrastimano le tecnologie che usano e le sottovalutano al tempo stesso: pensano che risolvano ogni problema, ma poi non sfruttano nemmeno il 10% delle loro potenzialità.

Serve un cambio di mentalità. La sicurezza non si compra in una scatola: si progetta, si configura e si mantiene. Significa conoscere le proprie reti, capire dove ci sono limiti tecnici o vincoli operativi, e trovare soluzioni realistiche.

E sì, a volte significa anche convivere con apparati vecchi di quindici anni, “croccanti” come diciamo noi, ma rinforzati con un po’ di hardening e buone pratiche. L’importante è sapere cosa si sta proteggendo e con quali strumenti.

Ci lasciamo con la promessa di riprendere il discorso nella prossima puntata, per approfondire i casi reali di attacco in reti con NAC — e come spesso, a causa di errori di configurazione o incomprensioni, i controlli saltano completamente.

Alla prossima.
