# gdb/domain/account_rules_properties_loader.py
import os

class AccountRulesPropertiesLoader:
    """Utility loading external .properties files."""

    @staticmethod
    def load_rules(account_type: str) -> dict:
        if not account_type or not account_type.strip():
            return {}
        filename = f"{account_type.strip().lower()}.properties"
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "resources", "config", "rules", filename)
        if not os.path.isfile(path):
            return {}
        rules = {}
        with open(path, encoding="utf-8") as rules_file:
            for line_number, raw_line in enumerate(rules_file, start=1):
                line = raw_line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" not in line:
                    raise ValueError(f"Malformed rule in {filename} at line {line_number}")
                key, value = line.split("=", 1)
                if not key.strip() or not value.strip():
                    raise ValueError(f"Malformed rule in {filename} at line {line_number}")
                rules[key.strip()] = value.strip()
        return rules
