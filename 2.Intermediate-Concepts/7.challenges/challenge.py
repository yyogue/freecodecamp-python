'''
Task: Build a Simple Contact Book

Steps:
1. Use OOP to create a Contact class.
2. Store contacts in an SQLite database.
3. Add functions to:
   - Add a contact
   - View all contacts
   - Search for a contact
'''

import sqlite3


class Contact:
    def __init__(self, name, email, phone):
        """Initialize a contact with name, email, and phone number."""
        self.name = name
        self.email = email
        self.phone = phone

    def add(self):
        """Adds a contact to the SQLite database."""
        conn = sqlite3.connect("contacts.db")  # Connect to database
        cursor = conn.cursor()

        # Create table if it does not exist
        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL
            )'''
        )

        # Insert the contact details
        cursor.execute(
            "INSERT INTO contacts (name, email, phone) VALUES (?, ?, ?)",
            (self.name, self.email, self.phone)
        )

        conn.commit()  # Save changes
        conn.close()  # Close connection

        print(f"✅ Contact '{self.name}' added successfully!")

    @staticmethod
    def view_all():
        """Fetches and displays all contacts."""
        conn = sqlite3.connect("contacts.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM contacts")  # Retrieve all records
        rows = cursor.fetchall()

        conn.close()  # Close connection

        if not rows:
            print("📂 No contacts found.")
        else:
            print("\n📜 Contact List:")
            for row in rows:
                print(
                    f"🆔 ID: {row[0]}\n"
                    f"    📛 Name: {row[1]}\n"
                    f"    📧 Email: {row[2]}\n"
                    f"    📞 Phone: {row[3]}"
                )

    @staticmethod
    def search(name):
        """Searches for a contact by name."""
        conn = sqlite3.connect("contacts.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM contacts WHERE name LIKE ?",
            (f"%{name}%",)
        )

        rows = cursor.fetchall()

        conn.close()  # Close connection

        if not rows:
            print(f"❌ No contact found with the name '{name}'.")
        else:
            print("\n🔍 Search Results:")
            for row in rows:
                print(
                    f"🆔 ID: {row[0]}\n"
                    f"    📛 Name: {row[1]}\n"
                    f"    📧 Email: {row[2]}\n"
                    f"    📞 Phone: {row[3]}"
                )


# Example Usage:
if __name__ == "__main__":
    # Adding contacts
    new_contact1 = Contact("Youssouf", "youssouf@example.com", "123-456-7890")
    new_contact1.add()

    new_contact2 = Contact("Ibrahim", "ibrahim@example.com", "987-654-3210")
    new_contact2.add()

    # Viewing all contacts
    Contact.view_all()

    # Searching for a contact
    Contact.search("Youssouf")
