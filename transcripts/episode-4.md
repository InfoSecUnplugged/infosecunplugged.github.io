Perfetto 👍
Ecco il risultato richiesto, basato sulla trascrizione che hai fornito.

---

## Trascrizione rielaborata – “Info Sec. Unplugged”

In questa puntata abbiamo deciso di concentrarci su un tema cruciale per la sicurezza informatica: la gestione e l’efficacia degli EDR (Endpoint Detection and Response). Ci siamo chiesti cosa succede quando la tecnologia non è presidiata, quando le policy non sono configurate correttamente, e come possiamo verificare se il nostro setup è davvero adeguato al livello di minaccia attuale.

Abbiamo iniziato parlando del presidio delle tecnologie. Se non presidiamo l’EDR, una minaccia rilevata in detection può passare inosservata. Una serie di eventi anomali, che dovrebbero attivare l’attenzione, rischiano di non essere viste da nessuno. Anche le minacce bloccate, se non vengono monitorate e analizzate nel tempo, possono evolversi e riuscire a eludere i controlli. In questi casi capita di trovarsi con infezioni latenti che restano silenti fino a quando, per qualche ragione, non riescono a propagarsi e causare danni.

Abbiamo osservato come il comportamento di tanti applicativi legittimi – agenti di monitoraggio, software di licenza, sistemi di reporting – sia molto simile a quello dei malware. Fanno chiamate esterne, ricevono istruzioni, si comportano come veri e propri “command and control” legittimi. Questo crea ambiguità nei sistemi di detection: un comportamento che in un contesto è malevolo, in un altro può essere perfettamente normale. È bastato, ad esempio, cambiare il sito di destinazione di una connessione — da Pastebin a Dropbox — per far sì che un EDR non segnalasse più l’allarme, pur essendo identico il comportamento di rete.

Da qui emerge un concetto fondamentale: il presidio non è facoltativo. Non basta configurare un EDR e lasciarlo lavorare. Serve una presenza costante, continua, che osservi, affini e adatti lo strumento. Il presidio h24 non è sempre necessario per ogni azienda, ma deve essere una decisione consapevole e ponderata sul rischio e sul costo.

Quando le policy sono troppo larghe o troppo strette, i problemi cambiano ma restano gravi. Una configurazione errata può generare falsi positivi infiniti o, al contrario, lasciare scoperte importanti. È quindi essenziale verificare periodicamente l’efficacia del sistema. Il modo migliore è attraverso test reali: simulazioni di attacco, esercitazioni controllate, red teaming o adversary simulation. Solo così possiamo capire non solo come reagisce la tecnologia, ma anche come risponde il team che la gestisce. Testare la tecnologia significa testare anche le persone e i processi.

Abbiamo anche discusso dei due approcci ai test: quelli automatici e quelli manuali. I test automatici hanno il vantaggio di essere rapidi e continui: lanciano centinaia di attacchi reali del passato e misurano l’efficacia delle policy. Tuttavia, i malware cambiano e i command & control di anni fa non esistono più, quindi servono anche simulazioni artigianali, manuali, costruite da persone che conoscono il contesto del cliente e cercano di aggirare l’EDR in modo realistico. L’uno non sostituisce l’altro: sono complementari.

Poi ci siamo chiesti come scegliere una tecnologia EDR. Non basta guardare chi è nel quadrante in alto a destra di Gartner. Certo, è un punto di partenza, ma esistono anche soluzioni meno note che fanno un ottimo lavoro. L’EDR è l’ultimo paracadute dell’azienda: entra in gioco quando un malware è già arrivato sull’endpoint. Per questo scegliere soluzioni volutamente “meno aggressive” solo per evitare falsi positivi può essere pericoloso. Meglio gestire il rumore che ignorare le minacce.

Abbiamo riflettuto su come ogni contesto aziendale sia diverso. Ci sono endpoint mobili, server, sistemi industriali OT su cui non è possibile installare agenti EDR. Tuttavia, è improbabile che un’azienda scelga più piattaforme diverse per coprire ogni scenario. La piattaforma sarà una sola, ma con policy differenziate.

Nel processo decisionale, due fattori sono fondamentali. Il primo è l’integrazione: la soluzione deve dialogare con il resto dell’ecosistema IT e di sicurezza. Se continuiamo a ragionare per silos, ci ritroviamo con quattordici console da gestire e nessuna visione unificata. Il secondo è la usabilità: se una piattaforma è difficile da usare, resterà spenta o sottoutilizzata. Un EDR va scelto anche per la sua capacità di essere compreso e utilizzato con efficacia da chi lo gestisce.

Un altro elemento che abbiamo messo sul tavolo riguarda il vendor: oggi molti produttori di EDR si sono dotati di team di incident response e di threat intelligence. È un vantaggio concreto: avere dietro un team che non solo sviluppa la tecnologia, ma gestisce incidenti e raccoglie intelligence in tempo reale, migliora la qualità e la rapidità delle difese. Anche quando si delega la gestione a un servizio MDR esterno, non significa “dimenticarsene”: la verifica deve comunque essere continua e contestualizzata.

Alla fine ci siamo resi conto che le piattaforme EDR non sono solo strumenti tecnologici, ma parte di un ecosistema complesso che include processi, persone e conoscenza. E proprio per questo motivo, nella prossima puntata, vogliamo parlare di XDR – l’evoluzione naturale dell’EDR – e del tema dell’evasion, cioè di come gli attaccanti riescono a eludere anche i sistemi più avanzati. Sono due argomenti vasti, ma fondamentali per capire dove sta andando davvero la sicurezza moderna.
