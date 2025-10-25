Bentornati a Info Sec. Unplugged. Dopo un paio di mesi di pausa, abbiamo deciso di ripartire raccontando un evento che abbiamo organizzato con NTS, l'azienda per cui lavoriamo, dedicato alla sicurezza in ambito industriale. È stata una tavola rotonda ristretta, nata dal bisogno di un cliente di confrontarsi con altre realtà su come gestire la sicurezza OT.

Vogliamo condividere con voi i temi principali che sono emersi, perché riflettono problematiche comuni a moltissime aziende.

Abbiamo strutturato l’incontro intorno a quattro grandi “obiezioni”, cioè i dubbi e i freni più frequenti che incontriamo quando si parla di sicurezza nel mondo OT — l’Operation Technology. È stato interessante notare come, pur provenendo da settori diversi — oil & gas, energia, automotive, manifattura — i problemi fossero pressoché identici.

### 1. L’infrastruttura è sicura perché non espone servizi

È una convinzione molto diffusa tra i tecnici OT. Si tende a pensare che, se un sistema non espone servizi verso l’esterno, allora non possa essere attaccato. In realtà, abbiamo chiarito che il concetto di “servizio” nell’IT ha un significato più ampio: qualsiasi software che risponde su una porta di rete rappresenta potenzialmente una superficie d’attacco, anche se non viene utilizzato da un client.
Spesso il primo ostacolo è proprio linguistico: dobbiamo imparare a parlare la stessa lingua tra mondo IT e mondo OT.

Un altro tema cruciale è quello dei protocolli. In ambito OT si usano protocolli come Modbus o DNP3, nati in epoca pre-Ethernet e progettati senza meccanismi di sicurezza. Oggi molti impianti li utilizzano ancora in chiaro, senza cifratura né autenticazione, per motivi di semplicità o compatibilità. Questo li rende vulnerabili ad attacchi man-in-the-middle, capaci persino di modificare in tempo reale i comandi inviati ai macchinari.

Abbiamo fatto l’esempio di un braccio meccanico che dovrebbe ruotare di 90 gradi: se un attaccante intercetta e altera il pacchetto, potrebbe farlo ruotare di 95, con conseguenze anche fisiche.

Il problema nasce dal fatto che in passato la sicurezza era “fisica”: un cavo seriale chiuso in un impianto era considerato affidabile. Portando tutto su Ethernet e su IP, quelle assunzioni di fiducia non valgono più.

### 2. L’accessibilità delle workstation OT

Nel mondo industriale, le workstation devono essere facilmente accessibili a operatori e manutentori. Questo però genera vulnerabilità enormi: postazioni senza password, login automatici, porte USB abilitate, sistemi non aggiornati.

La convivenza tra esigenze operative e requisiti di sicurezza è complicata. Le policy classiche dell’IT, come il blocco automatico dopo pochi minuti, risultano inapplicabili in contesti produttivi dove un login potrebbe rallentare un intervento critico.

In molti casi, queste workstation sono ancora basate su Windows XP o Windows 7, fuori supporto, e spesso appartenenti a un dominio Active Directory. Se l’utente è anche amministratore locale, il rischio diventa altissimo.
In più, gli strumenti di detection (come gli EDR) raramente sono installabili per limiti imposti dal costruttore. Ci ritroviamo quindi con macchine vulnerabili, esposte e invisibili.

Una soluzione praticabile è segmentare le reti, isolando l’OT dall’IT, e valutare la possibilità di mantenere le workstation OT fuori dominio, gestendole in modo autonomo. Non è l’approccio perfetto, ma riduce la superficie d’attacco e il rischio di propagazione in caso di compromissione.

### 3. La manutenzione remota non deve essere ostacolata

È un tema esploso dopo il COVID, con la normalizzazione degli accessi remoti. Quasi tutti gli impianti oggi hanno connessioni VPN o canali di telemetria costanti verso casa madre o integratori.

Il problema è che spesso queste connessioni sono Always-On, gestite da fornitori che non hanno competenze di sicurezza. Sono documentati casi in cui dispositivi di produzione venivano usati come demo per altri clienti, o in cui un fornitore compromesso da un malware ha propagato l’infezione a diversi clienti — il classico supply chain attack.

A complicare le cose, troviamo accessi remoti improvvisati con strumenti come TeamViewer o AnyConnect, a volte scaricati da fonti non ufficiali e infettati da spyware o trojan.

La telemetria verso l’esterno è utile se gestita correttamente e contrattualizzata, ma può rappresentare un rischio di data leakage, anche di proprietà intellettuali.

Inoltre, le reti industriali sono spesso configurate come un’unica grande rete che contiene OT, IoT e building automation, con pochi controlli di isolamento. Quando un attaccante entra da una VPN o da un gateway 4G, può muoversi liberamente.

### 4. Ogni change può compromettere l’impianto

È la paura più radicata nel mondo OT: il timore che ogni aggiornamento, patch o modifica possa bloccare la produzione. Questo porta molti impianti a rimanere immutati per decenni, con software obsoleti e vulnerabilità note.

Abbiamo visto casi in cui i bandi di gara prevedevano piani di aggiornamento che poi, nei fatti, non venivano applicati perché “meglio non toccare nulla”.

Sappiamo che patchare tutto è impossibile, ma possiamo gestire il rischio con strategie più ampie: aumentare la visibilità, censire i dispositivi e le vulnerabilità, comprendere chi parla con chi e tramite quali protocolli. Oggi esistono tecnologie che permettono di suddividere una rete industriale in zone di sicurezza isolate, riducendo l’impatto di un’eventuale compromissione.

L’incident management nel mondo OT deve essere adattato: non possiamo applicare gli stessi tempi e strumenti dell’IT. Se in IT ci si muove per ridurre il tempo di esposizione a poche ore, nel mondo OT un patching di 6-10 mesi è la norma — ma è chiaramente insufficiente. Servono quindi misure compensative, come monitoraggio passivo e controlli di rete dedicati.

### Conclusioni

La discussione si è chiusa su tre direttrici principali:

Visibilità: sapere cosa abbiamo, dove si trova e come comunica.

Gestione degli accessi remoti: deve esistere, ma in modo controllato e sicuro.

Detection alternativa: se non possiamo installare EDR, possiamo usare honeypot o sistemi canary per individuare anomalie nella rete.

In definitiva, non possiamo pensare a una convergenza totale tra IT e OT: ci sono ambiti in cui ha senso, come nelle infrastrutture di rete, e altri in cui le logiche rimarranno necessariamente diverse.
L’obiettivo non è eliminare il rischio, ma ridurlo in modo consapevole e sostenibile nel tempo.
