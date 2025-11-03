Bentornati a Info Sec. Unplugged in versione Extended.

Oggi vogliamo parlare di attacchi DDoS. In questa puntata condividiamo due casi interessanti, uno vissuto in prima persona e uno studiato, per poi riflettere insieme sull’impatto e sulla gestione di questo tipo di minacce.

Per chi non lo sapesse, un DDoS – Distributed Denial of Service – è un attacco che punta a rendere inutilizzabile un servizio informatico sfruttando fonti distribuite nel mondo. Può essere di due tipi: volumetrico, quando l’obiettivo è saturare la banda di rete, oppure applicativo, quando si sovraccaricano le risorse del server con un numero eccessivo di richieste.

Il primo caso che raccontiamo è un attacco volumetrico mirato direttamente all’indirizzo IP di un router di frontiera. Ci ha colpiti perché di solito gli attacchi DDoS prendono di mira un servizio applicativo, non un’infrastruttura di rete. In quei casi si possono adottare contromisure come i servizi cloud che “filtrano” il traffico — i cosiddetti traffic scrubbing services — restituendo al server finale solo traffico pulito.

Ma quando il bersaglio è un indirizzo di rete che sostiene la connettività stessa, non è possibile spostarlo altrove. In quel caso l’unica soluzione è stata coinvolgere direttamente il provider, che ha attivato un servizio anti-DDoS e ha risolto la situazione.

Il secondo episodio è il famoso attacco a Eurobet del 2019. Un caso peculiare: una serie di attacchi DDoS di piccola entità lanciati in diverse aree d’Italia, in cui la sorgente apparente dei pacchetti era proprio Eurobet. Poiché la sorgente era costante, molti provider, per difendersi, finirono per bloccare gli indirizzi IP di Eurobet stessa, escludendola di fatto dalla rete.

Un attacco indiretto, forse addirittura un sabotaggio. Non ci sono certezze sulle motivazioni, ma l’effetto è stato notevole: un’interruzione di servizio che ha compromesso la disponibilità e la reputazione dell’azienda.

Questi esempi ci fanno riflettere su quanto gli attacchi DDoS possano influenzare la fiducia dei clienti e la percezione di affidabilità di un fornitore di servizi digitali. Settori come e-commerce, finanza e cloud sono particolarmente vulnerabili, perché la disponibilità del servizio coincide con la loro stessa operatività.

Abbiamo poi ragionato su come valutare il rischio. Non esiste un framework unico dedicato ai DDoS, ma dal punto di vista network dobbiamo considerare che ogni punto esposto a Internet — dal router al firewall fino ai servizi pubblici — è potenzialmente un target.

Gli attacchi volumetrici colpiscono la banda, quelli applicativi le risorse computazionali. Oggi saturare anche connessioni da 10 Gbps è possibile con costi contenuti, quindi il rischio è tutt’altro che teorico.

Sul fronte della mitigazione, la prima risposta rimane sempre la prontezza operativa: sapere a chi rivolgersi, avere un contatto diretto con il provider, e — meglio ancora — un contratto preventivo che preveda la possibilità di attivare rapidamente un servizio anti-DDoS.

Tra le strategie di prevenzione, la segmentazione della rete e il monitoraggio proattivo del traffico sono fondamentali. Tuttavia, la detection non è sempre immediata: un attacco applicativo può passare inosservato se non si osservano anomalie evidenti nella banda o nella CPU. Anche parametri come i timer di rete possono essere sfruttati per mantenere connessioni “sospese” a basso costo, saturando i limiti di sessione del server senza apparenti picchi di traffico.

Gli attacchi evolvono: oggi non solo si possono creare DDoS più potenti, ma anche più intelligenti, progettati per eludere la detection o, al contrario, per generare rumore di copertura. Infatti, un DDoS può essere usato come diversivo, per distrarre i team di sicurezza mentre in parallelo si compiono altre azioni, come esfiltrazioni di dati o campagne di phishing mirato.

Questo scenario richiede un cambio di prospettiva. Serve formazione trasversale, non solo per i team tecnici (blue e red team), ma anche per chi si occupa di comunicazione e gestione crisi.

Occorrono simulazioni realistiche — veri e propri esercizi di red teaming — che permettano di testare la risposta aziendale a incidenti complessi, non limitandosi a un penetration test tradizionale.

Purtroppo, nella pratica aziendale, il piano di risposta agli incidenti esiste raramente o, quando esiste, viene poco testato. Anche gli scenari di DDoS sono spesso ignorati perché considerati troppo rischiosi da simulare. Tuttavia, per comprendere davvero l’impatto e migliorare la resilienza, bisogna affrontare anche questi test in modo controllato.

Concludiamo quindi questa puntata con una riflessione: la sicurezza non può limitarsi alla tecnologia, ma deve includere consapevolezza, preparazione e collaborazione.

Ne parleremo ancora, magari in una puntata dedicata alla formazione e alla cultura della sicurezza.

A presto e grazie per averci ascoltato in questa puntata “on the road” di Info Sec. Unplugged.
