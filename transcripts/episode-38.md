In questa puntata riprendiamo il discorso da dove lo avevamo lasciato nell’episodio precedente, quando avevamo parlato dei limiti dell’URL filtering e del fatto che il modello classico — il firewall che filtra l’accesso a internet — oggi mostra diverse debolezze, sia dal punto di vista tecnologico sia da quello topologico, soprattutto quando entrano in gioco utenti remoti o scenari distribuiti.

Partiamo da un caso concreto che abbiamo osservato di recente. Negli ultimi tempi ci siamo trovati a seguire diverse truffe bancarie, spesso legate al cambio improvviso delle coordinate di pagamento, tipicamente un IBAN che viene modificato per dirottare i soldi verso conti esteri. In uno degli episodi più significativi che abbiamo analizzato, il threat actor non ha iniziato la conversazione da zero: si è inserito nel mezzo.

In pratica ha compromesso uno dei due interlocutori — non il nostro cliente, ma la controparte — e ha aspettato il momento giusto per intervenire. A quel punto ha separato la conversazione in due thread distinti, intrattenendo da una parte lo scambio con il nostro cliente e dall’altra con il cliente del nostro cliente, quello che alla fine doveva effettuare il pagamento. In sostanza ha realizzato una sorta di man in the middle applicato alla posta elettronica.

La truffa, bisogna ammetterlo, era costruita molto bene. Tutta la conversazione risultava coerente: il tono, le risposte, il contesto. L’unico vero segnale d’allarme era il cambio dell’IBAN. Questo, da solo, dovrebbe sempre far scattare una grande luce rossa.

A rendere la situazione ancora più difficile da individuare c’era un dettaglio tecnico importante: il dominio dell’email era cambiato, ma non era affatto sospetto. Era un dominio perfettamente legittimo, con uno storico alle spalle. Probabilmente era stato registrato anni prima da un’azienda con un nome simile, poi abbandonato e infine riutilizzato. Era classificato come dominio “parcheggiato”, una categoria che idealmente andrebbe bloccata a livello di firewall. Ma qui non stavamo parlando di traffico web: era posta elettronica.

Questo ci ha portato a riflettere su una cosa: mentre negli anni abbiamo lavorato molto sulla categorizzazione dei domini e sui controlli lato navigazione web, nel mondo delle email siamo rimasti in parte indietro. Molte aziende utilizzano ancora sistemi antispam tradizionali che, un po’ come gli antivirus classici, mostrano limiti evidenti di fronte ad attacchi più sofisticati.

Il problema è che in conversazioni di questo tipo non ci sono indicatori tecnici evidenti. Non ci sono link sospetti, non ci sono file malevoli. Spesso sono semplicemente persone che parlano tra loro, magari anche con email in semplice testo. Tutto funziona come sempre, fino al momento in cui compare una richiesta di modifica delle coordinate bancarie.

E qui entra in gioco anche il comportamento umano. Quando una conversazione è iniziata mesi prima e procede nello stesso thread, non siamo più portati a verificare ogni volta il dominio del mittente. Il nostro cervello ha già classificato quella conversazione come affidabile. Se poi il dominio è credibile, accorgersi del cambiamento diventa ancora più difficile.

A complicare ulteriormente il quadro si aggiunge anche un tema legale. Di recente è uscita una sentenza della Cassazione relativa proprio a un caso di questo tipo, in cui la responsabilità del danno è stata attribuita alla persona che ha effettuato il bonifico sulle coordinate sbagliate. La motivazione era che, per il ruolo ricoperto nell’amministrazione aziendale, quella persona avrebbe dovuto essere consapevole dei rischi e delle possibili truffe.

In sostanza è stata considerata una colpa grave.

Questo apre una riflessione importante. In alcuni casi la negligenza può effettivamente causare incidenti informatici, soprattutto se esistono regole chiare che vengono violate. Ma quando parliamo di attacchi sociali sofisticati, aspettarsi che ogni impiegato sia in grado di riconoscerli sempre può essere eccessivo.

Certo, nel momento in cui viene richiesto un cambio IBAN una verifica aggiuntiva dovrebbe essere sempre fatta. Ma attribuire automaticamente tutta la responsabilità alla persona che ha eseguito il pagamento rischia di essere una semplificazione troppo drastica, soprattutto se non è chiaro se quell’utente abbia ricevuto una formazione adeguata.

Al di là della questione legale, dal punto di vista difensivo la risposta principale rimane organizzativa. Il primo vero strumento di difesa è una procedura interna chiara: le modifiche alle coordinate bancarie devono seguire un processo definito e documentato, senza eccezioni.

Per esempio, il cambio IBAN potrebbe richiedere sempre l’approvazione di una seconda persona. Oppure potrebbe essere verificato tramite un canale alternativo: una telefonata o un contatto diretto con un referente noto. Alcune aziende vanno ancora oltre e utilizzano portali dedicati ai fornitori: ogni fornitore ha un account protetto da autenticazione forte e gestisce direttamente i propri dati di pagamento all’interno del sistema. In questo modo si elimina quasi completamente il rischio legato alla conversazione email.

Naturalmente si sposta il problema su altri aspetti, come la sicurezza delle credenziali o dell’applicazione stessa, ma almeno si elimina la componente più discrezionale legata all’interpretazione umana delle richieste.

Dal punto di vista tecnologico, invece, le possibilità sono più limitate. I sistemi antispam lavorano principalmente su indicatori tecnici presenti nel messaggio, e raramente riescono a capire il contesto della conversazione.

Una possibile evoluzione potrebbe arrivare dall’analisi semantica dei thread. In teoria, se si analizzasse una conversazione completa con un modello linguistico, si potrebbe identificare quando si sta discutendo di un cambio IBAN e allo stesso tempo rilevare che l’indirizzo email del mittente è cambiato nel mezzo del thread. Un’anomalia del genere potrebbe generare un alert.

Naturalmente questa soluzione apre altre questioni, prima fra tutte quella del trattamento dei dati: significherebbe analizzare automaticamente tutte le conversazioni aziendali.

Un’altra riflessione riguarda il ruolo della posta elettronica nelle aziende. Di fatto oggi la usiamo per qualsiasi cosa: comunicazioni interne, documenti, offerte commerciali, promemoria personali. Diventa una sorta di enorme contenitore di informazioni che si accumulano per anni, spesso senza alcun controllo. Ci sono aziende con archivi di posta elettronica che coprono decenni.

Questo crea non solo problemi di sicurezza, ma anche problemi operativi ed economici. Archivi giganteschi devono essere gestiti, protetti, inclusi nei piani di backup e disaster recovery. E spesso contengono informazioni che probabilmente non avrebbero mai dovuto essere conservate così a lungo.

Il quadro si complica ulteriormente quando le comunicazioni aziendali si spostano su altri canali. Sempre più spesso vediamo informazioni di lavoro scambiarsi tramite WhatsApp o altre app di messaggistica. Questo apre un nuovo fronte di rischio, perché questi canali sono molto più difficili da controllare dal punto di vista della sicurezza aziendale.

Anche qui la risposta principale non è solo tecnica, ma organizzativa: l’azienda deve decidere se e come questi strumenti possono essere usati, stabilire regole chiare e formare gli utenti sui rischi. Per esempio, bisogna sapere che un messaggio ricevuto da un numero sconosciuto con la foto di un collega non significa necessariamente che sia davvero lui.

Abbiamo visto anche casi molto sofisticati in cui prima veniva compromesso un account Gmail sincronizzato sul telefono della vittima, poi veniva aggiunto un contatto falso con il nome reale della persona. Quando arrivava la chiamata o il messaggio, il telefono mostrava il nome corretto, ingannando completamente l’utente.

Tutto questo dimostra che il fenomeno delle truffe è molto più ampio di quanto possa sembrare a prima vista. Ridurre tutto alla responsabilità individuale rischia di essere una lettura troppo semplicistica.

Nel mondo della sicurezza informatica siamo abituati a ragionare in termini di ecosistema: esistono specialisti tecnici, auditor, esperti di compliance, professionisti della sicurezza offensiva e molti altri ruoli. Ognuno ha competenze specifiche.

Pretendere che una singola persona abbia sempre tutte le conoscenze necessarie per riconoscere ogni tipo di attacco non è realistico.

Per questo motivo alcune aziende stanno iniziando a porsi una domanda interessante: come possiamo renderci conto delle nostre debolezze prima che qualcuno le sfrutti? I security test sono sicuramente uno strumento utile, ma non bastano. Servirebbe una sorta di “grillo parlante”, qualcuno o qualcosa che ci stimoli costantemente a riflettere sulle nostre scelte e sui rischi che potrebbero comportare.

Perché il problema, in fondo, è proprio questo: non possiamo conoscere tutte le minacce emergenti, ma dobbiamo trovare il modo di continuare a metterci in discussione.
