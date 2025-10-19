Bentornati in Info Sec. Unplugged!

Oggi riflettiamo insieme su un tema che incontriamo spesso nelle nostre attività professionali: il disaster recovery e la sua applicazione in caso di incidenti di sicurezza informatica.

Negli ultimi anni abbiamo notato come molte aziende abbiano iniziato ad ampliare le proprie politiche di disaster recovery includendo anche gli eventi legati a compromissioni dovute ad attacchi informatici. È una tendenza comprensibile: ci si accorge che un piano pensato per guasti fisici o errori tecnici non è sufficiente quando l’origine del disastro è un attacco cyber.

Il caso classico è quello di un’azienda che ha una buona infrastruttura di DR, testata, funzionante, pronta a subentrare se il sito primario va giù. Ma se il sito primario viene compromesso da un ransomware o da un attacco mirato, come si fa a ripartire? Possiamo davvero usare la stessa infrastruttura di DR per tornare operativi in tempi accettabili?

La risposta che spesso sentiamo è: “Certo, abbiamo le repliche nel sito secondario.”

Ma quanto possiamo fidarci di quelle repliche? Se non sappiamo da quando la compromissione è iniziata, chi ci garantisce che il dato replicato non sia già infetto?

Molti rispondono: “Abbiamo sistemi immutabili.” Ma “immutabile” non significa “pulito”: significa solo che ciò che è scritto non può più essere modificato, non che non fosse già compromesso all’origine.

E qui emergono altre questioni. Quante volte abbiamo visto politiche di DR formalmente esistenti ma mai testate davvero? E quante volte l’infrastruttura di DR condivide con quella di produzione elementi critici, come il password manager o la directory di autenticazione? Sempre più spesso vediamo qualche miglioramento – ad esempio autenticazioni separate per DR e produzione – ma restano ancora tanti punti in comune che mettono a rischio la reale separazione dei due ambienti.

Durante i nostri tabletop exercise – che in poche ore riescono spesso a “smontare” progetti di DR apparentemente solidi – vediamo chiaramente quanto la separazione tra i due siti sia più teorica che effettiva. Il requisito minimo, lo ricordiamo sempre, è la separazione fisica o logica, ma in modo che i due ambienti non comunichino liberamente.

Un esempio lampante riguarda il piano di DR stesso: spesso è salvato su SharePoint, con dentro – incredibilmente – le password dei sistemi di DR. Così, se un utente compromesso accede a quello SharePoint, ottiene le chiavi per tutto. È un errore frequente, eppure comune.

In generale, tutto questo riporta a un tema centrale: la disciplina operativa. La sicurezza richiede rigore e progettazione, non soluzioni “a pezza”.

Gli attacchi ransomware, ad esempio, ci hanno mostrato la fragilità delle nostre infrastrutture: se il sistema di virtualizzazione viene compromesso, anche il DR può essere inutilizzabile. Da qui nascono domande fondamentali: abbiamo almeno qualche PC “pulito” in armadio da cui ripartire? Sappiamo distinguere quando possiamo procedere con un recovery e quando, invece, dobbiamo ricostruire da zero?

E poi arriva la realtà dei dati. Ci sono aziende che tengono archivi enormi, anche di dati obsoleti. È difficile trovare qualcuno disposto ad autorizzare cancellazioni. Ma questi dati diventano un rischio: li vediamo spuntare in backup dimenticati, spesso contenenti informazioni sensibili o personali che non dovrebbero più esistere.

L’esempio classico: vecchi backup di workstation non cifrati, dove si trovano credenziali cached e token di autenticazione. È un disastro annunciato, eppure frequente.

Quando parliamo di DR, torniamo sempre alle domande base:

- Perché esiste? Per rispondere a quali eventi?
- Quali dati devono sopravvivere e per quanto tempo?

Spesso il DR nasce per gestire guasti o errori umani, ma oggi deve affrontare anche attacchi sofisticati. E questo cambia tutto.

Il vero nodo è la definizione del punto di ripristino: quanto è accettabile perdere? Un giorno di dati? Una settimana? Questa riflessione – tipica della Business Impact Analysis – deve essere fatta a mente lucida, prima del disastro.

Serve una strategia a più livelli:

- mantenere versioni “immutabili” per proteggere i dati;
- gestire con cura la retention e il versioning;
- e, quando possibile, costruire golden image dei sistemi operativi, da cui ripartire in modo pulito.

Questo concetto si sposa con l’automazione e con l’approccio Infrastructure as Code: poter rigenerare un sistema operativo da zero, in modo automatizzato, è un vantaggio enorme. Permette di ripartire rapidamente e con certezza di integrità, riducendo il rischio di portarsi dietro una compromissione.

È chiaro che non tutto può essere automatizzato: alcuni sistemi, come Active Directory, richiedono ancora competenze specifiche e interventi manuali. Ma l’obiettivo deve essere muoversi verso infrastrutture ricostruibili, non solo “ripristinabili”.

In fondo, è quello che hanno fatto realtà come Debian o Red Hat dopo la scoperta di compromissioni nella supply chain: hanno buttato tutto e ricostruito da zero, grazie a processi automatizzati di build. È un esempio potente, che mostra come la resilienza passi anche dalla capacità di rifare tutto rapidamente e bene.

E allora, nella prossima puntata, vogliamo approfondire proprio questo: come si costruisce un piano di DR efficace oggi, e come può evolvere in un “DR mitologico” basato su automazione e immutabilità.
Perché, alla fine, il disaster recovery non è solo una procedura: è una filosofia di progettazione, che si misura nel momento peggiore — e distingue chi riesce davvero a rialzarsi da chi resta bloccato tra le macerie digitali.

Un saluto a tutti i colleghi che, almeno una volta nella vita, hanno vissuto un disaster recovery e ne sono usciti da eroi. Ci aggiorniamo alla prossima.
