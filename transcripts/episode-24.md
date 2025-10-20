Siamo di nuovo qui, a “Info Sec. Unplugged”. Siamo Andrea D’Inese e Rocco Sicilia, e ci ritroviamo dopo un’estate intensa, con le agende troppo piene e poco tempo per registrare. Nell’ultimo episodio avevamo parlato di EDR e SIEM, cercando di capire se uno potesse sostituire l’altro. Avevamo concluso che non esiste una soluzione unica per tutti: ogni contesto deve trovare il proprio equilibrio.

Oggi riprendiamo da lì, dalle fondamenta. Le piattaforme di sicurezza come EDR e XDR raccolgono log e telemetrie per generare rilevamenti, osservando i comportamenti dei sistemi: processi sospetti, chiamate verso IP malevoli, o eseguibili con hash noti. L’obiettivo è capire come usare questi dati non solo per ricevere informazioni, ma anche per contribuire — arricchendo la comunità con le nostre analisi e riflessioni.

Una delle prime lezioni che abbiamo imparato è che non basta buttare tutti i log nel SIEM. L’approccio “più dati = più sicurezza” non funziona, oltre a essere costoso. Serve capire quali scenari vogliamo coprire e qualificare i log in base alle regole di detection che intendiamo costruire. Se non sappiamo che dati stiamo acquisendo, non possiamo nemmeno scrivere regole sensate. Il SIEM non è una macchina magica che mette ordine nel caos: è potente, ma va configurato, integrato, adattato.

Spesso crediamo che basti inviare tutti i log di un firewall al SIEM per essere protetti. In realtà, il sistema di correlazione potrebbe non trarre alcun valore da quei dati se non sono strutturati nel modo giusto. Occorre bilanciare efficienza ed efficacia, evitando sprechi e focalizzandosi su ciò che serve davvero.

Da qui il collegamento naturale con la Threat Intelligence: per riconoscere minacce serve un termine di paragone, una conoscenza aggiornata di tattiche, tecniche, infrastrutture e indicatori di compromissione (IOC). Queste informazioni — come IP malevoli, hash di malware, domini sospetti — vengono documentate da analisti e vendor, e poi distribuite sotto forma di feed. I firewall o gli EDR, ad esempio, ricevono automaticamente liste di IOC dai vendor per bloccare traffico malevolo in tempo reale.

Il limite di questo approccio “real-time only” è evidente: tutto ciò che è accaduto prima di conoscere un determinato IOC rimane invisibile. Per questo si parla di Threat Detection da un lato, e Threat Hunting dall’altro — la ricerca attiva di indizi di compromissione passati.

La quantità di IOC in circolazione è enorme, e non possiamo usarli tutti. Ogni azienda deve scegliere quelli pertinenti al proprio contesto. Un istituto finanziario, ad esempio, sarà interessato a dati su truffe e frodi, mentre un’azienda manifatturiera no. C’è quindi un processo di qualificazione: capire quali IOC servono davvero e quali no, considerando anche la loro “scadenza”, perché gli attaccanti cambiano infrastrutture rapidamente.

Man mano che gli IOC diventano più complessi, non si limitano a un indirizzo IP o a un hash: diventano storie, catene di eventi che descrivono tattiche e comportamenti. Comprendere la “storia” di un attacco permette di scrivere regole di detection più durature, basate sui comportamenti e non su singoli elementi statici.

Naturalmente, non tutte le aziende possono gestire internamente un processo di intelligence. Per la maggior parte, è compito del SOC (Security Operations Center) esterno, che fornisce il servizio di monitoraggio, detection e miglioramento continuo. L’azienda cliente deve assicurarsi che il proprio SOC utilizzi fonti di intelligence aggiornate e che sappia adattare le regole di detection di conseguenza.

Gli attori in gioco sono tre:

L’utente finale, che deve avere strumenti ben configurati.

Il provider SOC/MDR, che raccoglie e analizza i feed di intelligence.

Il partner tecnologico, che implementa e ottimizza le regole di detection nei sistemi.

Tutti devono collaborare. Il SIEM da solo non basta, né il firewall, né un feed acquistato “chiavi in mano”.

Un punto cruciale è la configurazione: spesso durante gli assessment scopriamo sistemi lasciati quasi in default. Quando gli attacchi simulati vanno a buon fine, non è perché la tecnologia è inefficace, ma perché non è configurata correttamente. Le regole predefinite non bastano: vanno adattate al contesto del cliente e riviste nel tempo.

La Threat Intelligence entra qui come motore di miglioramento. Sapere come operano gli attaccanti ci aiuta a costruire regole specifiche: per esempio, se un gruppo usa WebSocket per comunicazioni di Command and Control, possiamo creare una detection ad hoc.

Il principio dello Zero Trust, spesso citato come filosofia ideale, resta un obiettivo difficile da raggiungere. In pratica, gli attaccanti riescono spesso a sfruttare servizi legittimi — come GitHub, Google Storage o SharePoint — per nascondere i propri canali di comunicazione. Bloccarli è impossibile, perché sono risorse usate anche legittimamente dalle aziende.

In un caso reale, una campagna di phishing sfruttava un link a un bucket GCP con dentro un semplice HTML di redirect verso un sito malevolo. Il sistema antispam lasciava passare l’email perché il dominio era “pulito” (appartenente a Google). Solo un’analisi combinata dei log — dalla posta elettronica, dal firewall, e dai processi utente — avrebbe potuto ricostruire la storia completa dell’attacco.

È proprio questo il futuro della detection: non guardare singoli eventi, ma ricostruire sequenze coerenti di azioni. Per farlo servono dati completi, conoscenza di come si muovono gli attaccanti, e regole scritte in base al contesto.

Chiudiamo con un pensiero: dobbiamo imparare a “fare ordine”. Capire come approcciare la complessità della Threat Intelligence, come integrarla nei processi e come farla gestire — internamente o dal proprio SOC.
Nel prossimo episodio vogliamo entrare nel concreto: partiremo da un esempio pratico di evento di threat intelligence, ne analizzeremo gli elementi e vedremo come trasformarli in regole di detection operative.

Continuate a seguirci, e come sempre, fateci sapere cosa ne pensate e se un approfondimento pratico vi piacerebbe.
Alla prossima!
