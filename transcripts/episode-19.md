Siamo tornati negli uffici di Verona, pronti a riprendere il nostro viaggio nel mondo dell’IT. Dopo aver parlato del network a livello campus, oggi vogliamo affrontare in modo più tecnico il tema del data center network, concentrandoci su come progettarlo e mantenerlo sicuro e resiliente.

Nel data center tutto ruota intorno all’affidabilità: quella rete non può mai fermarsi. A differenza del campus, qui la ridondanza è fondamentale. Parliamo di ambienti che ospitano servizi critici, dove anche una minima interruzione può avere impatti pesanti. Ovviamente la scala conta: tra un piccolo data center aziendale e una grande infrastruttura enterprise cambiano sia le scelte architetturali sia gli investimenti.

Molte realtà più piccole preferiscono oggi esternalizzare – in hosting o nel cloud – parte delle loro infrastrutture. Tuttavia, capire le logiche di design di un data center “classico” aiuta comunque a prendere decisioni consapevoli anche nel mondo ibrido o cloud.
E in questo senso, tutto quello che si applica a un data center on-premise deve essere “tradotto” nella lingua dell’hyperscaler.

Partiamo da uno dei cuori del data center: lo storage.

Nel mondo enterprise, lo storage su IP è ormai lo standard, con protocolli come NFS, iSCSI e in passato Fiber Channel over Ethernet (FCoE). Quest’ultimo oggi è quasi scomparso, soppiantato da soluzioni più semplici da gestire.
La differenza principale tra i protocolli sta nel modo in cui gestiscono affidabilità e latenza. Lo SCASI, ad esempio, è un protocollo storico che non tollera perdite di pacchetti: deve arrivare tutto, e deve arrivare integro. Ethernet, invece, nasce con una logica diversa, in cui qualche perdita è accettabile e gestita con ritrasmissioni. È chiaro quindi che far viaggiare SCASI su Ethernet può generare problemi di corruzione dei dati o crash di macchine virtuali se non si disegna la rete nel modo corretto.

Nel tempo, la complessità del Fiber Channel e i suoi costi hanno spinto molti a cercare alternative. Tuttavia, chi ha lavorato con questo protocollo sa quanto fosse affascinante: affidabilità totale, due reti parallele (le famose “fabric A” e “fabric B”), e una rigidissima certificazione di compatibilità tra tutti i componenti, dal firmware della scheda di rete all’hypervisor.

Quando si è deciso di spostare tutto su Ethernet, è iniziata una fase di semplificazione, ma anche di confusione. Molti network engineer hanno trattato i protocolli storage come normali protocolli IP, senza considerare le esigenze particolari di latenza e perdita zero. Il risultato? Dati corrotti, macchine bloccate e tante ore di troubleshooting – spesso per banalità come l’MTU sbagliato su una porta di rete.

Un’altra grande rivoluzione è stata l’introduzione di NFS come protocollo di comunicazione tra host e storage. NFS ha portato flessibilità, ma anche prestazioni molto variabili, soprattutto in presenza di carichi eterogenei. Alcuni vendor, come NetApp, hanno saputo implementarlo in modo eccellente; altri invece hanno proposto soluzioni improvvisate e lente.

Interessante notare come il ritorno del Fiber Channel in alcuni contesti moderni (soprattutto con l’arrivo degli SSD e NVMe) dimostri che certe architetture, per quanto complesse, offrono ancora prestazioni ineguagliabili.

Tra i design moderni c’è anche il concetto di converged storage, spesso mal interpretato: non significa mettere tutto nello stesso switch, ma adottare un’architettura in cui rete dati e rete storage condividono apparati pensati per gestire entrambe le funzioni, con le dovute garanzie di QoS e latenza.

Il tentativo di unire Ethernet e Fiber Channel in un unico protocollo, il FCoE, è stato interessante, ma la complessità lo ha condannato. Ha avuto un certo successo in ambiti ristretti – come i blade chassis – ma poco oltre.

Proprio i blade server meritano una riflessione: erano nati per offrire densità e scalabilità, ma nel tempo molti vendor hanno tradito la promessa di compatibilità tra generazioni di chassis e lame. In alcuni casi i clienti hanno abbandonato la tecnologia, preferendo tornare ai classici rack server. Oggi, con la densità di CPU e RAM raggiunta dai server moderni, questa scelta è spesso più sensata e flessibile.

Un errore ricorrente nel design dei data center è quello di non pianificare l’evoluzione nel tempo. Quando progettiamo un’infrastruttura dovremmo già sapere come la dismetteremo o come la espanderemo. Definire fin dall’inizio la “data di fine vita” di un asset, come fanno poche organizzazioni, aiuterebbe a gestire gli investimenti in modo più sano e prevedibile.

Venendo al tema sicurezza, oggi ogni rete o “zona di sicurezza” nel data center ha tipicamente un firewall come gateway. È una scelta logica e gestibile: centralizza le policy, garantisce visibilità e facilita l’analisi.

Tuttavia, dobbiamo accettare che alcune reti possano esistere solo a livello 2, senza routing, se hanno bisogno di comunicare solo internamente. Meno complessità, meno rischi.

Dal punto di vista offensivo, invece, lo scenario cambia: gli attaccanti sfruttano sempre più spesso il lateral movement, spostandosi all’interno della rete una volta compromessa una postazione utente.

La catena tipica parte dall’infezione di un endpoint client, dove il malware stabilisce comunicazione verso l’esterno, spesso indisturbato da regole firewall troppo permissive. Da lì l’attaccante esplora la rete, alla ricerca di file server, sistemi di backup, hypervisor o altri obiettivi sensibili.

In reti poco segmentate, questi movimenti laterali sono ancora oggi troppo facili.

Spesso il problema sta proprio nel design: reti client e reti server mal separate, con regole di accesso eccessivamente ampie. Un esempio classico sono le condivisioni file (le “share” SMB o CIFS), accessibili da troppe postazioni. È lì che gli attacker trovano password in chiaro, file di configurazione, firmware caricati da fornitori esterni, e altre minacce dormienti.

La gestione degli spazi condivisi è una delle aree più critiche e sottovalutate della sicurezza aziendale. Forse è il momento di ripensare del tutto il concetto di “file server”, come suggerivamo tempo fa: forse andrebbe sostituito da strumenti di collaborazione più moderni, che creino spazi temporanei e li eliminino quando non servono più.

Il problema è che nella realtà “non si cancella mai nulla” – e proprio in quella sporcizia gli attaccanti prosperano.

Guardando avanti, vediamo due direzioni principali.

La prima è la micro-segmentazione: suddividere i server in piccoli gruppi isolati, limitando la possibilità di movimento laterale. Esistono già tecnologie che lo permettono, ma oggi hanno ancora costi e complessità elevate.

La seconda è l’evoluzione del ruolo del firewall: da unico gateway centrale a un modello ibrido o distribuito, magari con funzioni di sicurezza direttamente sulle porte dello switch fisico o virtuale.

Sarà interessante osservare questa evoluzione nei prossimi anni e capire se la micro-segmentazione riuscirà davvero a diventare sostenibile, sia tecnicamente che economicamente.
