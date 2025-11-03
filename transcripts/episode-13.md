Bentornati a Info Sec. Unplugged – Extended. In questa versione del podcast vogliamo raccontare e commentare insieme alcuni incidenti di sicurezza realmente accaduti – episodi che sia noi che altri colleghi abbiamo vissuto in prima persona. Gli esempi sono romanzati quel tanto che basta a non rendere riconoscibili i protagonisti, ma il contenuto resta autentico.

Cominciamo con un caso molto comune: una campagna di phishing che, da inizio anno, ha colpito in modo massiccio organizzazioni in tutto il mondo. Tutto parte dalla compromissione della casella e-mail di un cliente: l’attaccante utilizza quell’indirizzo come testa di ponte per inviare e-mail di phishing a tutta la rubrica dell’utente compromesso. I messaggi invitano a cliccare su un collegamento WeTransfer, OneDrive o Dropbox, che porta al download di un file malevolo. Il malware si installa sul dispositivo della vittima e da lì può diffondersi.

Abbiamo visto questa campagna più volte. La cosa interessante è stata la scala: migliaia di caselle colpite. Non vogliamo entrare nel tecnicismo — gli analisti sanno già come affrontare simili scenari — ma spiegare a chi gestisce la sicurezza “dall’alto” come reagiamo e quali riflessioni emergono.

La prima è semplice: quando una casella di posta viene compromessa, possiamo dare per certo che tutto il suo contenuto e la sua rubrica siano stati esfiltrati. Non si tratta solo di messaggi cancellati o letti: quei dati sono stati rubati. E questo, ai sensi del GDPR, è un data breach vero e proprio, con conseguenze diverse a seconda del ruolo dell’utente colpito. Se l’account appartiene a un commerciale, l’attaccante ottiene clienti, proposte e fatture; se appartiene alle risorse umane, rischiano di uscire dati sensibili come buste paga e informazioni sanitarie.

Poi c’è un secondo punto: i dati rubati servono all’attaccante per “studiare” l’azienda e preparare attacchi successivi più mirati. In questo caso specifico, la campagna era grossolana – un’enorme “pesca a strascico” – ma proprio il rumore che ha generato ha aiutato a identificarla.

Nel nostro caso, l’attacco è stato individuato perché l’azienda aveva da poco concluso corsi di awareness, e il personale era più attento del solito. Inoltre, il team di sicurezza aveva già diffuso un avviso interno su campagne di phishing in corso. Un mix di intelligence e formazione ha fatto la differenza.

L’individuazione è avvenuta anche grazie alla natura del messaggio: una richiesta di condivisione WeTransfer, insolita per quella tipologia di cliente. E qui entra in gioco la parte tecnica: molti sistemi antispam controllano solo la posta in ingresso, ma raramente quella in uscita. È un errore comune. Se un account compromesso inizia a inviare centinaia di e-mail anomale, questo spesso non viene rilevato. Un buon controllo comportamentale aiuterebbe: se un utente normalmente invia 20 mail al giorno e improvvisamente ne spedisce 500, è un chiaro segnale d’allarme.

Allo stesso modo, i filtri dovrebbero verificare non solo i link diretti, ma anche eventuali redirect, spesso usati per eludere i controlli. Tutto, ovviamente, dipende da quanto bene lo strumento è configurato e monitorato: anche una soluzione eccellente, se impostata male, può risultare inutile.

Una volta scoperto l’attacco, la domanda diventa: chi ha cliccato sul file e l’ha installato?
In teoria, un buon EDR permetterebbe di verificare in rete se quel file è presente su altri computer, confrontando l’hash del malware. In pratica, la cosa è più complessa. L’analista deve identificare chi ha scaricato l’allegato, capire se l’ha eseguito e, se necessario, eliminarlo.

Un altro tema delicato è la comunicazione con il cliente. Spiegare che una casella di posta – magari di un dirigente – è stata compromessa non è mai facile. Spesso chi subisce l’attacco si sente accusato, come se avesse sbagliato personalmente. In realtà, può succedere a chiunque: a volte basta una password debole o un’email particolarmente ben costruita. Ma il rischio è che, in azienda, quella persona venga “etichettata” come colpevole.

Abbiamo visto casi in cui un dipendente, dopo un incidente simile, ha vissuto settimane difficili o addirittura è stato licenziato. È quindi fondamentale che le risorse umane gestiscano queste situazioni con tatto, trattandole come incidenti di processo, non come colpe individuali. È un tema di cultura aziendale: formare, non punire.

E qui torniamo alla security awareness. Molte aziende fanno un corso annuale “una tantum”, giusto per adempiere a un requisito. Ma non basta. La formazione deve essere continua, costruita su esempi reali e integrata nella vita quotidiana. Deve insegnare non solo a riconoscere un’e-mail sospetta, ma anche a capire lo scopo dell’attaccante e a reagire con calma.

Fondamentale è anche creare una cultura di ascolto e supporto: se un dipendente nota qualcosa di strano, deve sapere a chi segnalarlo e sentirsi libero di farlo. Spesso, invece, manca perfino una procedura chiara per la segnalazione. Ci è capitato di vedere scene paradossali, come colleghi che urlano “non aprite quella mail!” in ufficio. E può anche funzionare, ma non è certo un processo strutturato.

Un altro problema ricorrente è la mancanza di procedure operative. Gli utenti devono sapere come scambiare file in modo sicuro: se WeTransfer o Dropbox non sono strumenti approvati, vanno bloccati; se servono davvero, vanno acquistati e gestiti in modo ufficiale. Quando le regole non coprono la realtà del lavoro, le persone trovano soluzioni “creative” — e spesso rischiose.

Un caso emblematico: un team marketing usava WeTransfer per scambiarsi file troppo grandi per la posta interna. Non era autorizzato, ma funzionava. L’attaccante l’ha sfruttato proprio per colpire quell’azienda.

Questa storia, tutto sommato semplice, apre in realtà il vaso di Pandora del rapporto tra persone e sicurezza informatica. È un tema complesso, che merita di essere approfondito in futuro. Per ora ci fermiamo qui, ma la discussione continua: il prossimo episodio sarà l’occasione per esplorare nuovi incidenti e nuove lezioni.
