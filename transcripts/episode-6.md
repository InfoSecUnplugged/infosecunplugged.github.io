Oggi abbiamo deciso di parlare di XDR, anche se, come spesso succede, ci siamo ritrovati a esplorare molti temi collegati. Per noi, la XDR rappresenta l’estensione naturale di tutto ciò di cui si è discusso negli ultimi anni: un sistema capace di raccogliere e ingerire dati da qualsiasi fonte, teoricamente.

In pratica, però, l’ingestion dei dati non significa automaticamente correlazione efficace. Se buttiamo dentro log provenienti da firewall, directory, anti-spam o web application firewall, dobbiamo costruire regole che permettano di elevare gli eventi a incidenti, e poi farli passare per il triage. È qui che la teoria si scontra con la realtà.

Ci aspettavamo che i grandi vendor avessero già integrato molte di queste funzionalità. Invece ci stiamo muovendo lentamente verso una sorta di sostituzione parziale del SIEM. Non sono equivalenti, certo, ma dal punto di vista aziendale un sistema XDR che copre buona parte della visibilità può risultare molto più accattivante: richiede meno configurazione, meno parsing manuale, meno costi infrastrutturali. Insomma, una soluzione più appetibile, anche se ancora lontana dall’essere completa.

Quando proviamo a estendere la visibilità di un EDR includendo log di terze parti, in effetti otteniamo una prospettiva più ampia. Ha perfettamente senso per un analista che fa triage o investigation. Ma se iniziamo a creare regole di correlazione, finiamo per sviluppare un piccolo SIEM dentro l’EDR. Questo renderebbe la piattaforma più completa, ma anche più complessa da gestire. Ci chiediamo spesso se l’obiettivo finale sia davvero sostituire il SIEM o piuttosto affiancarlo.

Vediamo poi un collegamento sempre più stretto tra XDR e SOAR: una volta raccolti tutti i dati, la tendenza è passare subito all’automazione. Nelle architetture moderne questo legame è evidente. Eppure, oggi, nessun XDR è in grado di sostituire completamente un SIEM nelle sue capacità di correlazione, anche se i due modelli operativi si stanno avvicinando sempre di più.

Facendo un esempio concreto: la maggior parte delle aziende dispone di un EDR e di uno o due firewall. Se il vendor è lo stesso, nasce già una prima forma di XDR integrato. Per gli altri vendor, in teoria, non sarebbe complesso aggiungere il supporto a tre o quattro firewall principali. Quello che sorprende è che quasi tutti hanno una Active Directory interna, eppure pochi vendor sfruttano davvero i log di AD per fornire regole di correlazione predefinite, come facevano i SIEM. Se ci fossero regole già pronte, da attivare a scelta, copriremmo gran parte dei casi reali.

Dopotutto, la maggior parte degli attacchi passa da endpoint, firewall e directory: avere visibilità su questi tre elementi significa già coprire oltre il 90% della superficie utile di un’azienda.

È anche un’opportunità interessante per i security integrator che offrono servizi MDR: possono differenziarsi sviluppando regole personalizzate, ad esempio integrando i log dell’anti-spam o dell’Active Directory. Ma qui nasce il rischio che, un domani, il vendor integri direttamente quelle stesse funzioni, cancellando il valore aggiunto del partner. È un equilibrio delicato: innovare sì, ma con la consapevolezza che l’evoluzione della piattaforma può livellare tutti.

L’automazione, comunque, è cruciale. Permette di gestire centinaia di clienti, ma richiede piattaforme ben supportate. Le regole automatiche devono essere generiche, e non è facile farlo senza perdere efficacia. Quando una piattaforma non segnala un comportamento sospetto, anche se ne vede la telemetria, spesso non è un difetto, ma una scelta del vendor, che preferisce non essere troppo restrittivo.

Naturalmente, tutto questo funziona solo se usiamo l’EDR “con coscienza”: non è magico, non blocca tutto, ma si comporta in base alle regole definite. Se comprendiamo bene il comportamento e lo interpretiamo correttamente, anche i dati di terze parti, come quelli dell’antispam o del firewall, diventano indicatori di compromissione preziosi.

Il vero punto è: possiamo avere tutti i dati del mondo, ma se non impariamo a usarli, non cambia nulla.

Abbiamo visto anche molti casi di aziende con un SOC esterno che gestisce i log ma non l’EDR interno. In questi scenari, dare accesso alla piattaforma EDR al SOC migliorerebbe l’investigation, ma spesso non succede. Così si crea uno scollamento tra informazioni di rete e informazioni sugli endpoint, rendendo difficile collegare un alert del firewall con un evento registrato sull’EDR.

Integrare tutto questo non è banale, e spiega perché il SIEM continua ad avere un ruolo — anche se costoso. Portare i dati dell’EDR dentro un SIEM è oneroso, sia in termini economici sia di gestione. Per questo molti guardano all’XDR come una soluzione operativamente più semplice e meno costosa, soprattutto se cloud-based.

Ma attenzione: buttare tutti i log nel SIEM non basta. Il valore nasce solo se i dati vengono interpretati. Altrimenti restano rumore, spazio occupato e costi inutili.

E poi c’è anche la questione del disaster recovery: tutti quei dati devono essere replicati altrove, aumentando i costi complessivi.

In prospettiva, vediamo un’evoluzione lenta ma chiara verso un XDR “completo”, capace di integrare rule, investigation e automazione. Però stiamo anche assistendo a una sovrapposizione crescente con i SOAR, spesso percepiti come la panacea: “non serve più fare investigation, ci pensa l’automazione”. Noi restiamo scettici: l’automazione è una ottimizzazione, non una scorciatoia. L’investigation umana resta insostituibile, almeno per ora.

Certo, può aiutare nell’arricchimento degli eventi, ma non può sostituire l’analisi esperta. E l’intelligenza artificiale, oggi così di moda, non è la risposta a tutto: soprattutto in contesti dove il comportamento “lecito” e “malevolo” può cambiare da azienda a azienda. Non possiamo fidarci ciecamente di un algoritmo che decide da solo.

Lo stesso vale per la anomaly detection: funziona bene in teoria, ma in pratica i threat actor sanno come sfruttarla a loro vantaggio, avvelenando la base dati. Se la usiamo senza controllo, rischiamo di renderla inefficace.

Abbiamo visto casi emblematici: come quello in cui un sistema comportamentale segnalò come anomalia la diminuzione delle connessioni SSH, solo perché un malware che le generava era stato eliminato. Oppure la difficoltà di un web application firewall nel capire cosa fosse davvero “normale” in contesti complessi, dove le richieste sono migliaia e gli applicativi infiniti.

La verità è che molti sistemi basati su anomaly detection presuppongono che la rete sia pulita nella fase di apprendimento. Ma quante aziende fanno davvero una bonifica prima del learning? Pochissime. E così i modelli imparano che il traffico malevolo è normale.

Chi lavora in un SOC, con dataset ampi provenienti da più clienti, riesce a mitigare parzialmente questo limite. Ma nelle installazioni on-premise, con dati limitati e poco storico, il problema resta serio. Perché l’anomaly detection ha bisogno di molto tempo e molti dati storici per funzionare bene.

Concludendo, l’evoluzione dell’XDR e del suo ecosistema (SIEM, SOAR, AI, Anomaly Detection) è affascinante ma complessa. Abbiamo toccato tantissimi temi oggi, e ci lasciamo con l’idea di tornare presto a parlarne — magari con un ospite che lavora direttamente su Red Teaming o OT Security.

Noi, intanto, continuiamo a osservare, curiosi e un po’ scettici, questo mondo in rapida ma incerta trasformazione.
