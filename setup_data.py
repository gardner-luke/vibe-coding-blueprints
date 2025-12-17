import subprocess
import os
import sys

def load_config(config_path="config.yaml"):
    """Simple YAML parser for flat key-values to avoid dependencies"""
    config = {}
    try:
        with open(config_path, "r") as f:
            for line in f:
                # Remove comments and whitespace
                line = line.split("#")[0].strip()
                if not line or ":" not in line:
                    continue
                
                key, val = line.split(":", 1)
                key = key.strip()
                val = val.strip().strip('"\'')
                
                # Only care about top-level keys for now
                if key not in config:
                    config[key] = val
        return config
    except FileNotFoundError:
        print(f"Error: {config_path} not found.")
        sys.exit(1)

def run_command(cmd, cwd=None):
    print(f"Running: {' '.join(cmd)}")
    try:
        subprocess.run(cmd, cwd=cwd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command failed with exit code {e.returncode}")
        sys.exit(e.returncode)

def main():
    config = load_config()
    
    required_vars = ["catalog", "schema"]
    missing = [v for v in required_vars if v not in config]
    
    if missing:
        print(f"Error: Missing required variables in config.yaml: {', '.join(missing)}")
        sys.exit(1)
        
    catalog = config["catalog"]
    schema = config["schema"]
    
    bundle_dir = "fsa_env_setup"
    if not os.path.isdir(bundle_dir):
        print(f"Error: Directory {bundle_dir} not found.")
        sys.exit(1)

    print(f"Deploying data bundle using Catalog: {catalog}, Schema: {schema}...")
    
    # Deploy bundle
    run_command([
        "databricks", "bundle", "deploy",
        "--var", f"catalog={catalog}",
        "--var", f"schema={schema}"
    ], cwd=bundle_dir)
    
    # Run load_data_job
    print("\nRunning load data job...")
    run_command([
        "databricks", "bundle", "run", "load_data_job",
        "--var", f"catalog={catalog}",
        "--var", f"schema={schema}"
    ], cwd=bundle_dir)
    
    print("\n✅ Data setup complete!")

if __name__ == "__main__":
    main()

