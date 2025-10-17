Bentornati a Info Sec. Unplugged!

In questa puntata concludiamo il nostro viaggio dedicato al Disaster Recovery e, più in generale, alla Cyber Recovery. Nelle due parti precedenti abbiamo affrontato la fase di design e pianificazione; ora vogliamo chiudere il cerchio con la parte più operativa e concreta: il testing, l’automazione e tutto ciò che serve per rendere realmente funzionante un piano di DR.

Prima di entrare nel merito, ci è venuta un’idea: vogliamo organizzare una tabletop exercise aperta a chi ci segue, per simulare insieme la gestione di un evento di disaster recovery. L’obiettivo è sperimentare in prima persona cosa significa affrontare una crisi informatica.

Immaginiamo di formare un piccolo gruppo di partecipanti: noi proporremo uno scenario di disastro, assegneremo dei ruoli e costruiremo uno storytelling operativo. Ciascuno, nel proprio ruolo, dovrà prendere decisioni per gestire la situazione di emergenza. Sarà un modo concreto ma sostenibile per mettere in pratica ciò di cui abbiamo parlato, sfruttando gli strumenti di comunicazione remota.

Vorremmo farla verso la fine di novembre, in un giorno feriale, probabilmente nel tardo pomeriggio. Stiamo ancora definendo i dettagli, ma chi è interessato può già contattarci via LinkedIn o email. Appena tutto sarà pronto, comunicheremo le modalità di partecipazione.

Dopo questa anticipazione, possiamo entrare nel vivo della puntata.

Questa volta vogliamo chiudere definitivamente il tema del Disaster Recovery, focalizzandoci sulla parte di testing e automazione, cioè la fase in cui il piano viene messo alla prova.

Nella nostra esperienza, quando si passa dalla teoria alla pratica e si comincia a “mettere le mani” sul sistema, ci si accorge davvero di cosa serve, cosa manca e soprattutto di quali sono le dipendenze tra i vari componenti.

Idealmente, ogni azienda dovrebbe avere un piano che descriva come funzionano tutte le applicazioni e le loro interconnessioni. Nella realtà, però, è rarissimo trovarne uno completo. Il bello – e a volte il dramma – del DR è che, nel momento in cui lo mettiamo in piedi, scopriamo le dipendenze nascoste. E da lì iniziano i test, da ripetere più volte, con pazienza e metodo.

A questo punto entra in gioco l’automazione, che può semplificare enormemente la gestione.

Automatizzare l’avvio dei servizi, delle applicazioni e delle macchine virtuali ci permette di testare il DR più rapidamente e in modo più affidabile. Noi siamo convinti che si debba lavorare di giorno, non di notte: si è più lucidi, si capisce meglio cosa succede e si riducono gli errori.

Per questo crediamo molto nell’idea di costruire un DR che possa essere acceso senza disturbare la produzione, creando una sorta di “bolla” isolata dove far girare tutto.

Certo, oggi con le dipendenze cloud è tutto più complesso, ma la logica resta valida: dobbiamo pensare fin dal design a come provare il sistema, non solo a come costruirlo.

Una bolla di test ci permette di simulare in modo realistico l’accensione di tutto l’ambiente senza rischiare di intaccare la produzione. Inoltre, il testing non è solo una verifica, ma anche un processo di miglioramento continuo: ogni volta scopriamo qualcosa di nuovo. Magari partiamo con 150 servizi e ci accorgiamo che ne servono altri 20.

Durante i test, spesso si danno per scontate alcune cose. Ad esempio, si assume che certi servizi di base – come i domain controller – non debbano mai essere toccati, perché attivi anche sul sito di recovery. Questo porta a trascurare test importanti.
Avere una struttura che permette di accendere tutto in bolla ci costringe a testare davvero ogni componente, anche quelle che di solito vengono ignorate.

Un altro punto cruciale è la sequenza di avvio dei servizi. In teoria, un’applicazione ben scritta dovrebbe essere in grado di partire e attendere che le sue dipendenze siano disponibili. In pratica, sappiamo che non è così: se il database non è attivo, l’applicazione spesso non si avvia. Ecco perché è fondamentale che il sistema automatico sappia accendere tutto nell’ordine giusto, verificando che ogni servizio sia realmente funzionante prima di passare al successivo.

Un buon sistema di automazione ha anche un vantaggio collaterale: si autodocumenta. Invece di gestire manualmente centinaia di comandi e procedure scritte in documenti infiniti, basta premere un pulsante: dopo un’ora o due l’ambiente è pronto.
Inoltre, automatizzare rende il DR più accessibile e ripetibile: chiunque può farlo seguendo la procedura, non serve più un “sacerdote” del sistema.

Ci è capitato, di recente, di lavorare su un ambiente SAP: la parte di avvio era semplice e veloce, ma la riconfigurazione di SAP richiedeva giorni di lavoro e un documento di 70 pagine. Non ci eravamo mai resi conto di quanto potesse essere complesso riattivare un’infrastruttura di quel tipo. È un esempio chiaro di come il disaster recovery applicativo possa essere molto più impegnativo di quello infrastrutturale.

Lo stesso vale per certe applicazioni basate su Oracle. In un progetto con oltre 3000 macchine virtuali, lo startup infrastrutturale richiedeva circa due ore. Poi subentrava il team applicativo, che impiegava dalle sei alle otto ore per fare tuning e configurazioni. A volte cambiava un dominio, altre volte un nome host, e tutto andava adattato. Ci siamo resi conto che, per quanto la parte infrastrutturale sia importante, quella applicativa è spesso il vero collo di bottiglia.

Questo ci porta a una riflessione: così come disegniamo un DR sostenibile dal punto di vista operativo, dovremmo progettare anche le applicazioni in modo che siano sostenibili dal punto di vista del recovery. Il movimento DevOps va proprio in questa direzione: applicazioni più modulari, documentate e ripristinabili.

Quando pensiamo alla nostra “bolla”, dobbiamo considerare anche la rete. L’ambiente di DR deve essere isolato, ma con i servizi minimi necessari: una copia dell’Active Directory, firewall, servizi ponte sicuri per accedervi. Da quella bolla non deve uscire nemmeno un bit: se dei dati di test finissero nella produzione, sarebbero guai seri.
Questa esigenza di isolamento, però, rende il setup più difficile. Spesso le applicazioni dipendono da componenti esterne non replicabili nella bolla, e quindi si decide di non testarle. Ma questo è pericoloso: se un’applicazione non viene mai accesa e verificata, non possiamo sapere se funzionerà davvero in emergenza. È come non testare il ripristino di un backup.

Oggi le tecnologie di backup sono molto affidabili: è raro che un backup non sia ripristinabile. Ma il rischio di costruire un DR su ipotesi sbagliate è ancora altissimo.
Molte aziende, ad esempio, fanno una copia cifrata dei dati su cloud come ultimo paracadute. Ottimo, ma bisogna considerare anche i tempi e i costi di restore: scaricare 20 terabyte da un cloud può richiedere giorni e costare caro. Anche questo va testato.

Spesso il sito di DR non ha la stessa capacità del sito principale: meno banda, meno storage, meno potenza. È comprensibile, ma può rivelarsi un errore.
Se il disastro colpisce il sito primario, saremo costretti a lavorare dal secondario, e se lì la banda è insufficiente, il ripristino sarà lentissimo.
Durante i test bisogna simulare queste condizioni reali: se scaricare i dati dal cloud richiede giorni, forse la nostra architettura va ripensata. Non basta dire “andrò più lento”, perché a volte “più lento” significa “inutilizzabile”.

A questo punto entriamo in un tema spesso dimenticato: il rollback.
Molti piani di DR, anche ben fatti, non prevedono come tornare indietro una volta attivato il sito di recovery. Abbiamo sentito dire: “se andiamo in DR, quello diventa il nuovo ambiente di produzione”. Ma non è sempre accettabile.
Dobbiamo sapere come riportare tutto alla normalità, soprattutto nei casi – oggi più comuni – in cui il disastro è di tipo cyber e il sito primario non è stato distrutto. Dopo la bonifica, quel sito può tornare operativo, e bisogna avere un piano per rientrare.

Il rollback non è semplice: spesso richiede un fermo servizio pianificato, sincronizzazioni, test, e può durare quanto il DR stesso. Ma è necessario.
Inoltre, anche l’ambiente di DR deve avere un proprio sistema di backup e di monitoraggio. Non possiamo smettere di fare backup solo perché siamo “dall’altra parte”. Anzi, spesso i backup sono proprio ciò che ci serve per tornare indietro.

Un sistema di monitoraggio efficace è anche un aiuto prezioso nel rollback: se lo portiamo in DR e aggiorniamo i suoi puntamenti, possiamo vedere subito cosa funziona e cosa no, senza dover controllare tutto manualmente.
Purtroppo, nella maggior parte dei casi, i sistemi di monitoraggio sono eccellenti sul sito primario e assenti sul DR: se il principale va giù, restiamo ciechi.

Infine, un ultimo punto normativo: la DORA.
Questa normativa prevede che i fornitori critici siano sostituibili, e che esista un piano di uscita. Ciò vale per consulenti, fornitori di manutenzione e, naturalmente, per i servizi cloud.
In pratica, se il nostro provider di posta o di infrastruttura IaaS non è più affidabile – per guasti, costi, problemi di sicurezza o motivi geopolitici – dobbiamo essere in grado di migrare altrove.
Avere un piano di spostamento da un fornitore all’altro non è un DR in senso stretto, ma gli somiglia molto: implica comprendere come sono fatte le nostre applicazioni, dove risiedono i dati e come spostarli in sicurezza.

Chiudiamo quindi questa terza parte avendo toccato tutti i punti che ci eravamo proposti: testing, automazione, rollback, cloud e normative.
Ma non vogliamo fermarci qui.
Nella prossima puntata inviteremo Mattia Parise, esperto di data protection e disaster recovery, per approfondire questi temi dal punto di vista di chi li vive ogni giorno sul campo.
Gli chiederemo come cambia la progettazione del DR in presenza di incidenti cyber, quali sono le nuove sfide della cyber recovery, e come si può rendere davvero resiliente un’infrastruttura moderna.

Ci piace molto il termine cyber recovery: sposta l’attenzione dal disastro fisico al problema informatico, che oggi è molto più probabile.
Nelle nostre esperienze, i disastri fisici sono rari, mentre gli incidenti cyber si contano ogni anno. E spesso richiedono 5, 7 o anche 10 giorni solo per riattivare i servizi principali, con il rischio di non avere subito i dati più recenti.
Questo dimostra che il tema della resilienza cyber non è più teorico: è quotidiano.

Molti piani di DR, nati per eventi fisici, non sopravviverebbero a un incidente cyber, perché l’attacco compromette anche i sistemi su cui contiamo per ripartire. Lo abbiamo visto persino durante alcune tabletop exercise: nel giro di poche ore ci siamo accorti che l’intero impianto di DR non avrebbe retto.
Per questo vogliamo confrontarci con Mattia e capire come ripensare l’architettura in questo nuovo scenario.

Chi ci ascolta potrà anche inviarci domande o spunti da rivolgere direttamente a lui.
E con questo chiudiamo la puntata: ci aggiorneremo alla prossima, con un ospite speciale e nuovi punti di vista sul mondo del Disaster e Cyber Recovery.
