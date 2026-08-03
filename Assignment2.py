import functools

def bold_text(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"**{result}**"
    return wrapper

class Report:
    _templates = {}

    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    @classmethod
    def register_template(cls, name: str, template_func):
        cls._templates[name] = template_func

    @classmethod
    def get_template(cls, name: str):
        return cls._templates.get(name)

    @classmethod
    def list_templates(cls):
        return list(cls._templates.keys())

    def __call__(self, template_name: str) -> str:
        template = self.get_template(template_name)
        if not template:
            raise ValueError(f"Template '{template_name}' not found.")
        return template(self.title, self.content)

    def __str__(self) -> str:
        return f"Report(Title: {self.title})"

def simple_template(title: str, content: str) -> str:
    return f"--- {title} ---\n{content}\n"

@bold_text
def fancy_template(title: str, content: str) -> str:
    return f"==== REGAL REPORT: {title.upper()} ====\n>> {content}\n"

def uppercase_template(title: str, content: str) -> str:
    return f"TITLE: {title.upper()}\nCONTENT: {content.upper()}\n"

def main():
    Report.register_template("simple", simple_template)
    Report.register_template("fancy", fancy_template)
    Report.register_template("uppercase", uppercase_template)

    active_report = None

    while True:
        print("\n=== DYNAMIC REPORT GENERATOR ===")
        print("1. Create New Report")
        print("2. Generate Formatted Report")
        print("3. View Available Templates")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            title = input("Enter report title: ")
            content = input("Enter report content: ")
            active_report = Report(title, content)
            print(f"\n[Success] Report created for '{title}'.")

        elif choice == "2":
            if not active_report:
                print("\n[Error] No active report found. Please create one first (Option 1).")
                continue

            available = Report.list_templates()
            print(f"\nAvailable templates: {', '.join(available)}")
            template_name = input("Enter template name to apply: ").strip().lower()

            try:
                formatted_output = active_report(template_name)
                print("\n--- GENERATED REPORT ---")
                print(formatted_output)
            except ValueError as e:
                print(f"\n[Error] {e}")

        elif choice == "3":
            available = Report.list_templates()
            print("\nRegistered Templates:")
            for template in available:
                print(f" - {template}")

        elif choice == "4":
            print("\nExiting Report Generator. Goodbye!")
            break

        else:
            print("\n[Invalid Selection] Please choose a valid menu option.")

if __name__ == "__main__":
    main()