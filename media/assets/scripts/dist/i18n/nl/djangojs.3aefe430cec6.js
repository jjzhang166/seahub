(function(e){var t=e.django||(e.django={});t.pluralidx=function(e){var t=e!=1;return typeof t=="boolean"?t?1:0:t},t.catalog={"%curr% of %total%":"%curr% van %total%","Close (Esc)":"Sluiten (Esc)","Deleted directories":"Verwijderde mappen","Deleted files":"Verwijderde bestanden","Failed. Please check the network.":"Mislukt. Controleer de netwerkverbinding.","Loading failed":"Ophalen mislukt","Name is required":"Naam is verplicht","New files":"Nieuwe bestanden","Next (Right arrow key)":"Volgende (rechter pijltjestoets)","No matches":"Niet gevonden","Open in New Tab":"Open in nieuw tabblad","Password is too short":"Wachtwoord is te kort","Please enter 1 or more character":"Voer 1 of meer tekens in.","Please enter password":"Voer het wachtwoord in","Previous (Left arrow key)":"Vorige (linker pijltjestoets)","Rename Directory":"Hernoem map","Rename File":"Hernoem Bestand","Search users or enter emails":"Zoek gebruikers of voer emails in","Searching...":"Aan het zoeken...",Success:"Gelukt","Uploaded bytes exceed file size":"Geüploadde bytes overtreft bestandsgrootte"},t.gettext=function(e){var n=t.catalog[e];return typeof n=="undefined"?e:typeof n=="string"?n:n[0]},t.ngettext=function(e,n,r){var i=t.catalog[e];return typeof i=="undefined"?r==1?e:n:i[t.pluralidx(r)]},t.gettext_noop=function(e){return e},t.pgettext=function(e,n){var r=t.gettext(e+""+n);return r.indexOf("")!=-1&&(r=n),r},t.npgettext=function(e,n,r,i){var s=t.ngettext(e+""+n,e+""+r,i);return s.indexOf("")!=-1&&(s=t.ngettext(n,r,i)),s},t.interpolate=function(e,t,n){return n?e.replace(/%\(\w+\)s/g,function(e){return String(t[e.slice(2,-2)])}):e.replace(/%s/g,function(e){return String(t.shift())})},t.formats={DATETIME_FORMAT:"j F Y H:i",DATETIME_INPUT_FORMATS:["%d-%m-%Y %H:%M:%S","%d-%m-%y %H:%M:%S","%Y-%m-%d %H:%M:%S","%d-%m-%Y %H.%M:%S","%d-%m-%y %H.%M:%S","%d-%m-%Y %H:%M","%d-%m-%y %H:%M","%Y-%m-%d %H:%M","%d-%m-%Y %H.%M","%d-%m-%y %H.%M","%d-%m-%Y","%d-%m-%y","%Y-%m-%d","%Y-%m-%d %H:%M:%S.%f"],DATE_FORMAT:"j F Y",DATE_INPUT_FORMATS:["%d-%m-%Y","%d-%m-%y","%Y-%m-%d"],DECIMAL_SEPARATOR:",",FIRST_DAY_OF_WEEK:"1",MONTH_DAY_FORMAT:"j F",NUMBER_GROUPING:"3",SHORT_DATETIME_FORMAT:"j-n-Y H:i",SHORT_DATE_FORMAT:"j-n-Y",THOUSAND_SEPARATOR:".",TIME_FORMAT:"H:i",TIME_INPUT_FORMATS:["%H:%M:%S","%H.%M:%S","%H.%M","%H:%M"],YEAR_MONTH_FORMAT:"F Y"},t.get_format=function(e){var n=t.formats[e];return typeof n=="undefined"?e:n},e.pluralidx=t.pluralidx,e.gettext=t.gettext,e.ngettext=t.ngettext,e.gettext_noop=t.gettext_noop,e.pgettext=t.pgettext,e.npgettext=t.npgettext,e.interpolate=t.interpolate,e.get_format=t.get_format})(this);