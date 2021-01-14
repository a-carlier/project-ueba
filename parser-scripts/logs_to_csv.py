import sys
import re
    

def to_csv():

  regex = r'([0-9]{2})\:([0-9]{2})\:([0-9]{2})\.([0-9]{6}) IP ((?:25[0-5]\.|2[0-4][0-9]\.|[0-1]?[0-9]{1,2}\.){3}(?:25[0-5]|2[0-4][0-9]|[0-1]?[0-9]{1,2}))\.([0-9]{1,9}) \> ((?:25[0-5]\.|2[0-4][0-9]\.|[0-1]?[0-9]{1,2}\.){3}(?:25[0-5]|2[0-4][0-9]|[0-1]?[0-9]{1,2}))\.([0-9]{1,9})\:.+(ICMP|UDP|Flags)'

  fout = open('CSV/all_logs.csv', "w")
  fout.write('day,hours,minutes,seconds,microseconds,ip_source,port_source,ip_dest,port_dest,protocol\n')

  for i in range(0, 30):
    filename = 'pflog.' + str(i) + '.bz2.log'
    f = open('LOGS/' + filename)
    print('INFO: Read file ' + filename)

    for line in f:
      regex_results = re.search(regex, line)

      if (regex_results == None):
        print('ERROR: Cannot Parse: ' + line)
        continue

      object_line = {}
      object_line['day'] = str(i)
      object_line['hours'] = regex_results.group(1)
      object_line['minutes'] = regex_results.group(2)
      object_line['seconds'] = regex_results.group(3)
      object_line['microseconds'] = regex_results.group(4)
      object_line['ip_source'] = regex_results.group(5)
      object_line['port_source'] = regex_results.group(6)
      object_line['ip_dest'] = regex_results.group(7)
      object_line['port_dest'] = regex_results.group(8)
      object_line['protocol'] = regex_results.group(9).upper()
      if object_line['protocol'] == 'FLAGS':
        object_line['protocol'] = 'TCP'

      fout.write(object_line['day'] + ',' + object_line['hours'] + ',' + object_line['minutes'] + ',' + object_line['seconds'] + ',' + object_line['microseconds'] + ',' + object_line['ip_source'] + ',' + object_line['port_source'] + ',' + object_line['ip_dest'] + ',' + object_line['port_dest'] + ',' + object_line['protocol'] + '\n')
  
    
    f.close()

  fout.close()


if __name__ == "__main__":
  to_csv()
  
