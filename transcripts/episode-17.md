Oggi in Info Sec. Unplugged vogliamo parlare di un tema spesso sottovalutato ma fondamentale: la documentazione in azienda.

Ci capita troppo spesso di vedere realtà dove la documentazione è incompleta, datata o semplicemente inesistente. Quando chiediamo di mostrarci documenti di rete, procedure operative o asset, la risposta tipica è che ci sono bozze non aggiornate. Non è sempre un disastro, ma quasi mai troviamo documentazione davvero completa e viva.

Il problema, secondo noi, è duplice: da un lato mancano strumenti davvero pensati per fare documentazione in modo strutturato e integrato; dall’altro c’è ancora l’abitudine di lavorare con Word ed Excel. È un approccio sbagliato: tenere aggiornata una documentazione a suon di file statici è impossibile. Le normative – dal GDPR alla ISO 27001 – richiedono una dinamicità che un foglio Word non può offrire.

Ci piace pensare alla documentazione come a un ecosistema. Esistono diversi livelli: le policy e le procedure, che descrivono processi e regole aziendali, e la documentazione tecnica, che racconta come le cose funzionano davvero. Quest’ultima non va confusa con la reportistica: se i dati vivono in un database, quello è già un pezzo di documentazione. Il documento serve solo a dare contesto e coerenza.

Noi abbiamo sperimentato diversi strumenti: da xWiki a GitBook, passando per soluzioni più integrate. Le wiki funzionano bene, ma diventano caotiche se non c’è governance. Serve definire una struttura, assegnare responsabilità e mantenere ordine: altrimenti il wiki diventa un cestino digitale dove si accumula di tutto.

Sul fronte tecnico, la documentazione di rete è forse la più critica. Molte aziende hanno solo disegni ad alto livello che non aiutano chi deve lavorarci. Per noi la documentazione parte da una base solida: sapere cosa abbiamo e dove si trova. Poi arriva la descrizione di come i sistemi comunicano.

Qui entrano in gioco strumenti come CMDB, Asset Inventory e, in particolare, gli IPAM. Questi strumenti permettono di rappresentare la rete in modo strutturato, gestire subnet, VLAN, router e ottenere una visione chiara di come gira il traffico. Sono infinitamente più utili di un diagramma Visio che nessuno aggiorna mai.

L’automazione può aiutare moltissimo. Anche semplici script possono raccogliere informazioni dai device e aggiornare i database. Ci sono ottimi strumenti open source come NetBox o Nautobot, che rappresentano bene la rete e riducono il caos tipico dei file Excel pieni di indirizzi IP. L’importante è partire con regole chiare – naming convention, standard di configurazione – per evitare di trovarsi VLAN e device nominati in modi diversi.

La documentazione serve anche per mantenere la compliance tecnica: se definiamo modelli di configurazione per switch o firewall, dobbiamo garantire che i sistemi restino allineati a quei template. E qui il legame con la sicurezza è fortissimo.

Quando la rete non è documentata, diventa impossibile capire dove passa il traffico, come si propagano le connessioni o dove sta il problema in caso di fault. In quelle situazioni si perde tempo, si lavora nel panico e cresce l’entropia.

Il firewall è un altro punto critico. Troppo spesso le regole vengono aggiunte senza controllo, senza sapere chi le ha create o perché. Lo stesso vale per DNS e Active Directory: ambienti caotici, stratificati nel tempo, dove si aggiunge sempre e non si toglie mai nulla.

Per questi sistemi ha senso documentare la struttura e le logiche di base – le zone di un firewall, i gruppi di un’Active Directory – più che le singole voci o regole. La granularità va scelta con intelligenza.

Parlando proprio di Active Directory, emerge un altro aspetto: la collaborazione tra IT e HR. L’HR è spesso l’origine delle richieste di accesso e dovrebbe poter verificare le configurazioni senza passare sempre dall’IT. I sistemi di Identity Management servono esattamente a questo: descrivere in modo comprensibile chi può fare cosa, in un linguaggio chiaro anche per chi non è tecnico.

Così si evitano errori come “clonare” i permessi da un collega – pratica ancora diffusissima – e si mantiene controllo e responsabilità. L’automazione non deve servire a parlare con l’Active Directory in linguaggio naturale, ma a semplificare e rendere sicuri i processi. Prima si definisce come deve avvenire qualcosa, poi si automatizza.

Alla fine, tutto questo discorso sulla documentazione non è un esercizio di stile. Serve a ridurre gli errori, l’entropia e il caos operativo.

Quando c’è un guasto, un incidente o un attacco, la mancanza di informazioni strutturate genera panico e rallenta tutto. Non è accettabile impiegare quindici minuti solo per trovare le credenziali di accesso a un apparato. La documentazione deve essere disponibile, aggiornata e, soprattutto, resistente ai fault — deve vivere anche quando l’infrastruttura non lo fa.

Ecco perché crediamo che la documentazione sia il primo vero atto di governance. È un impegno costante, non un progetto una tantum. Ma quando è fatta bene, diventa la base per ogni processo di sicurezza, automazione e resilienza aziendale.
