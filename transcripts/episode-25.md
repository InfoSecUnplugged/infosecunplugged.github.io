Bentornati a Info Sec. Unplugged!

Da questa puntata, il podcast sarà disponibile solo su Spreaker e sulle piattaforme audio dedicate. Sul canale YouTube di Rocco troverete invece un highlight video con un riassunto e qualche anticipazione. In più, come sempre, ci sarà un post descrittivo allegato, con esempi pratici e riferimenti tecnici per chi vuole approfondire visivamente i casi di cui parliamo.

Nell’episodio precedente avevamo promesso di fare ordine nell’analisi di un incidente di sicurezza, raccontando la storia di un attacco in modo formale e strutturato. Oggi vogliamo proprio farlo: entrare nella mentalità dell’attaccante e imparare a leggere il suo comportamento.

Parlando al caffè questa mattina, riflettevamo su come il mondo della Threat Intelligence sia, per certi versi, molto più vicino a quello dell’Offensive Security che a quello puramente difensivo.

Chi lavora nell’offensiva studia gli attacchi dei threat actor per emularli — creare simulazioni, strumenti o artefatti utili a testare la resilienza dei sistemi.

Chi fa Threat Intelligence, invece, osserva lo stesso scenario ma da un’altra prospettiva: analizza attacchi già avvenuti, raccoglie dati sulle infrastrutture, sugli strumenti e sui comportamenti degli attori malevoli per anticiparne le prossime mosse.

In entrambi i casi, l’obiettivo è capire la mente dell’attaccante: noi lo emuliamo, noi lo anticipiamo. È lo stesso soggetto — l’attacco — visto da due lati diversi.

Un esempio emblematico riguarda l’uso di Python su macchine Windows per restare “under the radar” rispetto a PowerShell. L’idea, nata nei paper di ricerca tra il 2018 e il 2020, era stata inizialmente esplorata per studiare le lacune dei sistemi di detection, e poi sfruttata dai threat actor stessi.

La ricerca, come spesso accade, apre porte che possono essere usate sia per difendersi sia per attaccare. È un mercato dual use, e lo vediamo anche nel mondo degli exploit e delle CVE: la corsa alla scoperta di vulnerabilità genera valore, ma anche rischi, perché le stesse informazioni possono alimentare tanto l’intelligence militare quanto il cybercrime.

Ma torniamo al nostro caso pratico.

Abbiamo deciso di analizzare una campagna di phishing, partire dall’e-mail e seguire la catena dell’attacco fino alla fine, per capire come strutturare l’informazione in modo da trarne valore operativo.

L’evento iniziale è un’e-mail che sembra provenire da Decathlon, con una classica “offerta imperdibile”. L’utente, cliccando sul link, viene portato a un sito e-commerce dove, pagando 5 euro di spedizione, dovrebbe ricevere un prodotto di valore superiore. Naturalmente è una truffa.

Da qui inizia il lavoro dell’analista di Threat Intelligence.

L’utente segnala l’e-mail (quando va bene), oppure ci clicca sopra (quando va male).
Nel primo caso, il team SOC la riceve come segnalazione e la passa all’analisi; nel secondo, l’incidente viene scoperto solo dopo, in reazione.

L’analista parte dall’e-mail, analizzandone due sezioni fondamentali: header e body.

L’header contiene i dettagli tecnici del percorso della mail — mittente, IP sorgente, server attraversati, reputazione dei domini.

Il body invece mostra il contenuto effettivo: testo, link, eventuali allegati o elementi HTML nascosti.

Spesso gli attaccanti sono molto accorti: utilizzano domini leciti, infrastrutture compromesse o addirittura bucket cloud pubblici per ospitare i propri artefatti.

Nel nostro caso, la mail era passata indenne attraverso i filtri antispam: lo score era troppo basso per bloccarla.

Analizzando il sorgente dell’e-mail abbiamo trovato un piccolo trucco: nel codice HTML era inserito un thread fittizio, in più lingue, non visibile al destinatario ma letto dai filtri antispam. Alcuni sistemi, infatti, assegnano punteggi più alti a messaggi che sembrano parte di una conversazione.

Il threat actor, sfruttando questa logica, “inganna” il sistema simulando un thread. Un esempio perfetto di come ogni automatismo possa essere avvelenato.

Nel body c’era il link alla finta offerta, che puntava a un bucket di Google Cloud Storage: apparentemente innocuo, perché l’URL è di un dominio affidabile.

Dentro quel bucket, però, c’era un piccolo file HTML con un semplice script di redirect verso un altro dominio, e così via, per tre passaggi consecutivi.

È improbabile che un sistema di sicurezza analizzi tutta la catena di redirect: di solito si ferma al primo o al secondo. L’utente, alla fine, approda su un falso e-commerce, dove il pagamento serve solo a carpire i dati della carta di credito.

Questo tipo di campagna, apparentemente banale, mostra bene la necessità di raccontare la “storia” dell’attacco, non solo di reagire all’incidente.

Tutti gli elementi raccolti — indirizzi IP, domini, hash, titoli, pattern — vengono salvati e correlati, ad esempio su una piattaforma come MISP (Malware Information Sharing Platform).

Ogni informazione è un attributo, e alcuni di questi diventano IOC (Indicator of Compromise).

Con MISP possiamo rappresentare graficamente il flusso dell’attacco, correlare eventi, condividere gli IOC con il SOC o con altre organizzazioni, e anche verificare retroattivamente se la nostra infrastruttura è già stata toccata dallo stesso tipo di campagna.

Condividere è fondamentale. Le piattaforme come MISP nascono proprio per questo: creare un ecosistema in cui ogni organizzazione arricchisce la conoscenza collettiva.

Chi ha già un SOC, un SIEM, strumenti di EDR o XDR, può integrare questi feed nel proprio ambiente di detection e prevention, filtrandoli e pesandoli con attenzione.

Non si tratta di riversare milioni di indicatori a caso — anche perché un firewall non può gestirli tutti — ma di selezionare quelli pertinenti, attivi e verificati.

Un aspetto spesso trascurato è la “data di scadenza” degli IOC.

Un bucket Google usato per una campagna oggi, domani sarà chiuso, quindi quell’indicatore perde validità.
MISP prevede anche sistemi di validazione tra community (sighting), che permettono di segnalare se un IOC è ancora valido, falso positivo o ormai obsoleto.

Integrare la Threat Intelligence non è questione di installare un software: è costruire un ecosistema coerente, dove dati, processi e persone collaborano.

Gli strumenti automatici possono aiutare — ad esempio estrarre in automatico gli IOC dalle e-mail o alimentare i firewall — ma serve sempre una supervisione umana che interpreti il contesto.

Abbiamo raccontato questo caso per mostrare come, anche partendo da un’e-mail apparentemente semplice, si possa ricostruire un’intera catena di attacco e trasformarla in conoscenza utile, condivisibile e azionabile.

È questo il cuore della Threat Intelligence: passare dalla reazione alla comprensione, dall’evento isolato alla storia completa.

E così chiudiamo un piccolo ciclo di tre puntate dedicate all’analisi strutturata degli incidenti di sicurezza.

Abbiamo toccato concetti tecnici, strategici e metodologici — dal phishing alle infrastrutture cloud, dal ruolo del SOC a quello dell’intelligence, fino ai modelli di condivisione tra organizzazioni.
Un viaggio dentro il modo in cui impariamo, ogni giorno, a capire e raccontare la sicurezza informatica.

Alla prossima puntata di Info Sec. Unplugged!
