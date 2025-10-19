Bentornati a Info Sec. Unplugged!

Prima di entrare nel vivo, vogliamo ringraziare chi ci segue. Ascoltando le puntate precedenti ci siamo accorti di quanto spesso divaghiamo: prendiamo tangenti, apriamo parentesi, ma alla fine restate con noi, quindi davvero grazie.

Oggi vogliamo raccontarvi il percorso con cui si costruisce una procedura di Disaster Recovery (DR), passando dai principi di design fino alle tecnologie e alle azioni pratiche. Il nostro obiettivo è immaginare il “DR mitologico”: quello che tutti vorremmo realizzare, ma che nessuno riesce mai a ottenere pienamente.

Il punto di partenza, come giustamente ci diciamo sempre, non è la tecnologia, ma il business: i requisiti, i processi e l’impatto reale sul lavoro.

Spesso vediamo aziende in cui la progettazione del DR viene scaricata sull’IT da parte del management o della compliance, con la logica del “si deve fare”. Ma non funziona così. Né basta dire “abbiamo un backup”: non è questo un piano di disaster recovery, soprattutto oggi, dove il concetto di resilienza all’attacco – o “cyber recovery” – è diventato centrale. Non si tratta più solo di guasti tecnici, ma di veri e propri incidenti cyber, che cambiano completamente lo scenario rispetto a dieci anni fa.

Noi non vogliamo fare una puntata ipertecnica. Il nostro obiettivo è divulgativo: essere chiari, comprensibili, anche per chi non vive di IT ogni giorno.

Quando parliamo di DR con le aziende, partiamo da tre parametri fondamentali, che dovrebbero discendere da una Business Impact Analysis (BIA). E qui cominciano i problemi: quante aziende hanno davvero una BIA fatta e aggiornata? Pochissime. Solo in contesti particolarmente regolamentati – come le multi-utility o le acciaierie – la BIA è una prassi obbligatoria.

Per la maggior parte, invece, ci si arriva quando serve rivedere il DR. Negli ultimi anni, normative come la NIS hanno dato una spinta importante, perché impongono di ragionare sull’impatto reale di un’interruzione e sulla capacità di continuità operativa.

La BIA serve proprio a rispondere alla domanda: “Cosa succede se…?”

Cosa succede se non ho più internet? Se la posta elettronica non funziona? Se la produzione si ferma? Capire il tempo che posso sopportare di fermo e la quantità di dati che posso permettermi di perdere è il punto di partenza.

Non si tratta solo di tecnologia, ma di collegare in modo consapevole i servizi IT ai processi di business.

I tre parametri di base sono RTO, RPO e la distinzione tra DR parziale o totale.

L’RTO (Recovery Time Objective) indica il tempo massimo accettabile per riportare online i servizi dopo un disastro.

L’RPO (Recovery Point Objective) rappresenta invece la quantità di dati che posso perdere.

Ma attenzione: non basta definire numeri astratti. Bisogna tradurli in casi reali: “Per quanto tempo puoi permetterti di non spedire più merce?” oppure “Quante ore di ordini puoi perdere senza conseguenze gravi?”. È così che si ottengono risposte sensate dal management.

Più l’RTO e l’RPO sono brevi, più i costi aumentano. Tecnologie e automazioni per abbatterli esistono, ma non sono gratuite.

Oggi, poi, lo scenario è molto diverso rispetto al passato: non parliamo più solo di incendi o guasti allo storage, ma di attacchi informatici che possono essere avvenuti mesi prima e di cui ci accorgiamo tardi. E allora, da dove parte davvero il mio RPO?

Molti piani DR prevedono ormai anche scenari “in caso di cifratura totale dei sistemi”, ma spesso mancano riferimenti a tutto ciò che precede l’attacco. La vera difficoltà è capire quando è sicuro ripristinare.

Un’altra distinzione cruciale è quella tra DR parziale e totale. Può sembrare una scelta tecnica, ma cambia tutto: costi, tempi e complessità. In teoria, un DR totale è più lineare da gestire, ma richiede molte più risorse. In pratica, la maggior parte delle aziende copre solo una parte dei servizi, lasciandone altri scoperti – e spesso senza saperlo davvero.

La trasparenza con il management è fondamentale: bisogna dichiarare cosa è coperto e cosa no.
Meglio un piano dichiaratamente limitato che un DR “finto”.

Poi ci sono i vincoli fisici. Abbiamo visto troppi siti di DR a 20 chilometri da quello principale: logisticamente comodi, ma inefficaci in caso di disastro regionale. Alcune normative lo accettano, se il business è legato al territorio, ma serve comunque un’analisi di rischio sismico e idrogeologico.

Fare DR in un’area soggetta allo stesso evento distruttivo non ha senso.

C’è anche un tema di performance: spesso il sito di DR ha meno risorse di quello principale, e quindi le prestazioni calano. È normale, ma va scritto nero su bianco, perché in caso di crisi il management non può scoprire solo allora che “va più lento”.

Noi, se possiamo, preferiamo la simmetria: due siti degni, con repliche incrociate e pari dignità. È l’unico modo per dormire tranquilli.

Un buon DR nasce da un’infrastruttura resiliente. Se un sito non è stabile di suo, fare DR su di esso è solo un’illusione. Meglio investire prima nella fault tolerance e nella ridondanza.

E non dimentichiamo la responsabilità personale: con l’evoluzione normativa, come la NIS2 (entro il 2026), i manager IT rispondono in prima persona di certe scelte. È un motivo in più per documentare tutto e condividere le decisioni.

Un altro tema è la gestione dei fornitori critici.

La normativa DORA richiede di avere piani di uscita per i vendor essenziali: cloud provider, vendor di virtualizzazione, firewall, EDR, e persino criteri etici di fornitura. È un concetto spesso ignorato, ma fondamentale: se il tuo fornitore cambia proprietà o strategia e non rispetta più i tuoi requisiti di sicurezza o compliance, devi poter uscire in modo controllato.

È difficile, certo, perché quasi tutti i vendor fanno lock-in tecnologico, ma non impossibile.

E a proposito di cloud, molte aziende inseriscono il cloud storage nel piano DR, magari come backup freddo. Nulla di male, purché ci si renda conto di tempi e costi reali: se devo recuperare 50 terabyte con 300 megabit di banda, servono giorni e molto denaro. Il cloud può essere una “ultima spiaggia”, ma non va confuso con un DR operativo.

Fondamentale è la prova del piano: testarlo periodicamente, in condizioni realistiche.
Solo provando il recovery possiamo sapere se funziona davvero. E quando il test viene fatto collegandosi al sito primario (quello che in teoria non dovrebbe esistere più), beh… qualcosa non va.

Bisogna simulare l’accesso al sito secondario, verificare le credenziali, controllare che i dati siano coerenti, che i backup siano restaurabili. Altrimenti, al momento del bisogno, non funzionerà.

Infine, un punto spesso trascurato: i gruppi di consistenza.

Quando facciamo le fotografie (snapshot) dell’infrastruttura, raramente abbiamo una copia coerente di tutto. Database, macchine virtuali, storage diversi e dati nel cloud possono essere asincroni. Questo crea problemi logici: se una transazione cade a metà, i dati possono risultare duplicati o mancanti. Bisogna progettare il DR tenendo conto di queste relazioni, creando gruppi coerenti o strategie di riconciliazione post-recovery.

In sintesi, un piano di disaster recovery efficace non è una lista di tecnologie, ma un equilibrio tra analisi di business, automazione, gestione del rischio, test e consapevolezza organizzativa.

Il DR perfetto forse non esiste, ma quello realistico sì — ed è quello che ti permette di dormire la notte.
