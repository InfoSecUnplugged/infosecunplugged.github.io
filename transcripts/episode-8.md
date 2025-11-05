Quando parliamo di sicurezza nel mondo industriale, ci viene sempre in mente come certe evoluzioni dell’IT abbiano seguito percorsi curiosi. Prima di occuparci di rete, molti di noi venivano dallo storage, quello vero: i grandi armadi, i cavi lunghi metri, le connessioni in fibra. Abbiamo amato il Fiber Channel, un protocollo complesso ma affidabile. A un certo punto, però, qualcuno decise che era troppo costoso e che si poteva “semplificare” usando l’Ethernet e inventando l’iSCSI, definito allora “il Fiber Channel dei poveri”.

L’idea di trasportare un protocollo time-sensitive come lo SCSI su una rete Ethernet, dove i pacchetti possono essere bloccati anche per un minuto, si rivelò presto problematica. Eppure, in molti provarono comunque a far convergere rete e storage: nacque così il Fiber Channel over Ethernet (FCoE). L’idea era buona, ma la complessità la fece fallire.

Oggi stiamo ripetendo una storia simile. Portiamo Ethernet – una tecnologia che “può fallire by design” – dentro al mondo industriale, dove invece latenza e certezza di consegna sono fondamentali. Se un impianto smette di comunicare, si ferma. Eppure si tende a sottovalutare il rischio, facendo assunzioni sbagliate come “uso un kernel vecchio perché lo conosco”.

Abbiamo ripercorso questa storia informatica per ricordare che ogni cambiamento di tecnologia deve rispettare i requisiti tecnici di partenza. Nel tempo, le reti e gli storage si sono evoluti insieme, adattandosi. Ma nel mondo OT (Operational Technology), questo processo è appena cominciato. I produttori di macchine dovranno imparare a renderle aggiornabili, monitorabili e conformi a standard come IEC 62443 o TISAX. Gli utilizzatori, invece, dovranno dotarsi di procedure per gestire aggiornamenti e sicurezza: è un’intera filiera che deve muoversi in sincronia.

Oggi ci troviamo spesso a introdurre IT in contesti industriali rimasti fermi per vent’anni. Le certificazioni impongono macchine aggiornabili, ma poi ogni aggiornamento richiede una rivalidazione completa dell’impianto: un processo costoso e che, di fatto, pochi fanno davvero.

Un altro tema critico è il monitoraggio remoto. I produttori vogliono osservare il funzionamento delle macchine per fare manutenzione predittiva o upselling, installando gateway VPN o connessioni 4G/5G. Ma molti clienti non si rendono conto che questo significa aprire un ponte diretto verso il loro impianto. Se l’integratore viene compromesso, l’attaccante entra facilmente anche nella rete industriale del cliente.

Abbiamo visto casi reali in cui è successo. Quando le aziende lo capiscono, scatta la consapevolezza: la sicurezza OT non è solo una questione tecnica, ma di protezione del business e dei brevetti.

In molti impianti, infatti, i gateway di teleassistenza sono costantemente connessi. Se un utente dell’integratore viene compromesso, può avere accesso diretto a macchine Windows che pilotano le linee di produzione. Le aziende più mature iniziano a richiedere controlli sulle sessioni di manutenzione, log, tracciabilità degli accessi e validazioni temporanee. Ma basta poco — anche un semplice ping massivo — per mandare in tilt un impianto.

Il vero problema è che la percezione del rischio è ancora bassa. Finché un’azienda non vive un incidente diretto, pensa che non le capiterà mai. Eppure, gli attacchi OT accadono davvero: ricordiamo il caso di un magazzino automatico in cui i carrelli robotici iniziarono a scontrarsi. Dopo mesi di analisi, si scoprì che un gruppo APT stava modificando da remoto il codice dei PLC.

Serve collaborazione tra IT e OT. Il mondo IT punta al controllo, quello OT alla continuità operativa. Se i due non si parlano, non può esserci sicurezza. Un buon modello di riferimento è il Purdue Model, che separa IT e OT con una DMZ intermedia. Anche se nella realtà molti impianti violano questo principio installando gateway VPN direttamente dentro la rete industriale, almeno avere un modello chiaro aiuta a capire dove intervenire.

La prima azione utile è creare confini e visibilità: segmentare, monitorare, registrare. Le aziende dovrebbero pretendere dai fornitori che le macchine industriali supportino strumenti di monitoraggio e aggiornamento, anche con ritmi diversi da quelli IT. È tempo che il cliente finale chieda requisiti di sicurezza anche ai produttori.

Parlando di aggiornamenti, abbiamo notato che spesso si evita di patchare sistemi Windows HMI per paura che “si rompa tutto”. Ma nella maggior parte dei casi, non succede nulla. Questa paura nasce da software scritti male, che non tollerano variazioni. Nel mondo IT, questo problema è quasi sparito perché un software debole oggi viene bucato subito. Nell’OT, invece, il principio è ancora: “finché funziona, non toccarlo”.

Anche la rete è un problema. Quasi tutti gli impianti escono con la stessa configurazione: 192.168.1.0/24. Finché restano isolati, può andare bene, ma appena li colleghi a una rete aziendale diventa un disastro. Cambiare indirizzamento spesso è impossibile, perché i dispositivi non lo permettono: serve flashare un firmware con un tool proprietario. Tutto “hardcoded”, come nei vecchi bus industriali.

E così, quando abbiamo collegato IT e OT grazie all’Industria 4.0, sono arrivati i veri problemi. Gli impianti non erano progettati per convivere. Le tecnologie IT — NAC, segmentazione L2, VLAN, PVLAN — possono aiutare, ma nel mondo OT la compatibilità è scarsa e ogni tentativo di controllo viene percepito come un rischio operativo.

Molte di queste soluzioni nascono proprio per l’OT. Ad esempio, la segmentazione trasparente L2 e le private VLAN furono pensate per gestire reti industriali con topologie rigide. Ma spesso vengono implementate male o per caso: una tecnologia nata da un “bug” diventata poi feature. Alcune di queste soluzioni, pur non eleganti dal punto di vista di rete, permettono di creare “bolle” di sicurezza tra linee produttive diverse senza toccare i dispositivi.

Alla fine, tutto si riduce a un principio semplice: non possiamo aggiornare o cambiare il mondo OT ogni sei mesi, ma possiamo costruirgli intorno un perimetro di sicurezza e guardare dentro con strumenti di visibilità e detection.

Solo così possiamo reagire prima che il danno diventi catastrofico.

E intanto, continuiamo a parlarne — perché di strada da fare ce n’è ancora molta.
