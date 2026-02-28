In questa puntata di Info Sec. Unplugged abbiamo deciso di approfondire un controllo apparentemente semplice dell’Annex A della ISO/IEC 27001: il punto 8.23, Web Filtering.
Sulla carta è descritto in mezza pagina, ma nella pratica tocca uno dei temi più delicati della sicurezza perimetrale. Ci siamo chiesti se questa tecnologia sia davvero la prima grande barriera difensiva delle organizzazioni oppure se, in certi casi, venga sopravvalutata.

Siamo partiti dall’esperienza sul campo, soprattutto da attività offensive. Quasi tutte le aziende dotate di Next Generation Firewall attivano politiche di web filtering, confidando che intercettino traffico malevolo, download sospetti e comunicazioni pericolose verso l’esterno. Spesso però si ripone in questa funzionalità una fiducia eccessiva.

Il meccanismo alla base è relativamente statico: categorizzazione dei domini, reputazione degli IP, analisi del contenuto — quando possibile. Se il traffico è cifrato e non si attiva ispezione SSL, il firewall non può guardare dentro. Inoltre, la categorizzazione non è istantanea. Quando un threat actor registra un nuovo dominio, questo rimane per giorni o settimane in uno stato “uncategorized”. In quel periodo, molti firewall lo lasciano transitare liberamente perché non appartiene a nessuna categoria bloccata.

Abbiamo riflettuto sul tema dei cosiddetti “baby domain”, domini appena registrati. Spesso servono circa trenta giorni prima che escano dalla categoria generica. Nel frattempo, possono essere usati per phishing o landing page malevole. Anche la reputazione IP soffre di un problema temporale: un IP appena attivato parte con reputazione neutra. Finché non viene segnalato o classificato come malevolo, passa senza ostacoli.

Abbiamo poi osservato come la categorizzazione sia spesso alimentata anche da contributi manuali. È relativamente semplice richiedere la ricategorizzazione di un dominio. Questo apre interrogativi sulla robustezza del processo: quanto controllo c’è dietro? Quanto è facile manipolare la percezione di legittimità di un dominio nel tempo?

Un’altra debolezza riguarda i domini “dual use”: servizi legittimi come repository o piattaforme cloud, utilizzati anche per scopi malevoli. Bloccarli completamente è quasi impossibile in molte organizzazioni. Inoltre, esistono scenari in cui un sito legittimo viene compromesso e diventa vettore di attacco. In questi casi, il motore di reputazione non può fare nulla: il dominio rimane categorizzato come lecito.

Abbiamo quindi riconosciuto che il web filtering è uno strumento utile, ma a grana grossa. Serve per “sgranare il grosso”, eliminare categorie evidenti (malware, phishing, command & control), ma non può essere l’unica misura di difesa.

Ci siamo soffermati su un punto pratico: la policy di default. Troppo spesso troviamo configurazioni dove i domini non categorizzati sono consentiti. Eppure, le best practice suggeriscono di bloccarli. È paradossale che una logica “secure by default” non sia effettivamente preconfigurata.

Abbiamo poi analizzato le tecniche di attacco più sofisticate: registrazione di domini simili a quello aziendale, utilizzo di caratteri omografi provenienti da alfabeti diversi ma visivamente indistinguibili, riutilizzo di domini “parked” dopo un periodo di inattività. In scenari mirati, la probabilità che un database globale di reputazione intercetti tempestivamente il dominio è bassissima.

Questo ci ha portato a parlare di threat intelligence proattiva: monitorare la registrazione di domini simili al proprio, anche considerando varianti su alfabeti differenti. È un’attività complessa, ma sempre più necessaria.

Abbiamo poi spostato l’attenzione sui server. Spesso si proteggono gli utenti, ma si dimentica che anche i server possono navigare liberamente. In molti casi abbiamo trovato policy estremamente permissive lato server. Eppure, limitare la capacità di uscita verso internet può interrompere fasi cruciali dell’attack chain, come il download del payload o la comunicazione verso il command & control.

Ci siamo ricordati della vulnerabilità Log4j e di come una Remote Code Execution possa trasformarsi rapidamente in un collegamento verso l’esterno. Se il server non può navigare liberamente, si limita almeno una parte del danno.

Abbiamo poi discusso del ruolo dell’IPS integrato nei firewall. In teoria può analizzare il contesto del traffico in modo più approfondito rispetto alla semplice categorizzazione. In pratica, però, servono regole adeguate e tuning continuo. Troppo rumore porta a ignorare gli alert. Inoltre, l’IPS consuma molte risorse: quando il traffico cresce, spesso viene disattivato per ragioni di performance. E così si perde un altro strato difensivo.

Un tema fondamentale è la retention dei log. Per individuare anomalie o analizzare incidenti, servono anche i log del traffico “lecito”. Se non logghiamo tutto — o se conserviamo solo pochi giorni — perdiamo la possibilità di ricostruire la catena degli eventi. Ma qui si scontrano esigenze operative, limiti tecnici e vincoli normativi.

Abbiamo poi affrontato il problema della mobilità: molti utenti lavorano fuori dal perimetro. Il firewall non vede il loro traffico. Qui entra in gioco l’EDR, che ha visibilità locale sull’endpoint. Tuttavia, l’EDR non copre tutto (stampanti, dispositivi IoT, totem, ecc.) e non sostituisce la visione di rete. Serve sempre una doppia prospettiva: endpoint e network.

Da qui l’idea dell’enterprise browser: un ambiente controllato, separato dal contesto personale, soprattutto in scenari BYOD o provisioning decentralizzato. Non è una soluzione definitiva, ma può offrire un livello di controllo maggiore rispetto alla semplice VPN installata su un dispositivo personale.

Infine, abbiamo toccato il tema della commistione tra dispositivi privati e aziendali. Sempre più incidenti nascono da device personali su cui sono installati strumenti aziendali. Senza visibilità e controllo, queste diventano zone d’ombra difficili da gestire.

Abbiamo chiuso con una riflessione che rimandiamo alla prossima puntata: quanto senso ha continuare a puntare tutto sull’awareness degli utenti, se le tecniche di attacco sfruttano caratteri indistinguibili e meccanismi difficili da riconoscere anche per un occhio esperto?
La formazione resta fondamentale, ma non può essere l’unico argine.
