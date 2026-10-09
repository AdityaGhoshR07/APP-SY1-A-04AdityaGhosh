#A program using regular expression (regex) to find email patterns.
import re
def find_emails(text: str)->list[str]:
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return re.findall(email_pattern,text)
if __name__=="__main__":
    sample_text=input("Enter text to extract emails from: ")
    matched_emails=find_emails(sample_text)

    if matched_emails:
        print("\nFound email addresses:")
        for email in matched_emails:
            print(f"-{email}")
    else:
        print("\nNo email addresses found.")