import csv
import datetime

print("Start writing XML")

# Import CSV file
csvFile = input('/Users/seadsoftic/Desktop/csv_to_xml_in_python/daten.csv')
# Look for current date
dateNow = datetime.datetime.now()
# Create a new XML file
xmlFile = 'kundenDaten-' + dateNow.strftime('%Y-%m-%d') + '.xml'

# Read the CSV file
csvData = csv.reader(open(csvFile), delimiter=';')
# Write the XML file
xmlData = open(xmlFile, 'w')
xmlData.write('<?xml version="1.0" encoding="utf-8"?>\n')
xmlData.write('<Kunden_Daten>' + "\n")

# Removing duplicates
tempData = []
for i in csvData:
    if i not in tempData:
        tempData.append(i)
csvData = tempData

rowNum = 0
for row in csvData:
    if rowNum == 0:
        tags = row
        for i in range(len(tags)):
            # Replacing ...
            tags[i] = tags[i].replace('  ', ' ')
    else:
        xmlData.write('  <Kunde>\n')
        for i in range(len(tags)):
            # Replacing ...
            row[i] = row[i].replace('+49', '0')
            row[i] = row[i].replace('+', '00')
            row[i] = row[i].replace('  ', ' ')
            row[i] = row[i].replace('ä', 'ae')
            row[i] = row[i].replace('Ä', 'AE')
            row[i] = row[i].replace('ö', 'oe')
            row[i] = row[i].replace('OE', 'OE')
            row[i] = row[i].replace('ü', 'ue')
            row[i] = row[i].replace('Ü', 'UE')
            row[i] = row[i].replace('ß', 'ss')
            row[i] = row[i].replace('Herr', '')
            row[i] = row[i].replace('Frau', '')
            row[i] = row[i].replace('-', '')
            row[i] = row[i].replace('/', '')
            row[i] = row[i].replace('Wasserwirtschaftsamt', 'WWA')
            row[i] = row[i].replace('Wasserverband', 'WV')
            row[i] = row[i].replace('Wasser und Schifffahrtsamt', 'WSA')
            row[i] = row[i].replace('Wasserstrassen u. Schifffahrtsamt', 'WAS')
        # XML structure
        xmlData.write('    ' + '<Kundennummer>' + row[0] + '</Kundennummer>\n')
        xmlData.write('    ' + '<Lieferantennummer>' + row[1] +
                      '</Lieferantennummer>\n')
        xmlData.write('    ' + '<Firma-Name>' + row[2] + '</Firma-Name>\n')
        xmlData.write('    ' + '<Ansprechpartner>' + row[3] +
                      '</Ansprechpartner>\n')
        xmlData.write('    ' + '<Abteilung>' + row[4] + '</Abteilung>\n')
        xmlData.write('    ' + '<Unterabteilung>' + row[5] +
                      '</Unterabteilung>\n')
        xmlData.write('    ' + '<Email>' + row[6] + '</Email>\n')
        xmlData.write('    ' + '<Telefonnnummer>' + row[7] +
                      '</Telefonnnummer>\n')
        xmlData.write('    ' + '<Telefax>' + row[8] + '</Telefax>\n')
        xmlData.write('    ' + '<Mobil>' + row[9] + '</Mobil>\n')
        xmlData.write('    ' + '<Strasse>' + row[10] + '</Strasse>\n')
        xmlData.write('    ' + '<PLZ>' + row[11] + '</PLZ>\n')
        xmlData.write('    ' + '<Ort>' + row[12] + '</Ort>\n')
        xmlData.write('    ' + '<Land>' + row[13] + '</Land>\n')
        xmlData.write('    ' + '<Projekt>' + row[14] + '</Projekt>\n')
        xmlData.write('    ' + '<Typ>' + row[15] + '</Typ>\n')
        xmlData.write('    ' + '<Anschreiben>' + row[16] + '</Anschreiben>\n')

        xmlData.write('  </Kunde>\n')

    rowNum += 1

xmlData.write('</Kunden_Daten>\n')
# Close XML file
xmlData.close()

print("End writing XML")