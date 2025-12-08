import configparser

config_file = "test.ini"

config = configparser.ConfigParser(inline_comment_prefixes='#')  # Inline comments in the config file start with "#".
config.optionxform = str  # Preserve case of the keys.
config.read(config_file, encoding='utf-8')
action = config.get("Simulation", "action", fallback="results_only")
action2 = config.get("Simulation", "findes_ikke", fallback="results_only")
print()
