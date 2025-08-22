# importing modules
import logging
import yaml
import argparse



# CLI arguments
parser = argparse.ArgumentParser()
parser.add_argument("--config", default="config/config.yaml", help="Path to config file")
args = parser.parse_args()


# Load config
with open(args.config, "r") as f:
    config = yaml.safe_load(f)


# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(config["log_file"]),
        logging.StreamHandler()
    ]
)


# Example "Hello Project" log
logging.info(f" Project:- {config['project_name']}")
logging.info(f" Stage:- {config['stage']}")
logging.info(f" Message:- {config['message']}")
logging.info(f" Credit:- {config['Credit']}")