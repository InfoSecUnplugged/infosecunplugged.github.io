In questa puntata di Info Sec. Unplugged – Extended Edition, assieme a Mattia Parise, raccontiamo un tema che tocca il cuore della continuità operativa: la relazione – e le differenze – tra Disaster Recovery e Cyber Recovery.

Mattia Parise, Solution Architect in un’azienda di cyber resilience, ci accompagna in un viaggio che parte da un presupposto semplice ma fondamentale: i due processi, pur simili nel nome, rispondono a logiche profondamente diverse.

Riflettiamo insieme su come, negli ultimi anni, la gestione del rischio si sia evoluta. Se il Disaster Recovery nasce per affrontare eventi fisici – un guasto, un incendio, un’alluvione – il Cyber Recovery ha l’obiettivo di riportare in vita i sistemi dopo un attacco informatico. Sono mondi che possono condividere infrastrutture, ma solo entro certi limiti.

Mattia ci spiega che nella realtà molte aziende, per ragioni di budget o di semplicità, tendono a far coincidere i due ambienti. Tuttavia, la vera resilienza richiede indipendenza: reti separate, autenticazioni autonome, copie immutabili e processi di ripartenza che non dipendano da ciò che è stato compromesso.

Discutiamo di come progettare una strategia efficace, partendo da una “lista della spesa” – il Bill of Materials – che identifichi tutte le dipendenze critiche. Un’infrastruttura di Cyber Recovery deve poter ripartire da zero, in modo indipendente dall’ambiente produttivo.

Parliamo di tier 0, di autenticazione, di rete e firewall: elementi fondamentali per garantire che, nel momento del bisogno, tutto ciò che serve a riavviare l’azienda sia realmente disponibile e intatto.

Riconosciamo che una delle difficoltà principali sta nella complessità delle infrastrutture moderne. Le interdipendenze tra sistemi, spesso poco documentate, rendono difficile garantire la consistenza dei dati durante un ripristino. L’unico modo per scoprirlo davvero è testare: testing continuo, clean room, simulazioni periodiche. Solo provando a ripristinare possiamo capire quanto siamo pronti.

Mattia ci racconta come le snapshot e le copie di backup possano sembrare soluzioni semplici, ma nascondono limiti: non sempre permettono di tornare indietro nel tempo quanto serve, e non sempre garantiscono che i dati siano puliti. La vera sfida è il *clean recovery*: poter ripristinare sistemi certi, privi di malware, verificati anche con strumenti EDR o analisi forense.
Il backup non deve solo funzionare: deve essere sano.

Ci soffermiamo poi sulla progettazione di un’infrastruttura davvero “cyber resilient”. Deve essere indipendente dalla produzione, avere copie immutabili, accessi controllati e modifiche tracciate con doppia approvazione. Ogni cambiamento deve lasciare traccia e ogni operazione a rischio di perdita dati deve essere autorizzata da più persone.

È un approccio più maturo, che unisce governance, security e processi di compliance.

Un punto chiave è la visibilità. L’integrazione tra il sistema di backup e il CMDB aziendale permette di sapere, in ogni momento, se le risorse critiche sono davvero protette. Serve una dashboard chiara, automatizzata, che mostri l’ultimo backup completato: una piccola ma grande forma di consapevolezza.

Condividiamo anche esempi pratici. Mattia racconta il caso di un’azienda che, grazie a copie in cloud ben configurate, è riuscita a ripartire dopo un attacco. Le copie su Azure, isolate tramite proxy e traffico monodirezionale, si sono rivelate la chiave per la sopravvivenza.

Il cloud, spiegano, può essere un ottimo sostituto della vecchia tape library, a patto di considerare tempi, costi di retrieval e soprattutto l’immutabilità del dato tramite object lock.

Riflettiamo poi sul fatto che oggi è più semplice estendere un sistema di Cyber Recovery per includere funzioni di DR, piuttosto che il contrario. La base di un cyber recovery è più rigorosa, richiede competenze più ampie e un design consapevole. Non è più l’attività “da neoassunti” che era un tempo: oggi chi si occupa di backup deve conoscere sicurezza, rete, infrastruttura e persino database.

Chiudiamo la puntata con una considerazione comune: la cultura aziendale sta cambiando. Normative come DORA e NIS2 stanno accelerando la consapevolezza, ma la vera spinta arriva dall’esperienza diretta – spesso dolorosa – degli incidenti.

Le aziende più mature hanno iniziato a far dialogare i team di sicurezza e di data protection, ma c’è ancora molta strada da fare.

La resilienza non è solo una questione tecnologica: è una questione di processo, collaborazione e responsabilità condivisa.

E, come ci diciamo alla fine, la regola d’oro resta sempre la stessa: rendere l’infrastruttura indipendente, sicura e verificata. Solo così possiamo dormire sonni tranquilli.
