````markdown
# CSV to vCard Converter

This Python script allows you to convert contact information from a `.csv` file into a `.vcf` (vCard) file.
vCards are widely used for importing contacts into mobile phones and email clients.

## 📁 Features

- Converts each row in a CSV to an individual vCard entry.
- Supports UTF-8 encoding for international character support.
- Outputs a `.vcf` file compatible with phones, email clients, and contact apps.

## 📋 CSV Format

Ensure your CSV file (`contacts.csv`) has the following header structure:

```csv
Name,Number
John Doe,+1234567890
Jane Smith,+1987654321
````

> Each row should contain the contact's name and phone number.

## 🛠️ How to Use

### 1. Clone the Repository

```bash
https://github.com/Roshini-r20/csv-to-vcard.git
```

### 2. Place Your CSV File

* Ensure your `contacts.csv` file is in the same directory as the script.
* The file should follow the format shown above.

### 3. Run the Script

Make sure you have Python 3 installed.

```bash
python csv_to_vcard.py
```

### 4. Get Your vCard File

* The script will generate a file named `contacts.vcf` in the same directory.
* You can now import it into your phone or email contact list.

## 📲 How to Import vCard
✅ Import on Android
* Transfer the contacts.vcf file to your Android phone (via USB, email, Google Drive, etc.).
* Open the Contacts app.
* Tap the three dots or menu and choose Import/Export.
* Choose Import from .vcf file.
* Navigate to and select the transferred contacts.vcf.
* Contacts will be added to your phone.

✅ Import on Apple
* Transfer the contacts.vcf file to your Mac.
* Open the Contacts app.
* Click File → Import…
* Select the contacts.vcf file.
* Click Open. Contacts will be added to your iCloud or local group.

## 🧪 Example

Given a `contacts.csv` with:

```csv
Name,Number
Alice,+11234567890
Bob,+10987654321
```

The script will output a `contacts.vcf` like:

```
BEGIN:VCARD
VERSION:3.0
FN:Alice
TEL;TYPE=CELL:+11234567890
END:VCARD

BEGIN:VCARD
VERSION:3.0
FN:Bob
TEL;TYPE=CELL:+10987654321
END:VCARD
```

## 📌 Requirements

* Python 3.x

No external packages are required — uses only Python’s built-in `csv` module.

## ✅ License

This project is licensed under the MIT License.

---
