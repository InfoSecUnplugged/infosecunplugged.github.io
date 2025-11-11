In questa puntata di Info Sec. Unplugged vogliamo condividere le nostre riflessioni su come selezionare una soluzione di EDR. È un argomento vasto, e non sappiamo mai bene da dove partire, ma proviamo a raccontare la nostra esperienza, così come l’abbiamo maturata sul campo.

Quando parliamo di EDR, pensiamo a due contesti principali: da un lato, l’azienda che acquista e gestisce autonomamente la soluzione; dall’altro, chi la usa professionalmente in un contesto di MDR, SOC o defense service, quindi dalla parte “blu”.

Le esigenze, le competenze e l’approccio operativo cambiano completamente tra i due casi.

Abbiamo imparato che un EDR, in linea generale, si basa su tre componenti principali.

La prima è quella statica, ereditata dal vecchio mondo antivirus basato su firme: controlla se un file appartiene a qualcosa di già noto.

Poi c’è la parte dinamica, che lavora con sandbox, spesso in cloud, dove i file sospetti vengono “detonati” per osservare il loro comportamento. Questo punto è cruciale: l’uso del cloud comporta che i file analizzati vengano trasferiti all’esterno, e in contesti con politiche molto restrittive questo può essere un vincolo serio.

Infine, c’è l’analisi comportamentale, la parte più “intelligente”, che interpreta pattern e comportamenti sospetti. È il cuore moderno delle piattaforme, ma anche il terreno dove si gioca la sfida dell’evasion.

Abbiamo citato un ottimo speech di Seclabs del 2022, che spiega come vengono condotti i bypass comportamentali, e anche il libro Evading EDR, che entra a fondo nelle tecniche di analisi ed elusione.

L’idea di fondo è semplice: chi costruisce, chi evade e chi difende giocano tutti sullo stesso terreno, quello dell’analisi dei comportamenti.

Un altro elemento cruciale è come il sistema presenta le informazioni. Gli EDR generano una grande quantità di dati, ma l’analista deve saperli leggere e comprendere. L’usabilità, quindi, è un fattore chiave.

La dashboard deve essere chiara, coerente e basata su standard come MITRE ATT&CK, così da consentire triage e investigazioni efficaci.

Chi lavora in un SOC o un MDR lo sa bene: la qualità dell’interfaccia impatta direttamente la capacità di reazione.

Perciò, tra i criteri di selezione, mettiamo al primo posto proprio l’usabilità.

Poi c’è la questione della detection. È vero che, nelle soluzioni di fascia alta, i livelli di rilevamento sono simili, ma non per questo possiamo dare tutto per scontato.

Il testing è fondamentale: mettere alla prova le soluzioni per capire se fanno davvero ciò che promettono.

Eppure, nella pratica, lo vediamo raramente. Le aziende spesso comprano una soluzione e si fidano che funzioni, senza verificarla.

È una lacuna culturale: mancano competenze, tempo e mentalità sperimentale. Eppure, come diciamo sempre, testare le proprie difese è parte integrante della postura di sicurezza.

Abbiamo visto due modalità di test.

Una è automatizzata: una batteria di attacchi simulati verifica la capacità di rilevamento della piattaforma.

L’altra è manuale, più mirata, dove si prova a bypassare consapevolmente la soluzione.

Purtroppo, la maggior parte delle aziende non lo fa né prima né dopo l’acquisto, salvo i contesti più maturi – tipicamente quelli bancari – dove esistono team dedicati alla sicurezza.

Per chi non può testare, i report indipendenti possono essere utili, ma vanno letti con attenzione: devono essere aggiornati, perché il panorama evolve velocemente.

Un report del 2021, oggi, non ha più alcuna validità operativa.

E qui entra in gioco un altro fattore essenziale: la Threat Intelligence.

La capacità del vendor di aggiornare tempestivamente il proprio database di indicatori di compromissione (IOC) è ciò che fa la differenza tra bloccare un attacco al primo round o al secondo.

Chi dispone di un team di TI interno avrà soluzioni più aggiornate e pronte rispetto a chi si affida solo a fonti esterne.

Anche questo è un criterio di valutazione concreto: la velocità e la qualità dell’intelligence del vendor.

Poi c’è il tema della gestione.

Molte aziende acquistano un EDR, ma non lo gestiscono.

Abbiamo visto più volte piattaforme lasciate senza supervisione, con alert disattesi, o addirittura mai configurate.

Questo succede perché i team IT spesso non hanno le competenze né il tempo per occuparsene in modo continuativo.

Da qui la necessità, quasi inevitabile, di delegare la gestione a un servizio MDR esterno.

Avere un EDR senza presidio equivale, di fatto, a non averlo.

Un aspetto interessante è anche quello culturale: chi lavora nel mondo della sicurezza tende a cercare ambienti stimolanti, quindi mantenere internamente risorse altamente specializzate è difficile, costoso e poco sostenibile nel tempo.

Abbiamo poi toccato il tema della Tyber e del Red Teaming, introdotti nel settore finanziario come standard di test obbligatori.

È la prima volta che un framework normativo mette per iscritto l’obbligo di testare realmente la postura difensiva, non solo di dimostrarla a parole.

Da lì nasce l’idea di Adversary Simulation: prendere in prestito dal Red Teaming alcune pratiche concrete e applicarle anche alle aziende di medie dimensioni, in modo proporzionato ma utile.

Nel processo di scelta di una soluzione, contano anche aspetti più tecnici.

La pervasività sugli endpoint, per esempio: quanto è ampia la copertura su Windows, Linux e macOS?

Molte piattaforme offrono agent per tutti, ma non sempre le funzionalità sono equivalenti.

In particolare, sugli ambienti Linux e macOS, la capacità di detection è spesso ridotta rispetto a Windows.

Lo stesso vale per i sistemi legacy o industriali: la compatibilità va verificata a fondo, specialmente nel medicale e nell’OT.

E non dimentichiamo la virtualizzazione: gli EDR installati sul desktop non sempre vedono cosa accade dentro le macchine virtuali o nei container, e questa è un’area che molti attaccanti sfruttano con astuzia.

Lo stesso vale per i sistemi mobile: iOS e Android sono sempre più usati in contesti aziendali, ma l’effettiva capacità degli agent di proteggerli resta limitata. In questi casi, un buon MDM e policy rigorose spesso valgono più di una protezione EDR tradizionale.

Infine, la nostra esperienza ci porta a una conclusione semplice: scegliere un EDR non è solo una questione tecnica o commerciale, ma una valutazione che deve includere usabilità, detection, threat intelligence, compatibilità e gestione.

Senza questi cinque pilastri, il rischio è di avere una tecnologia avanzata… ma di fatto spenta.
