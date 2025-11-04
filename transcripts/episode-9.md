Bentornati a tutti a Info Sec. Unplugged!

Oggi vogliamo parlare di un tema che ci appassiona entrambi: cosa può fare un attaccante una volta che riesce a introdurre fisicamente un dispositivo in una rete target.

Ci immaginiamo la classica situazione in cui, per qualche motivo, un dispositivo viene collegato a una porta Ethernet libera — una di quelle che, per sbaglio o per superficialità, è attiva e magari non protetta da 802.1X. Da lì, l’obiettivo dell’attaccante è chiaro: capire dove si trova, come configurarsi, e soprattutto come muoversi in rete nel modo più silenzioso possibile.

Quando ci troviamo in questo contesto, i nostri primi passi sono quasi sempre gli stessi: osserviamo il traffico locale, tentiamo qualche ARP scan per individuare gli host nel dominio di broadcast e, appena possibile, cerchiamo di identificare il gateway. Anche senza un indirizzo IP, si possono ottenere informazioni preziose — basta un po’ di intuito, qualche tentativo e un po’ di analisi a livello 2.

Uno dei metodi più semplici è partire dall’ARP: è veloce, di solito passa inosservato, e ci permette di mappare rapidamente i dispositivi attivi sulla rete locale. Tuttavia, se vogliamo spingerci oltre, dobbiamo trovare una via verso Internet o verso subnet più ampie, e lì iniziano le cose interessanti.

Quando si lavora in questo modo, avere un piccolo dispositivo in bridge, trasparente — ad esempio un Raspberry Pi a due porte — può aiutare molto. Inserendolo tra un host e lo switch, possiamo analizzare il traffico che passa, identificare facilmente gateway, comunicazioni, protocolli e pattern di rete. Anche se non possiamo sapere la subnet mask, possiamo dedurla dai comportamenti ARP e dal numero di host attivi, intuendo se si tratta di una /24 o qualcosa di più ampio.

Durante queste attività ci siamo imbattuti in comportamenti curiosi, come il proxy ARP, che in alcuni casi permette la comunicazione anche quando la subnet è configurata male. È una caratteristica di vecchi ambienti Cisco — oggi quasi sempre disabilitata — che, però, spiega perché certi host “funzionano a metà” pur con subnet sbagliate. È un comportamento utile da riconoscere, perché può far credere che tutto sia a posto, mentre sotto la superficie la rete è mal configurata.

Un’altra riflessione che ci facciamo sempre è: che tipo di gateway abbiamo davanti? È un semplice switch layer 3 o un firewall con controllo a livello 4 e oltre?
Lo si può capire da piccoli segnali: se proviamo a connetterci su porte insolite e riceviamo un pacchetto “reset”, probabilmente non c’è un firewall; se invece non riceviamo nulla, il traffico è filtrato. Capirlo presto fa la differenza, perché ci dice quanto possiamo essere rumorosi nelle nostre scansioni successive.

A proposito di rumorosità: un ARP scan è inevitabilmente visibile, ma raramente genera alert reali — pochi sistemi di detection si preoccupano di una manciata di ARP in più. Tuttavia, se il firewall integra un IPS, in teoria potrebbe segnalarlo. Sta all’attaccante capire quanto “osare”.

Una volta individuata la rete e il gateway, possiamo iniziare ad analizzare i protocolli di adiacenza — CDP e LLDP, ad esempio. Spesso questi protocolli ci regalano molte più informazioni di quanto si pensi: hostname dello switch, modello, IP di management, numero di porta, e in alcuni casi persino la VLAN associata. In alcune implementazioni LLDP, infatti, viene comunicato anche il VLAN ID, cosa che torna utilissima per l’autoconfigurazione di un dispositivo inserito in rete.

Da qui nasce l’idea di costruire un sistema che si autoconfigura ascoltando la rete: un piccolo agente che, tramite Scapy o strumenti simili, raccoglie tutto ciò che sente — gateway, DHCP, LLDP, CDP — e, dopo qualche minuto, si autoconfigura in modo coerente, pronto a comunicare verso l’esterno senza farsi notare. È un concetto di automazione “adversarial”, potremmo dire.

Ma la rete fisica riserva sempre delle insidie. Ad esempio, lo spanning tree protocol: se male configurato, può essere manipolato, causando denial of service o cambi di topologia imprevisti. Non è una tecnica utile per raccogliere informazioni, ma sapere che esiste e che può essere abusato è importante. Lo stesso vale per il VTP (VLAN Trunking Protocol): nella versione 2 era tristemente famoso per la sua assenza di controlli — bastava un frame con un revision number più alto per riscrivere il database VLAN dell’intera infrastruttura. Nella versione 3 il problema è risolto, ma nei contesti legacy capita ancora di trovarlo, e lì basta un errore per spegnere una rete intera.

Altri due protocolli “sensibili” sono DTP (Dynamic Trunking Protocol) e Voice VLAN. Entrambi possono essere sfruttati per negoziare una porta come trunk anche se nasce come access: in pratica, un attaccante può convincere lo switch a inviargli traffico di più VLAN, ottenendo così visibilità o accesso a segmenti che dovrebbero essere isolati. Lo stesso meccanismo usato dai telefoni IP per collegarsi alla voice VLAN può essere ingannato simulando un dispositivo VoIP. È un piccolo dettaglio tecnico che, però, apre porte inattese.

Abbiamo anche toccato la tecnica del VLAN hopping, quella che sfrutta frame doppiamente taggati per “saltare” tra VLAN. È una vecchia conoscenza del mondo offensive, ma oggi quasi tutti gli switch moderni hanno contromisure efficaci — e comunque crea un traffico asimmetrico facilmente intercettabile, quindi resta più un esercizio teorico che una reale minaccia.

Infine, ci siamo ricordati di una vecchia tecnica: saturare la MAC Address Table degli switch, costringendoli a comportarsi come hub e inviando pacchetti ovunque. Funziona solo su hardware datato, e comunque causa rallentamenti pesanti e comportamenti anomali — poco utile se l’obiettivo è restare invisibili.

Ricapitolando, tra ARP scan, analisi di protocolli di adiacenza, osservazione passiva del traffico, e qualche tentativo controllato di negoziazione o autoconfigurazione, si può raccogliere una quantità sorprendente di informazioni. Spesso bastano dieci minuti per sapere in che rete siamo, chi ci circonda e dove si trova l’uscita verso Internet.

E se da un lato questa è conoscenza preziosa per chi difende, dall’altro è un promemoria: anche un semplice switch, se non ben configurato, può diventare il miglior alleato di un attaccante.
