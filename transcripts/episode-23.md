Siamo tornati con Info Sec. Unplugged.

Oggi vogliamo affrontare un argomento vastissimo: la Threat Intelligence. È un tema che apre un capitolo enorme, ma per poterlo affrontare, dobbiamo prima gettare le basi, ripartendo dal mondo dell’EDR e dell’XDR, e da come oggi raccogliamo e analizziamo i dati di sicurezza.

Ricordiamo che ne avevamo già parlato circa un anno fa, in una delle prime puntate, quando ci eravamo concentrati sull’ottimizzazione e il tuning degli EDR. All’epoca avevamo accennato alle funzionalità principali di queste piattaforme, ma non avevamo approfondito davvero come funzionano nel profondo. Oggi possiamo dire che un buon EDR non si limita più all’analisi statica: sfrutta la telemetria dinamica, osserva i comportamenti e arricchisce i dati per individuare minacce reali.

Un anno fa avevamo anche ipotizzato che gli XDR avrebbero “inghiottito” i SIEM, diventando piattaforme in grado di raccogliere eventi da fonti eterogenee — non solo dagli endpoint, ma anche da firewall, Active Directory e altri sistemi. In effetti, il mercato si è mosso proprio in quella direzione: oggi le piattaforme EDR di fascia alta integrano spesso una componente SIEM interna, offrendo tutto in un’unica console. È comodo, ma il risultato non è un vero superamento del SIEM: piuttosto una collaborazione tra i due mondi.

Questo percorso è diventato evidente con le grandi acquisizioni: Palo Alto che compra QRadar, Cisco che compra Splunk, CrowdStrike che sviluppa un proprio SIEM. Tutto converge verso l’integrazione. Ma se da un lato guadagniamo efficienza, dall’altro perdiamo la semplicità originaria dell’EDR.

Un aspetto interessante riguarda la retention dei dati: l’EDR conserva la telemetria per periodi brevi, mentre il SIEM può mantenerla e indicizzarla per mesi o anni, rendendo possibili analisi retroattive e attività di threat hunting. Ecco perché, alla fine, i due strumenti continuano a coesistere.

Nel frattempo, gli approcci si sono diversificati. L’XDR tende a semplificare l’esperienza d’uso per gli analisti interni, mentre le piattaforme con SIEM integrato richiedono competenze più avanzate. Inoltre, molti vendor puntano sull’automazione e sull’intelligenza artificiale per gestire gli eventi in autonomia. Ma queste soluzioni non sono “magia pura”: vanno configurate, presidiate e migliorate continuamente.

Abbiamo anche notato un forte spostamento verso il cloud: i SIEM moderni sono sempre più spesso offerti in modalità SaaS. È un’evoluzione naturale — un po’ come accadde con Exchange — perché mantenere e gestire un’infrastruttura così complessa on-premise è sempre più difficile.

Un tema spesso frainteso riguarda la distinzione tra log management e SIEM. Gestire i log per la compliance o per il troubleshooting è un conto, fare correlazione e detection è un altro. Le due attività hanno obiettivi, retention e costi diversi. Confonderle porta facilmente a errori di configurazione e a spese sproporzionate.

Nel progettare un SOC, un’altra grande sfida è stimare i volumi: quanti log, quanti incidenti, quanta ingestion di dati? Domande a cui le aziende spesso non sanno rispondere, ma fondamentali per dimensionare licenze e infrastrutture.

Un punto chiave è che nessuna di queste piattaforme “fa tutto da sola”. L’EDR e il SIEM raccolgono una quantità enorme di dati, ma non trasformano automaticamente log grezzi in threat intelligenti. Servono regole, tuning e conoscenza del contesto. Ad esempio, un firewall deve essere configurato per registrare gli eventi utili alla sicurezza — non tutto, ma ciò che ha valore per la detection.

Lo stesso vale per gli EDR: un evento isolato, come una chiamata HTTP, non significa nulla se non è correlato a un indicator of compromise (IOC). Solo allora il dato assume significato. E qui entra in gioco la Threat Intelligence: serve per arricchire ciò che osserviamo con informazioni esterne — reputazione di domini, URL malevoli, indicatori aggiornati — che i nostri sistemi da soli non possono conoscere.

Abbiamo anche discusso della contestualizzazione: ogni azienda ha dinamiche proprie. Bloccare PowerShell o Python può avere senso in un contesto produttivo, ma non in un reparto IT. L’efficacia delle regole dipende sempre da dove e come vengono applicate.

Oggi la complessità delle infrastrutture è enorme — tra cloud, Active Directory, Entra ID, NAC, firewall, endpoint, gateway email — e richiede competenze specialistiche che poche aziende hanno. Chi non può gestirle internamente deve affidarsi a provider esterni, ma dovrebbe comunque conservare la visione d’insieme per sapere cosa sta acquistando e come misurarlo.

Siamo quindi arrivati al punto in cui abbiamo tutto: EDR, XDR, SIEM, log, telemetrie, regole, automazione. Eppure, la vera sfida è capire cosa guardare e come correlare. È qui che entra in gioco la Threat Intelligence: collegare i dati interni con informazioni esterne, aggiornate e contestuali, per dare senso al rumore.

Ed è proprio da qui che ripartiremo nella prossima puntata, per capire come si costruisce e si integra un sistema di Threat Intelligence in un SOC moderno.
