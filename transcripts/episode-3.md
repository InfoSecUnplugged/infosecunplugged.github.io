In questa puntata di Info Sec. Unplugged volevamo affrontare un tema che sta diventando sempre più centrale nel mondo della sicurezza informatica: gli EDR. È una tecnologia ormai affermata, ma notiamo ancora parecchia confusione. Le soluzioni sono tante, le proposte dei vendor amplissime, e spesso si tende a consultare il solito quadrante Gartner per orientarsi, senza però considerare i dettagli nascosti che influenzano in modo decisivo la scelta e l’uso effettivo di queste piattaforme.

Ci accorgiamo che molti interpretano l’EDR come una sorta di antivirus evoluto: qualcosa che installi, configuri e poi lasci lavorare da solo, aspettandoti che intercetti ogni minaccia. In realtà non è così. L’EDR è progettato non solo per rilevare comportamenti malevoli, ma anche per permetterci di fare hunting — cioè di andare a caccia di attività sospette all’interno della nostra infrastruttura. E qui nasce il primo grande malinteso: quasi nessuno utilizza queste soluzioni per cercare attivamente i segnali deboli di un attacco in corso.

Spesso le aziende si sorprendono quando scoprono che l’EDR non ha generato un allarme di fronte a un’attività sospetta che poi si rivela essere il preludio di un incidente. Ma il punto è che l’EDR aveva visto quegli eventi: semplicemente non aveva le regole giuste per interpretarli come parte di una minaccia.

Questo ci porta a distinguere due grandi funzioni dell’EDR.

Da un lato, la capacità automatica di rilevare e bloccare comportamenti malevoli; dall’altro, la possibilità di fare hunting per scoprire ciò che non è stato intercettato automaticamente. Le soluzioni sul mercato, però, non sono tutte equivalenti: alcune sono più “pronte”, installi e funzionano con una buona copertura di base; altre richiedono un tuning avanzato e una configurazione approfondita da parte di un team esperto, per offrire lo stesso livello di efficacia.

E qui sorge un altro problema: molte aziende, soprattutto nel settore manifatturiero italiano, non hanno risorse interne con le competenze necessarie per fare tuning, creare regole di detection personalizzate o gestire feed di threat intelligence. Spesso si affidano completamente ai partner o ai vendor, senza strumenti per valutare criticamente la qualità del servizio ricevuto.

La maggior parte delle implementazioni resta così ferma alla configurazione “di default”, quella che il vendor fornisce appena accendi il tenant. Ma gli stessi produttori lo dicono chiaramente: la configurazione di default non è sufficiente per la produzione. L’EDR funziona davvero solo quando viene personalizzato sulle esigenze del contesto in cui opera — quando qualcuno crea regole aggiuntive, aggiorna costantemente i parametri, e svolge attività di monitoraggio continuo.

Questo richiede tempo, risorse e competenze specialistiche, e non tutte le aziende possono permetterselo. Così, anche piattaforme molto potenti finiscono per essere sottoutilizzate, trasformandosi in strumenti che “vedono tutto ma non capiscono cosa stanno guardando”.

Serve quindi una gestione continua, basata su tre dimensioni:

1. Gestione operativa degli eventi e degli incidenti sollevati dall’EDR.
2. Attività di hunting, per verificare se ci sono comportamenti anomali non segnalati.
3. Evoluzione costante delle regole di detection, integrando feed di threat intelligence e best practice dei vendor.

In teoria è il modo corretto di operare; nella pratica, è quasi utopia. Pochissime aziende lo fanno davvero.

Negli ultimi anni, questa complessità ha spinto verso un’evoluzione: l’XDR, che estende il concetto di EDR collegandolo a un ecosistema più ampio, integrato con sistemi di SIEM e SOC, e capace di correlare dati da fonti diverse. È la direzione naturale per affrontare una minaccia in continua evoluzione.

Il punto è che gli attacchi moderni non si basano più solo su malware riconoscibili: oggi molte minacce operano senza usare alcun malware, sfruttando strumenti legittimi in modo malevolo. In questo contesto, le tecnologie tradizionali — antivirus o antimalware basati su firme — sono diventate inutili. Serve un approccio comportamentale, ma soprattutto serve qualcuno che sappia interpretare i comportamenti.

E anche quando l’EDR funziona bene, bisogna capire che il rilevamento non è sempre istantaneo. A volte la piattaforma ha bisogno di tempo per raccogliere abbastanza eventi e “arricchire” le informazioni prima di capire che una sequenza di azioni costituisce un attacco. È un processo che somiglia molto alla correlazione dei dati nei SIEM, solo che qui avviene a livello comportamentale.

Per questo motivo, insistiamo con i clienti: non serve avere un presidio 24/7 davanti a un muro di monitor, come si vede nei film. Quello che conta davvero è la capacità di analizzare, contestualizzare e reagire in modo consapevole. La velocità è importante, ma la comprensione lo è di più.

Alla fine, l’EDR — e ancor più l’XDR — rappresentano la risposta tecnologica a un mondo in cui le minacce evolvono continuamente. Ma finché continueremo a trattarli come semplici “antivirus più intelligenti”, resteranno strumenti potenti ma incompleti. La vera differenza la fa la conoscenza: quella di chi li usa, li configura, e soprattutto li comprende.
