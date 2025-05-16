import csv

def csv_to_vcard(csv_filename, vcf_filename):
    with open(csv_filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        with open(vcf_filename, 'w', encoding='utf-8') as vcf_file:
            for row in reader:
                name = row['Name']
                number = row['Number']
                vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL;TYPE=CELL:{number}
END:VCARD
"""
                vcf_file.write(vcard)
    print(f"vCard file '{vcf_filename}' created successfully.")

if __name__ == "__main__":
    csv_file = 'contacts.csv'   # Your CSV file name
    vcf_file = 'contacts.vcf'   # Output vCard file
    csv_to_vcard(csv_file, vcf_file)
