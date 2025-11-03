Siamo partiti dalla nostra esperienza diretta sul campo, come team NTS impegnato in attività offensive di sicurezza informatica. Chi lavora in questo settore lo sa bene: quando parliamo di attività offensive, intendiamo tutte quelle azioni che servono a verificare la tenuta complessiva di un’azienda di fronte a un attacco cyber — non solo in termini di prevenzione, ma anche di rilevamento e gestione. Non possiamo illuderci di bloccare tutti gli incidenti, e da questa consapevolezza nasce la riflessione che condividiamo oggi.

Nel nostro lavoro abbiamo incontrato organizzazioni di ogni tipo — pubbliche amministrazioni, banche, aziende manifatturiere, GDO — ma, nonostante le differenze, i problemi fondamentali restano spesso gli stessi. Abbiamo deciso di concentrarci su due temi che ricorrono costantemente: la gestione delle vulnerabilità e le debolezze strutturali delle infrastrutture.

Tutte le aziende di grandi dimensioni hanno un processo di Vulnerability Management: censiscono, misurano e classificano le vulnerabilità, poi pianificano attività di remediation. Ma il numero di vulnerabilità rilevate è enorme: centinaia di casi, tutti classificati come urgenti. Il risultato è un conflitto tra sicurezza e operatività — patch da installare in 48 ore, ma sistemi come SAP o la produzione che non si possono fermare.

Abbiamo capito che il problema non è tanto l’effort, quanto la prioritizzazione. Basarsi solo su “severity” e “impatto sul business” non basta. Oggi bisogna considerare anche il contesto d’attacco: quanto è realmente sfruttabile quella vulnerabilità, tenendo conto delle difese già presenti (EDR, firewall, detection di rete, SOC, ecc.).

Quando abbiamo applicato questo metodo, il numero di vulnerabilità davvero critiche è passato da centinaia a poche unità. E questo ha cambiato radicalmente la gestione operativa: tre o quattro sistemi da patchare in modo mirato, invece di cento interventi indistinti. Senza questo approccio, si rischia di lasciare scoperte le aree più importanti semplicemente perché “non si fa in tempo”.

Il secondo tema è strettamente collegato: la fragilità strutturale delle infrastrutture. Quasi mai partiamo da zero: ereditiamo reti costruite da altri, spesso stratificate nel tempo. Si riconoscono veri e propri “strati geologici” di tecnologie, con logiche di design che risalgono a vent’anni fa.

Un esempio classico è quello delle reti MPLS: soluzioni efficaci in passato, ma che oggi offrono troppo spazio di manovra a un attaccante se non sono adeguatamente segmentate e controllate. In contesti come la GDO, con centinaia di negozi, il rischio cresce in modo esponenziale. Per ovviare, molte aziende hanno introdotto firewall distribuiti per ottenere visibilità e contenimento, ma questo comporta nuovi oneri di gestione e manutenzione.

Abbiamo notato lo stesso fenomeno anche nei sistemi wireless o nei network campus: molte implementazioni, considerate sicure dieci o quindici anni fa, oggi non reggono più il confronto con gli attacchi moderni. È quindi necessario rivedere i design, perché più strumenti di controllo e detection abbiamo — EDR, SIEM, Network Detection — meglio possiamo comprendere se un attack path verso una vulnerabilità è effettivamente possibile.

Ragionando sulle cause di questa situazione, abbiamo individuato tre fattori principali: complessità, competenze e governance.

Le infrastrutture sono diventate complesse: network overlay, SD-WAN, container, firewall multifunzione... tutto si mescola. Le competenze che un tempo bastavano oggi non sono più sufficienti. Chi configura un firewall, per esempio, non si limita più a gestire ACL e porte, ma deve comprendere IPS, DNS filtering, routing, applicazioni e protocolli.

Il problema non è solo tecnico ma anche economico: molte aziende sfruttano solo una piccola parte del potenziale delle tecnologie che hanno acquistato, spesso per mancanza di tuning o di design adeguato. Serve una visione trasversale che unisca rete, sicurezza e business.

E poi c’è la governance: il processo di gestione della sicurezza deve avere dignità aziendale. Se manca un processo riconosciuto, anche le patch più urgenti restano ferme per paura di impattare la produzione. Nessuno vuole “toccare SAP” e rischiare rallentamenti, e così la vulnerabilità rimane aperta.

Un altro tema cruciale è quello della scelta tra make e buy. Non tutte le aziende devono fare tutto internamente: dipende da quanto la componente IT è parte integrante del business. Alcune realtà, soprattutto i grandi gruppi industriali, riescono a sviluppare internamente processi e competenze e poi a riutilizzarli in più aziende del gruppo.

Ma per altre, costruire internamente team offensivi o di defense non ha senso: richiede skill rare, che non servono ogni giorno, e trattenere talenti in aziende non tecnologiche è quasi impossibile. In questi casi, esternalizzare — totalmente o in parte — è la scelta più logica.

Il principio guida è mantenere la verticalità: chiedere supporto specialistico per design e implementazione, ma mantenere la visione d’insieme e la responsabilità strategica. Le soluzioni ci sono, ma devono essere gestite e personalizzate. Un EDR “out of the box” non basta se nessuno lo monitora, e un SIEM pieno di log è inutile se nessuno fa threat hunting.

In definitiva, la nostra esperienza ci ha insegnato che la sicurezza non è una questione di strumenti, ma di processo, consapevolezza e priorità. Serve una governance solida, un disegno coerente e competenze che sappiano collegare i pezzi. Solo così possiamo davvero rendere le infrastrutture più sicure, ridurre l’esposizione e trasformare la complessità in valore.
