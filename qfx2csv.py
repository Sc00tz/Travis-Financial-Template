from datetime import datetime
import xml.etree.ElementTree as ET
import csv
import argparse

def extract_fields(xml_file, csv_file):

   # Parse the XML file
   tree = ET.parse(xml_file)
   root = tree.getroot()

   # Extract the ACCTID
   acct_id = root.find('.//ACCTID').text if root.find('.//ACCTID') is not None else ""
   
   # Open the CSV file in write mode with UTF-8 encoding
   with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
      writer = csv.writer(file)
      writer.writerow(['Account ID', 'Transaction ID',' Transaction Type', 'Transaction Date', 'Description', 'Date Posted', 'Description', 'Card Used'])

      # Iterate through each STMTTRN element
      for stmttrn in root.findall('.//STMTTRN'):

         # Extract required fields
         trntype = stmttrn.find('TRNTYPE').text
         dtposted = datetime.strptime(stmttrn.find('DTPOSTED').text[:-10], '%Y%m%d')
         trnamt = stmttrn.find('TRNAMT').text
         fitid = stmttrn.find('FITID').text
         memo = stmttrn.find('MEMO').text
            
         # Fix date for better importing to spreadsheet
         dtuser = datetime.strptime(stmttrn.find('DTUSER').text[:-10], '%Y%m%d') if stmttrn.find('DTUSER') is not None else dtposted
         ccacctto_acctid = stmttrn.find('.//CCACCTTO/ACCTID').text if stmttrn.find('.//CCACCTTO/ACCTID') is not None else ""

         # Write the fields to the CSV file
         writer.writerow([acct_id, fitid, trntype, dtuser.date(), dtposted.date(),trnamt, memo, ccacctto_acctid])

def main():

   # Parse command-line arguments
   parser = argparse.ArgumentParser(description='Extract specified fields from XML and convert to CSV')
   parser.add_argument('input', help='Input XML file')
   parser.add_argument('output', help='Output CSV file')
   args = parser.parse_args()

   # Extract fields and write to CSV
   extract_fields(args.input, args.output)
   print("QFX has been converted to CSV")

if __name__ == "__main__":
   main()
